# coding=utf-8
import datetime
import threading
import time

from src.base.log4py import logger
from src.service.paysv import PaySV

"""
多线程启动不同设备
"""


class Process(threading.Thread):
    def __init__(self, device_id, frequency=1, debug=False):
        threading.Thread.__init__(self)
        self.device_id = str(device_id)
        self.debug = debug
        self.pay_sv = PaySV(str(device_id), debug=debug)
        self.frequency = frequency
        self.is_stop = False

    def stop(self):
        '''
        stop thread
        :return:
        '''
        logger.debug("stop thread ! ")
        self.is_stop = True
        self.join()

    def run(self):
        '''
        running thread
        :return:
        '''
        logger.debug("running thread for device [" + self.device_id + "] ")
        is_connected = False
        is_login = False

        # 尝试3次如果没有设备不在线就直接退出自己
        count_connected = 0
        while True:
            if self.is_stop:
                logger.debug("return while")
                return

            if count_connected == 3:
                self.pay_sv.delete_device(self.device_id)
                self.is_stop = True
                return

            try:
                if not is_connected:
                    is_connected = self.detect_connect()

                if is_connected:
                    logger.debug("connected to device:" + self.device_id)
                    # 获取上次登录的时间进行判断是否过期
                    device_obj = self.pay_sv.load_account_by_device_id(self.device_id)
                    if device_obj:
                        try:
                            login_time = device_obj["login_time"]
                            if login_time:
                                now_time = datetime.datetime.now().strftime('%Y%m%d000000')
                                if int(now_time) - int(login_time) == 0:
                                    # 未过期直接使用
                                    is_login = True
                                    alipay_account = device_obj["account"]
                        except:
                            pass

                    if not is_login:
                        # 过期重新登录
                        is_login, alipay_account = self.configure()

                    if is_login:
                        is_notify = self.pay_sv.detect_alipay_notify()
                        if self.debug:
                            is_notify = True

                        if is_notify:
                            self.pay_sv.detect_income(alipay_account)
                else:
                    count_connected += 1
            except:
                is_connected = False
                is_login = False
                logger.debug("lost device: " + self.device_id)

            time.sleep(self.frequency)

    def configure(self):
        """
        上线并获取基本信息给到服务器端
        :return:
        """
        return self.pay_sv.configure()

    def detect_connect(self):
        """
        设备上线检测
        :return:
        """
        return self.pay_sv.detect_connect()
