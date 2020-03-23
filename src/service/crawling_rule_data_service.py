from src.dao.crawling_rule_data_dao import CrawlingRuleDataDao
from src.entity.crawling_rule_data import CrawlingRuleData
from src.service.base_service import BaseService


class CrawlingRuleDataService(BaseService):
    def __init__(self):
        self.crawlingRuleDataDao = CrawlingRuleDataDao()

    def load(self, code) -> CrawlingRuleData:
        return self.crawlingRuleDataDao.load(code)

    def saveOrModify(self, crawlingRuleData):
        """
        保存更新
        :param crawlingRuleData: 对象
        """
        crawling_rule_code = crawlingRuleData.crawling_rule_code
        crawling_rule_data = self.crawlingRuleDataDao.load_by_crawling_rule_code(crawling_rule_code)
        if not crawling_rule_data:
            self.crawlingRuleDataDao.insert(crawlingRuleData)
        else:
            self.crawlingRuleDataDao.update(crawling_rule_code, crawlingRuleData.value)
