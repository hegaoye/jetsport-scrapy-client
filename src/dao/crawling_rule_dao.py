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
        CrawlingRule.create(code=crawlingRule.code, api_code=crawlingRule.api_code,
                            get_value_method=crawlingRule.get_value_method, api_field=crawlingRule.api_field,
                            field_type=crawlingRule.field_type, value_type=crawlingRule.value_type,
                            result_type=crawlingRule.result_type, frequce=crawlingRule.frequce,
                            xpath=crawlingRule.xpath, sub_xpath=crawlingRule.sub_xpath,
                            sub_xpath_relative=crawlingRule.sub_xpath_relative, sub_label=crawlingRule.sub_label,
                            sub_label_class=crawlingRule.sub_label_class, opt=crawlingRule.opt,
                            access_url=crawlingRule.access_url, target_code=crawlingRule.target_code,
                            pre_code=crawlingRule.pre_code, api_url=crawlingRule.api_url)

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
