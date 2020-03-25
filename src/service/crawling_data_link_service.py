from src.dao.crawling_rule_data_link_dao import CrawlingRuleDataLinkDao
from src.entity.crawling_rule_data_link import CrawlingRuleDataLink
from src.service.base_service import BaseService


class CrawlingRuleDataLinkService(BaseService):
    def __init__(self):
        self.crawlingRuleDataLinkDao = CrawlingRuleDataLinkDao()

    def save(self, code, link_data) -> int:
        crawlingRuleDataLink = CrawlingRuleDataLink()
        crawlingRuleDataLink.crawling_rule_code = code
        crawlingRuleDataLink.link = link_data
        return self.crawlingRuleDataLinkDao.insert(crawlingRuleDataLink)
