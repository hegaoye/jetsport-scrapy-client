# coding=utf-8
import threading

from src.base.browser import Browser
from src.base.enum.get_value_type_enum import GetValueTypeEnum
from src.base.enum.xpath_type_enum import XpathTypeEnum
from src.base.enum.y_n_enum import YNEnum
from src.entity.crawling_rule_data import CrawlingRuleData
from src.entity.crawling_rule_data_link import CrawlingRuleDataLink
from src.service.crawling_data_link_service import CrawlingRuleDataLinkService
from src.service.crawling_rule_data_service import CrawlingRuleDataService
from src.service.crawling_rule_service import CrawlingRuleService
from src.thread.base_thread import BaseTread


class BugThread(BaseTread):
    """
    虫子，用于爬取数据的爬虫，多线程实现可以多线程并行多个规则，
    """

    def __init__(self, crawlingRule=None):
        threading.Thread.__init__(self)
        self.browser = Browser().get_brower()
        self.crawlingRule = crawlingRule
        self.crawlingRuleService = CrawlingRuleService()
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

    def __crawling(self, crawlingRule):
        """
        爬取网页数据
        """
        is_parameter = self.crawlingRule.is_parameter
        xpath = crawlingRule.xpath
        xpath_type = crawlingRule.xpath_type
        access_url = crawlingRule.access_url
        # 如果有进入入口先打开页面
        if access_url and str(access_url).startswith('http'):
            self.browser.get(access_url)

        # 如果规则爬取的数据是接口的参数的则爬取
        if YNEnum.Y.name.__eq__(is_parameter):
            if XpathTypeEnum.Text.name.__eq__(xpath_type):
                self.__find_elements_by_xpath(crawlingRule)


            elif XpathTypeEnum.Image.name.__eq__(xpath_type):
                pass
            elif XpathTypeEnum.Video.name.__eq__(xpath_type):
                pass
            elif XpathTypeEnum.Audio.name.__eq__(xpath_type):
                pass

        elif YNEnum.N.name.__eq__(is_parameter):
            crawling_rule_sub_list = self.crawlingRuleService.list_sub(crawlingRule.code)

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
                            self.browser.get(link)
                            for crawling_rule_sub in crawling_rule_sub_list:
                                self.__crawling(crawling_rule_sub)

                            # 返回上一页
                            self.browser.back()

    def __find_elements_by_xpath(self, crawlingRule, pre_id=None, element=None):
        xpath = crawlingRule.xpath
        crawling_rule_sub_list = self.crawlingRuleService.list_sub(crawlingRule.code)
        if not element:
            elements = self.browser.find_elements_by_xpath(xpath)
        else:
            elements = element.find_elements_by_xpath(xpath)

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
                id = self.__save_crawling_rule_data(crawlingRule.parameter_code, crawlingRule.code, data, pre_id)

                if crawling_rule_sub_list and crawling_rule_sub_list.__sizeof__() > 0:
                    # 下级数据关联
                    for crawlingRuleSub in crawling_rule_sub_list:
                        # 循环爬取
                        self.__find_elements_by_xpath(crawlingRuleSub, id, element)

    def __save_crawling_rule_data(self, parameter_code, code, data, pre_id) -> int:
        # 存储爬取的数据
        crawling_rule_data = CrawlingRuleData()
        crawling_rule_data.parameter_code = parameter_code
        crawling_rule_data.crawling_rule_code = code
        crawling_rule_data.value = data
        if pre_id:
            crawling_rule_data.pre_id = pre_id
        id = self.crawlingRuleDataService.saveOrModify(crawling_rule_data)
        return id

    def test(self):
        self.browser.get('https://777score.ph/')
        list = self.browser.find_elements_by_xpath('//*[@id="categories"]/li')
        for i in list:
            print("------" + i.text)
            uls = i.find_elements_by_xpath('ul/li/a')
            for u in uls:
                print(u.get_attribute('title'))

            a = i.find_element_by_xpath('a')
            print(a.get_attribute('title'))


if __name__ == '__main__':
    c = CrawlingRuleService()
    cr = c.load_by_code(1)
    bug = BugThread(cr)
    bug.start()
    # bug.test()
