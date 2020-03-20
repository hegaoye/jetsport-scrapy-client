from src.base.enum.command_state_enum import CommandStateEnum
from src.dao.commands_dao import CommandsDao
from src.entity.commands import Commands
from src.service.base_service import BaseService


class CommandsService(BaseService):
    """
    指令服务接口
    """

    def __init__(self):
        self.commandsDao = CommandsDao()

    def load(self) -> Commands:
        """
        查询一条指令
        :return:  Commands
        """
        return self.commandsDao.load(CommandStateEnum.Init.name)

    def save(self, list) -> bool:
        """
        批量保存指令到本地库
        :param list: 集合
        :return: True/False
        """
        for command in list:
            self.commandsDao.insert(command)
        return True

    def delete(self, code) -> bool:
        """
        删除数据
        :param code: 编码
        :return: True/False
        """
        n = self.commandsDao.delete(code)
        return True if n > 0 else False
