# coding=utf-8
import json

from src.base.browser import Browser
from src.thread.base_thread import BaseTread


class BugThread(BaseTread):
    """
    虫子，用于爬取数据的爬虫，多线程实现可以多线程并行多个规则，
    """

    def __init__(self, crawlingRule=None):
        self.browser = Browser().get_brower()
        self.crawlingRule = crawlingRule

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
        access_url = "https://777score.ph/"
        self.browser.get(access_url)
        country_xpath = '//*[@id="categories"]/li'
        league_xpath = 'ul[@class="tournaments"]/li/a'
        nations_element = self.browser.find_elements_by_xpath(country_xpath)
        # nations_element = WebDriverWait(self.browser, 3).until(
        #     EC.presence_of_all_elements_located((By.XPATH, contry_xpath)))
        nations = []
        for nation_element in nations_element:
            nation = nation_element.text
            leagues = nation_element.find_elements_by_xpath(league_xpath)
            leagues_text = []
            for league in leagues:
                a_href = league.get_attribute('href')
                a_title = league.get_attribute('title')
                a = {
                    "href": a_href,
                    "league": a_title
                }
                leagues_text.append(a)

            data = {
                str(nation): leagues_text
            }
            nations.append(data)

        print(json.dumps(nations))


if __name__ == '__main__':
    bug = BugThread(None)
    bug.run()
