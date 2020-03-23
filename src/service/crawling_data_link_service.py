from src.dao.crawling_rule_data_link_dao import CrawlingRuleDataLinkDao
from src.service.base_service import BaseService


class CrawlingRuleDataLinkService(BaseService):
    def __init__(self):
        self.crawlingRuleDataLinkDao = CrawlingRuleDataLinkDao()

    def save(self, crawlingRuleDataLinkDao) -> None:
        self.crawlingRuleDataLinkDao.insert(crawlingRuleDataLinkDao)
