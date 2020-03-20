# coding=utf-8
import threading

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from src.base.browser import Browser
from src.thread.base_thread import BaseTread


class BugThread(BaseTread):
    """
    虫子，用于爬取数据的爬虫，多线程实现可以多线程并行多个规则，
    """

    def __init__(self, crawlingRule):
        self.browser = Browser().get_brower()
        self.crawlingRule = crawlingRule

    def run(self):
        """
        启动线程
        """
        try:
            # 爬取网页数据
            self._crawling()
        except:
            # todo 增加异常判断，规则判断
            self._stop()

    def _crawling(self):
        """
        爬取网页数据
        """
        access_url = ""
        self.browser.get(access_url)
        xpath = ""
        WebDriverWait(self.browser, 3).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
