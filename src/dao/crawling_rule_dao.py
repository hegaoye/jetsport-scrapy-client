# coding=utf-8

from src.base.singleton import Singleton
from src.entity.crawling_rule import CrawlingRule


class CrawlingRuleDao(Singleton):
    """
    爬取规则Dao
    """

    def insert(self, crawlingRule) -> None:
        """
        插入一条爬虫规则
        :param crawlingRule: 爬取规则
        """
        CrawlingRule.create(code=crawlingRule.code, pre_code=crawlingRule.pre_code,
                            api_code=crawlingRule.api_code, parameter_code=crawlingRule.parameter_code,
                            xpath=crawlingRule.xpath, xpath_type=crawlingRule.xpath_type,
                            get_value_type=crawlingRule.get_value_type, html_attr=crawlingRule.html_attr,
                            access_url=crawlingRule.access_url, frequce=crawlingRule.frequce,
                            is_parameter=crawlingRule.is_parameter, ordinal=crawlingRule.ordinal)

    def insert_batch(self, list):
        """
        批量插入 爬取规则
        :param list: 规则集合
        """
        for crawlingRule in list:
            self.insert(crawlingRule)

    def load_by_code(self, code) -> CrawlingRule:
        """
        加载一条爬虫规则
        :param code: 编码
        :return: CrawlingRule
        """
        return CrawlingRule.get(CrawlingRule.code == code)

    def list_sub(self, pre_code) -> list:
        """
        查询爬虫规则列表
        :param pre_code: 上级编码
        :return: list
        """
        return CrawlingRule.select().where(CrawlingRule.pre_code == pre_code).order_by(CrawlingRule.ordinal.asc())


if __name__ == '__main__':
    crawlingRule = CrawlingRuleDao().load_by_code(1)
    ignore = crawlingRule.ignore_value
    i = ignore.split(",") if not str(ignore).endswith(",") else ignore[:-1].split(",")
    print(i)
    print('all' in i)
