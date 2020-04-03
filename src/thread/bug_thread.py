# coding=utf-8
import threading
import uuid
from time import sleep

from src.base.browser import Browser
from src.base.enum.get_value_type_enum import GetValueTypeEnum
from src.base.enum.xpath_type_enum import XpathTypeEnum
from src.base.enum.y_n_enum import YNEnum
from src.base.log4py import logger
from src.entity.crawling_rule import CrawlingRule
from src.service.crawling_data_link_service import CrawlingRuleDataLinkService
from src.service.crawling_rule_data_service import CrawlingRuleDataService
from src.service.crawling_rule_service import CrawlingRuleService
from src.service.parameter_serivce import ParameterService
from src.thread.base_thread import BaseTread


class BugThread(BaseTread):
    """
    虫子，用于爬取数据的爬虫，多线程实现可以多线程并行多个规则，
    """

    def __init__(self, crawlingRule=None, pre_id=None):
        threading.Thread.__init__(self)
        self.browser = Browser().get_brower()
        self.crawlingRule = crawlingRule
        self.crawlingRuleService = CrawlingRuleService()
        self.crawlingRuleDataService = CrawlingRuleDataService()
        self.crawlingDataLinkService = CrawlingRuleDataLinkService()
        self.parameterService = ParameterService()
        self.pre_id = pre_id

    def run(self):
        """
        启动线程
        """
        try:
            # 爬取网页数据
            self.__crawling(self.crawlingRule, self.pre_id)
            # 拼装数据 使用多线程进行

        except Exception as e:
            # todo 增加异常判断，规则判断
            logger.error(e)

        try:
            self.browser.close()
            logger.info('关闭浏览器-' + str(self.crawlingRule.code))
            self.browser.quit()
            logger.info('退出浏览器-' + str(self.crawlingRule.code))
        except Exception as e:
            logger.error(e)

        self.stop()
        logger.info('退出爬虫-' + str(self.crawlingRule.code))

    def __crawling(self, crawlingRule, pre_id=None, element=None):
        """
        爬取网页数据
        """
        xpath = crawlingRule.xpath
        xpath_type = crawlingRule.xpath_type
        html_attr = crawlingRule.html_attr
        crawling_rule_code = crawlingRule.code
        frequce = crawlingRule.frequce
        crawling_rule_sub_list = self.crawlingRuleService.list_sub(crawlingRule.code)

        if XpathTypeEnum.Entrance.name.__eq__(xpath_type):
            self.__entrance(crawlingRule.access_url, crawling_rule_sub_list)
        elif XpathTypeEnum.Element.name.__eq__(xpath_type):
            self.__element(xpath, crawling_rule_sub_list, pre_id, element)
        elif XpathTypeEnum.Click.name.__eq__(xpath_type):
            self.__click(xpath, frequce, crawling_rule_sub_list, pre_id, element)
        elif XpathTypeEnum.Link.name.__eq__(xpath_type):
            self.__link(xpath, frequce, crawling_rule_sub_list, html_attr,
                        crawling_rule_code, pre_id, element)
        elif XpathTypeEnum.Text.name.__eq__(xpath_type):
            self.__text(crawling_rule_code, crawlingRule.parameter_code, xpath, crawlingRule.ignore_value,
                        html_attr, crawlingRule.get_value_type, crawling_rule_sub_list, pre_id, element)
        elif XpathTypeEnum.Image.name.__eq__(xpath_type):
            pass
        elif XpathTypeEnum.Video.name.__eq__(xpath_type):
            pass
        elif XpathTypeEnum.Audio.name.__eq__(xpath_type):
            pass

    def __entrance(self, access_url, crawling_rule_list):
        """
        打开入口
        :param access_url: 入口地址
        :param crawling_rule_list: 第一级 规则集合
        """
        if access_url and crawling_rule_list and len(crawling_rule_list) > 0:
            # 打开连接
            self.browser.get(access_url)
            # 循环下级规则
            if crawling_rule_list and len(crawling_rule_list) > 0:
                for crawlingRuleSub in crawling_rule_list:
                    pre_id = str(uuid.uuid1()).replace("-", "")
                    self.__crawling(crawlingRuleSub, pre_id)

    def __element(self, xpath, crawling_rule_list, pre_id, element):
        """
        页面html标签元素进行迭代
        :param xpath: xpath
        :param crawling_rule_list: 子集规则
        :param pre_id: 上级id
        :param element: html标签元素
        """
        elements = self.__element_list(element, xpath)
        if elements and len(elements) > 0:
            for sub_element in elements:
                pre_id = str(uuid.uuid1()).replace("-", "")
                self.__crawling_rule_list(crawling_rule_list, pre_id, sub_element)

    def __click(self, xpath, frequce, crawling_rule_list, pre_id, element):
        """
        点击类型进行点击操作
        :param xpath: xpath 点击位置
        :param frequce: 点击后停留时间
        :param crawling_rule_list: 下级规则集合
        :param pre_id: 上级id
        :param element: 元素
        """
        elements = self.__element_list(element, xpath)
        if elements:
            for click_element in elements:
                click_element.click()
                sleep(frequce)
                self.__crawling_rule_list(crawling_rule_list, pre_id, click_element)

    def __link(self, xpath, frequce, crawling_rule_list, html_attr, crawling_rule_code, pre_id, element):
        """
        链接处理
        :param xpath:
        :param frequce:
        :param crawling_rule_list:
        :param html_attr:
        :param crawling_rule_code:
        :param pre_id:
        :param element:
        :return:
        """
        elements = self.__element_list(element, xpath)
        if elements and len(elements) > 0:
            links = []
            # todo 保存链接的必要性在哪里？
            for link in elements:
                link_data = link.get_attribute(html_attr)
                id = self.crawlingDataLinkService.save(pre_id, link_data)
                if link_data:
                    links.append(link_data)

            if crawling_rule_list and len(crawling_rule_list) > 0:
                for url in links:
                    crawlingRuleSub = CrawlingRule()
                    crawlingRuleSub.xpath_type = XpathTypeEnum.Entrance.name
                    crawlingRuleSub.access_url = url
                    crawlingRuleSub.is_parameter = YNEnum.N.name
                    crawlingRuleSub.code = crawling_rule_code
                    bug = BugThread(crawlingRuleSub, pre_id)
                    bug.start()
                    sleep(frequce)

    def __text(self, crawling_rule_code, parameter_code, xpath, ignore_value,
               html_attr, value_type, crawling_rule_list, pre_id, element):
        """
        爬取文本内容
        :param crawling_rule_code: 规则编码
        :param parameter_code: 参数编码
        :param xpath: 爬取文本的xpath
        :param ignore_value: 忽略的值
        :param html_attr: 获取text html的具体属性
        :param value_type: 取值类型
        :param crawling_rule_list: 子规则集合
        :param pre_id: 上级id
        :param element: html 标签元素
        """
        elements = self.__element_list(element, xpath)
        if elements and len(elements) > 0:
            for element in elements:
                if GetValueTypeEnum.Text.name.__eq__(value_type):
                    text = element.text
                elif GetValueTypeEnum.Attribute.name.__eq__(value_type):
                    text = element.get_attribute(html_attr)
                elif GetValueTypeEnum.Download.name.__eq__(value_type):
                    pass

                # 忽略字符内容判断
                if self.__is_ignore(ignore_value, text):
                    continue

                # 存储爬取的数据 todo 重复判断可能阻碍其他的数据的进入，需要进一步参数判断
                crawling_rule_data_load = self.crawlingRuleDataService.load_by_value(text)
                if not crawling_rule_data_load:
                    parameter = self.parameterService.load(parameter_code)
                    crawlingRuleData = self.crawlingRuleDataService.saveOrModify(crawling_rule_code, pre_id, text,
                                                                                 parameter)

                sub_code = crawling_rule_data_load.code if crawling_rule_data_load else crawlingRuleData.code
                self.__crawling_rule_list(crawling_rule_list, sub_code, element)

    def __crawling_rule_list(self, crawling_rule_list, pre_id=None, element=None):
        if crawling_rule_list and len(crawling_rule_list) > 0:
            for crawlingRuleSub in crawling_rule_list:
                self.__crawling(crawlingRuleSub, pre_id, element)

    def __is_ignore(self, ignore_value, text) -> bool:
        """
        判断是否需要忽略值
        :param ignore_value: 需要忽略的值，逗号分隔
        :param text: 需要被忽略的文本
        :return: True/False
        """
        if ignore_value:
            ignore_value = str(ignore_value)
            ignores = ignore_value[:-1].split(",") if ignore_value.endswith(",") else ignore_value.split(",")
            if str(text) in ignores:
                return True

        return False

    def __element_list(self, element, xpath) -> list:
        """
        获取元素集合
        :param element: 元素
        :param xpath: xpath
        :return: list
        """
        if not element:
            # 浏览器 定位 元素
            elements = self.browser.find_elements_by_xpath(xpath)
        else:
            # 相对路径查找 xpath
            elements = element.find_elements_by_xpath(xpath)

        return elements


if __name__ == '__main__':
    c = CrawlingRuleService()
    cr = c.load_by_code(19)
    bug = BugThread(cr)
    bug.start()
