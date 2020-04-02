# coding=utf-8
from src.base.enum.y_n_enum import YNEnum
from src.service.api_serivce import ApiService
from src.service.crawling_rule_data_service import CrawlingRuleDataService
from src.service.crawling_rule_service import CrawlingRuleService
from src.service.parameter_serivce import ParameterService
from src.thread.base_thread import BaseTread


class ConstructDataThread(BaseTread):
    """
    构造用于推送的数据，保持单例模式，禁止多线程跑多个实例导致指令执行的混乱
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
        1.查询接口列表
        2.查询参数列表
        3.查询参数数据
        4.构造结构
        """
        # 1.查询接口列表
        api_list = self.apiService.list()

        # 2.查询参数列表
        if api_list and len(api_list) > 0:
            for api in api_list:
                api_parameter_list = []
                parameter_code_list = self.parameterService.list_code(api.code, YNEnum.Y.name)
                pre_id_list = self.crawlingRuleDataService.list_pre_id(parameter_code_list)
                if pre_id_list and len(pre_id_list) > 0:
                    for pre_id in pre_id_list:
                        # 3.查询参数数据
                        crawling_rule_data_list = self.crawlingRuleDataService.list_by_pre_id(pre_id)
                        # 4.构造结构
                        parameter_data = {}
                        for crawlingRuleData in crawling_rule_data_list:
                            parameter_data[crawlingRuleData.parameter_name] = crawlingRuleData.value
                            api_parameter_list.append(parameter_data)


if __name__ == '__main__':
    data = {}
    name = "a"
    value = "b"
    data[name] = value
    print(data)
