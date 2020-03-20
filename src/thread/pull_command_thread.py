# coding=utf-8
from time import sleep

from src.base import http
from src.base.enum.setting_key_enum import SettingKeyEnum
from src.base.singleton import Singleton
from src.service.commands_service import CommandsService
from src.thread.base_thread import BaseTread

"""
仅用于 拉取服务器端的控制命令检测
"""


class PullCommandThread(BaseTread, Singleton):
    """
    拉取命令多线程，保持单例模式，禁止多线程跑多个实例导致指令执行的混乱
    """

    def __init__(self):
        self.commandsService = CommandsService()

    def run(self) -> None:
        pullCommandFrequce = int(self.settingService.loadValue(SettingKeyEnum.PullCommandFrequce.name))
        while True:
            try:
                flag = self.pull_commands()
                if flag:
                    self.exec_commands()
            except:
                pass

            # 休眠 n 秒钟
            sleep(pullCommandFrequce)

    def pull_commands(self) -> bool:
        """
        拉取云端 控制指令
        1.拉取云端的指令
        2.存储指令到数据库中
        :return: True/False
        """
        url = self.settingService.loadValue(SettingKeyEnum.PullCommandUrl.name)
        r = http.get(url)
        if r.success:
            try:
                return self.commandsService.save(r.data)
            except:
                return False
        return False

    def exec_commands(self):
        """
        执行指令并进行控制
        1.执行指令
        2.删除指令
        :return:
        """
        # 1.执行指令
        command = self.commandsService.load()
        if command:
            # todo 执行指令

            # 2.删除指令
            self.commandsService.delete(command.code)
