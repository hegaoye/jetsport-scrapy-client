# coding=utf-8
import threading

from src.thread.base_thread import BaseTread

"""
仅用于 拉取服务器端的控制命令检测
"""


class PullCommandThread(BaseTread):
    def run(self) -> None:
        pass
