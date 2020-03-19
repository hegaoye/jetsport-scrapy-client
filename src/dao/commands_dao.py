# coding=utf-8
from src.entity.commands import Commands


class CommandsDao:
    """
    指令dao
    """

    def load(self, state) -> Commands:
        return Commands.get(Commands.state == state)

    def insert(self, command) -> None:
        Commands.create(code=command.code, command=command.command, type=command.type, order=command.order,
                        state=command.state)

    def update(self, code, state):
        Commands.update(state=state).where(Commands.code == code).execute()
