# coding=utf-8
from time import sleep

from src.base.browser import Browser
from src.base.enum.get_value_type_enum import GetValueTypeEnum
from src.base.enum.result_type_enum import ResultTypeEnum
from src.base.enum.xpath_type_enum import XpathTypeEnum
from src.base.enum.y_n_enum import YNEnum
from src.entity.crawling_data import CrawlingData
from src.service.crawling_data_service import CrawlingDataService
from src.service.crawling_rule_service import CrawlingRuleService
from src.thread.base_thread import BaseTread


class BugThread(BaseTread):
    """
    虫子，用于爬取数据的爬虫，多线程实现可以多线程并行多个规则，
    """

    def __init__(self, crawlingRule=None):
        self.browser = Browser().get_brower()
        self.crawlingRule = crawlingRule
        self.crawlingRuleService = CrawlingRuleService()
        self.crawlingDataService = CrawlingDataService()

    def run(self):
        """
        启动线程
        """
        try:
            # 爬取网页数据
            self.__crawling()
        except:
            # todo 增加异常判断，规则判断
            self.stop()

    def __crawling(self):
        """
        爬取网页数据
        """
        # 如果是参数规则则爬取
        if self.crawlingRule.is_parameter == YNEnum.Y.name:
            if self.crawlingRule.result_type == ResultTypeEnum.List.name:
                access_url = self.crawlingRule.access_url
                xpath = self.crawlingRule.xpath
                elements = self.list(access_url, xpath)
                for element in elements:
                    if self.crawlingRule.get_value_method == GetValueTypeEnum.Text.name:
                        data = element.text
                    else:
                        data = element.get_attribute(self.crawlingRule.html_attr)

        elif self.crawlingRule.is_parameter != YNEnum.N.name:
            # 如果不是参数规则则不爬取
            if self.crawlingRule.xpath_type == XpathTypeEnum.Click.name:
                self.browser.find_element_by_xpath(self.crawlingRule.xpath).click()

    def list(self, access_url, data_xpath, click_xpath=None) -> list:
        if not access_url:
            return

        # 打开url页面
        self.browser.get(access_url)

        # 如果需要点击则找到元素进行点击
        if click_xpath:
            self.browser.find_element_by_xpath(click_xpath).click()
            # 点击后默认等待加载 3s
            sleep(3)

        # 获取集合元素
        elements = self.browser.find_elements_by_xpath(data_xpath)
        if not elements:
            # todo 如果找不到则报错，进行规则报错
            pass

        return elements

    def detail(self, data_xpath, click_xpath, get_value_type, value_attribute=None) -> object:
        # 如果需要点击则找到元素进行点击
        if click_xpath:
            self.browser.find_element_by_xpath(click_xpath).click()
            # 点击后默认等待加载 3s
            sleep(3)

        element = self.browser.find_element_by_xpath(data_xpath)

        # 获取值的方式
        if get_value_type == GetValueTypeEnum.Text.name:
            data = element.text
        elif get_value_type == GetValueTypeEnum.Attribute.name and value_attribute:
            data = element.get_attribute(value_attribute)

        return data

    def detail_with_url(self, access_url, data_xpath, click_xpath, get_value_type, value_attribute=None) -> object:
        if access_url:
            # 打开url页面
            self.browser.get(access_url)
        self.detail(data_xpath, click_xpath, get_value_type, value_attribute)


if __name__ == '__main__':
    bug = BugThread(None)
