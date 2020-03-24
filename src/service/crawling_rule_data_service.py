from src.dao.crawling_rule_data_dao import CrawlingRuleDataDao
from src.entity.crawling_rule_data import CrawlingRuleData
from src.service.base_service import BaseService


class CrawlingRuleDataService(BaseService):
    def __init__(self):
        self.crawlingRuleDataDao = CrawlingRuleDataDao()

    def load(self, id) -> CrawlingRuleData:
        return self.crawlingRuleDataDao.load(id)

    def saveOrModify(self, crawlingRuleData) -> int:
        """
        保存更新
        :param crawlingRuleData: 对象
        """
        crawling_rule_code = crawlingRuleData.crawling_rule_code
        # crawling_rule_data = self.crawlingRuleDataDao.load_by_crawling_rule_code(crawling_rule_code)
        # if not crawling_rule_data:
        id = self.crawlingRuleDataDao.insert(crawlingRuleData)

        # else:
        #     self.crawlingRuleDataDao.update(crawling_rule_code, crawlingRuleData.value)
        #     id = crawling_rule_data.id

        return id


def list(self, crawling_rule_code) -> list:
    return self.crawlingRuleDataDao.list(crawling_rule_code)
