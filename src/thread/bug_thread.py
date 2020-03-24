# coding=utf-8

from src.base.browser import Browser
from src.base.enum.get_value_type_enum import GetValueTypeEnum
from src.base.enum.xpath_type_enum import XpathTypeEnum
from src.base.enum.y_n_enum import YNEnum
from src.entity.crawling_rule_data import CrawlingRuleData
from src.entity.crawling_rule_data_link import CrawlingRuleDataLink
from src.service.crawling_data_link_service import CrawlingRuleDataLinkService
from src.service.crawling_data_service import CrawlingDataService
from src.service.crawling_rule_data_service import CrawlingRuleDataService
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
        self.crawlingRuleDataService = CrawlingRuleDataService()
        self.crawlingDataLinkService = CrawlingRuleDataLinkService()

    def run(self):
        """
        启动线程
        """
        try:
            # 爬取网页数据
            self.__crawling(self.crawlingRule)

            # 拼装数据 使用多线程进行

        except:
            # todo 增加异常判断，规则判断
            self.stop()

    def __crawling(self, crawlingRule, pre_id=None):
        """
        爬取网页数据
        """
        is_parameter = self.crawlingRule.is_parameter
        xpath = crawlingRule.xpath
        xpath_type = crawlingRule.xpath_type
        access_url = crawlingRule.access_url
        # 如果有进入入口先打开页面
        if access_url:
            self.browser.get(access_url)

        crawling_rule_sub_list = self.crawlingRuleService.list_sub(crawlingRule.code)

        # 如果规则爬取的数据是接口的参数的则爬取
        if YNEnum.Y.name.__eq__(is_parameter):
            if XpathTypeEnum.Text.name.__eq__(xpath_type):
                elements = self.browser.find_elements_by_xpath(xpath)
                if elements and elements.__sizeof__() > 0:
                    for element in elements:
                        if GetValueTypeEnum.Text.name.__eq__(crawlingRule.get_value_type):
                            # 文本方式获取数据
                            data = element.text
                        elif GetValueTypeEnum.Attribute.name.__eq__(crawlingRule.get_value_type):
                            # 属性方式获取数据
                            data = element.get_attribute(crawlingRule.html_attr)
                        elif GetValueTypeEnum.Download.name.__eq__(crawlingRule.get_value_type):
                            # todo 下载
                            pass

                        # 存储爬取的数据
                        crawling_rule_data = CrawlingRuleData()
                        crawling_rule_data.parameter_code = crawlingRule.parameter_code
                        crawling_rule_data.crawling_rule_code = crawlingRule.code
                        crawling_rule_data.value = data
                        if pre_id:
                            crawling_rule_data.pre_id = pre_id
                        self.crawlingDataService.saveOrModify(crawling_rule_data)

                        if crawling_rule_sub_list and crawling_rule_sub_list.__sizeof__() > 0:
                            # 下级数据关联
                            for crawling_rule_sub in crawling_rule_sub_list:
                                self.__crawling(crawling_rule_sub, crawling_rule_data.id)


            elif XpathTypeEnum.Image.name.__eq__(xpath_type):
                pass
            elif XpathTypeEnum.Video.name.__eq__(xpath_type):
                pass
            elif XpathTypeEnum.Audio.name.__eq__(xpath_type):
                pass

        elif YNEnum.N.name.__eq__(is_parameter):
            # 如果爬取规则爬取的数据不是接口数据则进行判断是否需要点击或者另外打开网页等
            if XpathTypeEnum.Click.name.__eq__(xpath_type):
                self.browser.find_element_by_xpath(xpath).click()
                if crawling_rule_sub_list and crawling_rule_sub_list.__sizeof__() > 0:
                    for crawling_rule_sub in crawling_rule_sub_list:
                        self.__crawling(crawling_rule_sub)

            elif XpathTypeEnum.Link.name.__eq__(xpath_type):
                # 爬取并存储链接路径
                link_list = self.browser.find_elements_by_xpath(xpath)
                if link_list and link_list.__sizeof__() > 0:
                    for link in link_list:
                        crawlingRuleDataLink = CrawlingRuleDataLink()
                        crawlingRuleDataLink.crawling_rule_code = crawlingRule.code
                        crawlingRuleDataLink.link = link
                        self.crawlingDataLinkService.save(crawlingRuleDataLink)

                    if crawling_rule_sub_list and crawling_rule_sub_list.__sizeof__() > 0:
                        for crawling_rule_sub in crawling_rule_sub_list:
                            self.__crawling(crawling_rule_sub)

    def test(self):
        self.browser.get('https://777score.ph/')
        xpath = '/html/body/div[3]/aside/div[2]/ul/li/a'
        list = self.browser.find_elements_by_xpath(xpath)
        for e in list:
            print(e.location)
            print(e.text)


if __name__ == '__main__':
    bug = BugThread(None)
    bug.test()
