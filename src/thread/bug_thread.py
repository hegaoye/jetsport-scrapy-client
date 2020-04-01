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
            logger.info('关闭浏览器-' + self.crawlingRule.code)
            self.browser.quit()
            logger.info('退出浏览器-' + self.crawlingRule.code)
        except Exception as e:
            logger.error(e)

        self.stop()
        logger.info('退出爬虫-' + self.crawlingRule.code)

    def __crawling(self, crawlingRule, pre_id=None, element=None):
        """
        爬取网页数据
        """
        is_parameter = crawlingRule.is_parameter
        xpath = crawlingRule.xpath
        xpath_type = crawlingRule.xpath_type
        # access_url = crawlingRule.access_url
        # 如果有进入入口先打开页面
        # if access_url and str(access_url).startswith('http'):
        #     self.browser.get(access_url)

        crawling_rule_sub_list = self.crawlingRuleService.list_sub(crawlingRule.code)

        # 如果规则爬取的数据是接口的参数的则爬取
        if YNEnum.Y.name.__eq__(is_parameter):
            if XpathTypeEnum.Text.name.__eq__(xpath_type):
                elements = self.element_list(element, xpath)
                if elements and len(elements) > 0:
                    for element in elements:
                        if GetValueTypeEnum.Text.name.__eq__(crawlingRule.get_value_type):
                            # 文本方式获取数据
                            text = element.text
                        elif GetValueTypeEnum.Attribute.name.__eq__(crawlingRule.get_value_type):
                            # 属性方式获取数据
                            text = element.get_attribute(crawlingRule.html_attr)
                        elif GetValueTypeEnum.Download.name.__eq__(crawlingRule.get_value_type):
                            # todo 下载
                            pass

                        # 忽略字符内容判断
                        ignore = crawlingRule.ignore_value
                        if ignore:
                            ignore = str(ignore)
                            ignores = ignore[:-1].split(",") if ignore.endswith(",") else ignore.split(",")
                            if str(text) in ignores:
                                continue

                        # 存储爬取的数据 todo 重复判断可能阻碍其他的数据的进入，需要进一步参数判断
                        crawling_rule_data_load = self.crawlingRuleDataService.load_by_value(text)
                        if crawling_rule_data_load:
                            continue

                        parameter = self.parameterService.load(crawlingRule.parameter_code)
                        crawlingRuleData = self.crawlingRuleDataService.saveOrModify(parameter.code, crawlingRule.code,
                                                                                     parameter.name, text, pre_id)

                        if crawling_rule_sub_list and len(crawling_rule_sub_list) > 0:
                            # 下级数据关联
                            for crawlingRuleSub in crawling_rule_sub_list:
                                # 循环爬取
                                self.__crawling(crawlingRuleSub, crawlingRuleData.code, element)


            elif XpathTypeEnum.Image.name.__eq__(xpath_type):
                pass
            elif XpathTypeEnum.Video.name.__eq__(xpath_type):
                pass
            elif XpathTypeEnum.Audio.name.__eq__(xpath_type):
                pass

        elif YNEnum.N.name.__eq__(is_parameter):
            if XpathTypeEnum.Entrance.name.__eq__(xpath_type):
                # 入口判断
                self.browser.get(crawlingRule.access_url)
                if crawling_rule_sub_list and len(crawling_rule_sub_list) > 0:
                    pre_id = str(uuid.uuid1()).replace("-", "")
                    for crawlingRuleSub in crawling_rule_sub_list:
                        self.__crawling(crawlingRuleSub, pre_id, element)

            elif XpathTypeEnum.Element.name.__eq__(xpath_type):
                # 判断元素
                sub_elements = self.element_list(element, xpath)
                if sub_elements and len(sub_elements) > 0:
                    for sub_element in sub_elements:
                        for crawlingRuleSub in crawling_rule_sub_list:
                            self.__crawling(crawlingRuleSub, pre_id, sub_element)


            elif XpathTypeEnum.Click.name.__eq__(xpath_type):
                # 点击事件判断
                click_elements = self.element_list(element, xpath)
                if click_elements:
                    for click_element in click_elements:
                        click_element.click()
                        sleep(crawlingRule.frequce)
                        if crawling_rule_sub_list and len(crawling_rule_sub_list) > 0:
                            for crawlingRuleSub in crawling_rule_sub_list:
                                self.__crawling(crawlingRuleSub, pre_id, click_element)


            elif XpathTypeEnum.Link.name.__eq__(xpath_type):
                # 爬取并存储链接路径
                link_list = self.element_list(element, xpath)
                if link_list and len(link_list) > 0:
                    links = []
                    for link in link_list:
                        if GetValueTypeEnum.Attribute.name.__eq__(crawlingRule.get_value_type):
                            link_data = link.get_attribute(crawlingRule.html_attr)
                            id = self.crawlingDataLinkService.save(pre_id, link_data)
                            if link_data:
                                links.append(link_data)

                    if crawling_rule_sub_list and len(crawling_rule_sub_list) > 0:
                        for url in links:
                            crawlingRuleSub = CrawlingRule()
                            crawlingRuleSub.xpath_type = XpathTypeEnum.Entrance.name
                            crawlingRuleSub.access_url = url
                            crawlingRuleSub.is_parameter = YNEnum.N.name
                            crawlingRuleSub.code = crawlingRule.code
                            bug = BugThread(crawlingRuleSub, pre_id)
                            bug.start()
                            sleep(crawlingRule.frequce)

    def element_list(self, element, xpath) -> list:
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
    cr = c.load_by_code(38)
    bug = BugThread(cr)
    bug.start()
