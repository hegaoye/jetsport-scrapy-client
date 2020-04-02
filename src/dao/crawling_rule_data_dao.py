# coding=utf-8
import uuid

from src.base.singleton import Singleton
from src.entity.crawling_rule_data import CrawlingRuleData


class CrawlingRuleDataDao(Singleton):
    """
    api parameter dao
    """

    def load(self, id) -> CrawlingRuleData:
        return CrawlingRuleData.get(CrawlingRuleData.id == id)

    def load_by_crawling_rule_code(self, crawling_rule_code) -> CrawlingRuleData:
        return CrawlingRuleData.get(CrawlingRuleData.crawling_rule_code == crawling_rule_code)

    def load_by_pre_id_and_crawling_rule_code(self, pre_id, crawling_rule_code) -> CrawlingRuleData:
        return CrawlingRuleData.get(CrawlingRuleData.pre_id == pre_id,
                                    CrawlingRuleData.crawling_rule_code == crawling_rule_code)

    def update(self, crawling_rule_code, value) -> int:
        return CrawlingRuleData.update(value=value).where(CrawlingRuleData.crawling_rule_code == crawling_rule_code)

    def insert(self, crawlingRuleData) -> int:
        return CrawlingRuleData.insert(code=str(uuid.uuid1()).replace("-", ""), pre_id=crawlingRuleData.pre_id,
                                       crawling_rule_code=crawlingRuleData.crawling_rule_code,
                                       value=crawlingRuleData.value, parameter_name=crawlingRuleData.parameter_name,
                                       parameter_code=crawlingRuleData.parameter_code).execute()

    def list(self, crawling_rule_code) -> list:
        return CrawlingRuleData.select().where(CrawlingRuleData.crawling_rule_code == crawling_rule_code)

    def load_by_value(self, value) -> CrawlingRuleData:
        list = CrawlingRuleData.select().where(CrawlingRuleData.value == value)
        if list and len(list) > 0:
            return list.get()
        return None

    def list_by_parameter_code(self, parameter_code) -> list:
        return CrawlingRuleData.select().where(CrawlingRuleData.parameter_code == parameter_code)

    def list_pre_id(self, parameter_code_list) -> list:
        return CrawlingRuleData.select(CrawlingRuleData.pre_id).where(
            CrawlingRuleData.parameter_code in parameter_code_list)

    def list_by_pre_id(self, pre_id) -> list:
        return CrawlingRuleData.select().where(CrawlingRuleData.pre_id == pre_id)

    def delete_list(self, ids):
        if ids and len(ids) > 0:
            for id in ids:
                CrawlingRuleData.delete_by_id(id)
