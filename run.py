# coding=utf-8
import logging.config

from settings import LOGGIN_CONF
from src.base.log4py import logger
from src.thread.bug_factory_thread import BugFactoryThread
from src.thread.pull_command_thread import PullCommandThread
from src.thread.pull_task_thread import PullTaskThread
from src.thread.push_data_thread import PushDataThread

"""
入口启动文件类
"""


class Main:
    def run(self):
        """
        入口启动多线程开始工作
        :return:
        """
        logger.info("启动 检查命令线程")
        PullCommandThread().start()

        logger.info("启动 检查任务线程")
        PullTaskThread().start()

        logger.info("启动 虫子制造工厂")
        BugFactoryThread().start()

        logger.info("启动 推送数据线程")
        PushDataThread().start()


if __name__ == '__main__':
    try:
        logging.config.fileConfig(LOGGIN_CONF)
        log = logging.getLogger(__name__)
        log.info('>>>>> Starting server <<<<<')
        Main().run()
    except Exception as e:
        print(e)
