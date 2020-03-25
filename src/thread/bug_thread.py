# coding=utf-8
import threading
from time import sleep

from src.base.browser import Browser
from src.base.enum.get_value_type_enum import GetValueTypeEnum
from src.base.enum.xpath_type_enum import XpathTypeEnum
from src.base.enum.y_n_enum import YNEnum
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

    def __crawling(self, crawlingRule, pre_id=None, element=None):
        """
        爬取网页数据
        """
        is_parameter = crawlingRule.is_parameter
        xpath = crawlingRule.xpath
        xpath_type = crawlingRule.xpath_type
        access_url = crawlingRule.access_url
        # 如果有进入入口先打开页面
        # if access_url and str(access_url).startswith('http'):
        #     self.browser.get(access_url)

        crawling_rule_sub_list = self.crawlingRuleService.list_sub(crawlingRule.code)
        if crawling_rule_sub_list:
            for c in crawling_rule_sub_list:
                print(c.code, ' ', c.xpath)

        # 如果规则爬取的数据是接口的参数的则爬取
        if YNEnum.Y.name.__eq__(is_parameter):
            if XpathTypeEnum.Text.name.__eq__(xpath_type):
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
                        id = self.crawlingRuleDataService.saveOrModify(crawlingRule.parameter_code, crawlingRule.code,
                                                                       data, pre_id)

                        if crawling_rule_sub_list and crawling_rule_sub_list.__sizeof__() > 0:
                            # 下级数据关联
                            for crawlingRuleSub in crawling_rule_sub_list:
                                # 循环爬取
                                self.__crawling(crawlingRuleSub, id, element)


            elif XpathTypeEnum.Image.name.__eq__(xpath_type):
                pass
            elif XpathTypeEnum.Video.name.__eq__(xpath_type):
                pass
            elif XpathTypeEnum.Audio.name.__eq__(xpath_type):
                pass

        elif YNEnum.N.name.__eq__(is_parameter):
            if XpathTypeEnum.Entrance.name.__eq__(xpath_type):
                self.browser.get(crawlingRule.access_url)
                if crawling_rule_sub_list and crawling_rule_sub_list.__sizeof__() > 0:
                    for crawlingRuleSub in crawling_rule_sub_list:
                        self.__crawling(crawlingRuleSub)

            elif XpathTypeEnum.Click.name.__eq__(xpath_type):
                # 如果爬取规则爬取的数据不是接口数据则进行判断是否需要点击或者另外打开网页等
                if not element:
                    click_elements = self.browser.find_elements_by_xpath(xpath)
                else:
                    click_elements = element.find_elements_by_xpath(xpath)

                if click_elements:
                    for click_element in click_elements:
                        click_element.click()
                        sleep(crawlingRule.frequce)
                        if crawling_rule_sub_list and crawling_rule_sub_list.__sizeof__() > 0:
                            for crawlingRuleSub in crawling_rule_sub_list:
                                self.__crawling(crawlingRuleSub, pre_id, click_element)


            elif XpathTypeEnum.Link.name.__eq__(xpath_type):
                # 爬取并存储链接路径
                if not element:
                    link_list = self.browser.find_elements_by_xpath(xpath)
                else:
                    link_list = element.find_elements_by_xpath(xpath)

                if link_list and link_list.__sizeof__() > 0:
                    links = []
                    for link in link_list:
                        if GetValueTypeEnum.Attribute.name.__eq__(crawlingRule.get_value_type):
                            link_data = link.get_attribute(crawlingRule.html_attr)
                        id = self.crawlingDataLinkService.save(pre_id, link_data)
                        if link_data:
                            links.append(link_data)

                    if crawling_rule_sub_list and crawling_rule_sub_list.__sizeof__() > 0:
                        for l in links:
                            for crawlingRuleSub in crawling_rule_sub_list:
                                crawlingRuleSub.access_url = l
                                bug = BugThread(crawlingRuleSub)
                                bug.start()
                                # self.__crawling(crawling_rule_sub, pre_id)

    def test(self):
        self.browser.get('https://777score.ph/')
        list = self.browser.find_elements_by_xpath('//*[@id="categories"]/li[48]')
        for i in list:
            print("------" + i.text)
            uls = i.find_elements_by_xpath('ul/li/a')
            for u in uls:
                print(u.get_attribute('title'))
                url = u.get_attribute('href')
                self.browser.get(url)
                teams = self.browser.find_elements_by_xpath(
                    '//*[@id="dataContainer"]/div[1]/span/table/tbody/tr/td[2]/a')
                for team in teams:
                    print(team.text)

                sleep(3)
                self.browser.back()
                sleep(3)


if __name__ == '__main__':
    c = CrawlingRuleService()
    cr = c.load_by_code(1)
    bug = BugThread(cr)
    bug.start()
    # bug.test()
