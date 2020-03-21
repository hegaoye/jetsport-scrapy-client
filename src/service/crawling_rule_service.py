from src.dao.crawling_rule_dao import CrawlingRuleDao
from src.entity.crawling_rule import CrawlingRule
from src.service.base_service import BaseService


class CrawlingRuleService(BaseService):
    """
    爬虫规则接口类
    """

    def __init__(self):
        self.crawlingRuleDao = CrawlingRuleDao()

    def load_by_code(self, code) -> CrawlingRule:
        """
        加载一条爬虫规则
        :param code: 编码
        :return: CrawlingRule
        """
        return self.crawlingRuleDao.load_by_code(code)

    def list_sub(self, pre_code) -> list:
        """
        查询爬虫规则列表
        :param pre_code: 上级编码
        :return: list
        """
        return self.crawlingRuleDao.list_sub(pre_code)
