from src.base.singleton import Singleton
from src.entity.crawling_rule_data import CrawlingRuleData


class CrawlingRuleDataDao(Singleton):
    def insert(self, crawlingRuleData) -> None:
        CrawlingRuleData.create(crawling_rule_code=crawlingRuleData.crawling_rule_code,
                                parameter_code=crawlingRuleData.parameter_code, value=crawlingRuleData.value,
                                pre_id=crawlingRuleData.pre_id, parameter_name=crawlingRuleData.parameter_name)
