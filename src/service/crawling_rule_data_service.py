from src.dao.crawling_rule_data_dao import CrawlingRuleDataDao
from src.entity.crawling_rule_data import CrawlingRuleData
from src.service.base_service import BaseService


class CrawlingRuleDataService(BaseService):
    def __init__(self):
        self.crawlingRuleDataDao = CrawlingRuleDataDao()

    def load(self, id) -> CrawlingRuleData:
        return self.crawlingRuleDataDao.load(id)

    def load_by_value(self, value) -> CrawlingRuleData:
        return self.crawlingRuleDataDao.load_by_value(value)

    def saveOrModify(self, code, parameter_code, parameter_name, data, pre_id) -> CrawlingRuleData:
        """
        保存更新
        :param crawlingRuleData: 对象
        """
        crawling_rule_data = CrawlingRuleData()
        crawling_rule_data.parameter_code = parameter_code
        crawling_rule_data.parameter_name = parameter_name
        crawling_rule_data.crawling_rule_code = code
        crawling_rule_data.value = data
        if pre_id:
            crawling_rule_data.pre_id = pre_id
        id = self.crawlingRuleDataDao.insert(crawling_rule_data)
        return self.crawlingRuleDataDao.load(id)

    def list(self, crawling_rule_code) -> list:
        return self.crawlingRuleDataDao.list(crawling_rule_code)

    def list_by_parameter_code(self, parameter_code) -> list:
        return self.crawlingRuleDataDao.list_by_parameter_code(parameter_code)
    def list_by_pre_id(self,pre_id)->list:
        return self.crawlingRuleDataDao.list_by_pre_id(pre_id)
    def list_pre_id(self, parameter_code_list) -> list:
        return self.crawlingRuleDataDao.list_pre_id(parameter_code_list)
