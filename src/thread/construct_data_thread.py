# coding=utf-8
from src.base.enum.parameter_type_enum import ParameterTypeEnum
from src.service.api_serivce import ApiService
from src.service.crawling_rule_data_service import CrawlingRuleDataService
from src.service.crawling_rule_service import CrawlingRuleService
from src.service.parameter_serivce import ParameterService
from src.thread.base_thread import BaseTread


class ConstructDataThread(BaseTread):
    """
    拉取命令多线程，保持单例模式，禁止多线程跑多个实例导致指令执行的混乱
    """

    def __init__(self, crawlingRule):
        self.crawlingRule = crawlingRule
        self.apiService = ApiService()
        self.crawlingRuleService = CrawlingRuleService()
        self.crawlingRuleDataService = CrawlingRuleDataService()
        self.parameterService = ParameterService()

    def run(self) -> None:
        pass

    def build_data(self):
        """
        构造接口数据
        1.查询参数数据
        2.查询规则参数值
        3.构造结构
        """
        crawling_rule_data_list = self.crawlingRuleDataService.list(self.crawlingRule.code)
        if crawling_rule_data_list and crawling_rule_data_list.__sizeof__() > 0:
            for crawlingRuleData in crawling_rule_data_list:
                parameter = self.parameterService.load(crawlingRuleData.parameter_code)
                name = parameter.name
                value = crawlingRuleData.value

                if ParameterTypeEnum.Map.name.__eq__(parameter.parameter_type):
                    data = {}
                    data[name] = value
                elif ParameterTypeEnum.List.name.__eq__(parameter.parameter_type):
                    pass
                elif ParameterTypeEnum.Uri.name.__eq__(parameter.parameter_type):
                    pass


if __name__ == '__main__':
    data = {}
    name = "a"
    value = "b"
    data[name] = value
    print(data)
