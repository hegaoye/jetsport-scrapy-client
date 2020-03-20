# coding=utf-8
from src.entity.commands import Commands


class CommandsDao:
    """
    指令dao
    """

    def load(self, state) -> Commands:
        """
        查询一条指令
        :param state: 状态
        :return:  Commands
        """
        return Commands.select().where(Commands.state == state).order_by(Commands.order.asc())

    def insert(self, command) -> None:
        """
        插入一条指令
        :param command: 指令
        """
        Commands.create(code=command.code, command=command.command, type=command.type, order=command.order,
                        state=command.state)

    def updateStateByCode(self, code, state) -> None:
        """
        根据code 更新指令状态
        :param code: 编码
        :param state: 状态
        """
        Commands.update(state=state).where(Commands.code == code).execute()
