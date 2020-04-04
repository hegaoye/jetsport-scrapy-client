# coding=utf-8
import json
import threading

from src.base.enum.parameter_type_enum import ParameterTypeEnum
from src.base.enum.y_n_enum import YNEnum
from src.base.log4py import logger
from src.base.singleton import Singleton
from src.entity.data_cache import DataCache
from src.service.api_serivce import ApiService
from src.service.crawling_rule_data_service import CrawlingRuleDataService
from src.service.crawling_rule_service import CrawlingRuleService
from src.service.data_cache_service import DataCacheService
from src.service.parameter_serivce import ParameterService
from src.thread.base_thread import BaseTread


class ConstructDataThread(BaseTread, Singleton):
    """
    构造用于推送的数据，保持单例模式，禁止多线程跑多个实例导致指令执行的混乱
    """

    def __init__(self, crawlingRule=None):
        threading.Thread.__init__(self)
        self.crawlingRule = crawlingRule
        self.apiService = ApiService()
        self.crawlingRuleService = CrawlingRuleService()
        self.crawlingRuleDataService = CrawlingRuleDataService()
        self.parameterService = ParameterService()
        self.dataCacheService = DataCacheService()

    def run(self) -> None:
        try:
            self.__build_data()
        except Exception as e:
            logger.error(e)

    def __build_data(self):
        """
        构造接口数据
        1.查询接口列表
        2.查询参数列表
        3.查询参数数据
        4.构造结构
        5.存储构造的数据到datacache中
        6.删除已经被构造的数据
        """
        # 1.查询接口列表
        api_list = self.apiService.list()

        # 2.查询参数列表
        if api_list and len(api_list) > 0:
            for api in api_list:
                api_parameter_list = []
                id_list = []
                parameter_code_list = self.parameterService.list_code(api.code, YNEnum.Y.name)
                pre_id_list = self.crawlingRuleDataService.list_pre_id(parameter_code_list)
                if not pre_id_list:
                    continue

                for pre_id in pre_id_list:
                    ids, parameter_data = self.__build_param(pre_id, {})
                    id_list = id_list + ids
                    api_parameter_list.append(parameter_data)

                # 5. 存储构造的数据到datacache中
                self.__data_cache(api.code, api_parameter_list)

                # 6.删除已经被构造的数据 todo 暂时注释避免数据被删，调试好后，需要解开注释
                # self.crawlingRuleDataService.delete_list(id_list)

    def __build_param(self, pre_id, parameter_data):
        print(str(pre_id))
        id_list = []
        # 3.查询参数数据
        crawling_rule_data_list = self.crawlingRuleDataService.list_by_pre_id(pre_id)
        print(len(crawling_rule_data_list))
        # 4.构造结构
        for crawlingRuleData in crawling_rule_data_list:
            if crawlingRuleData.pre_parameter_code:
                parameter_load = self.parameterService.load(crawlingRuleData.pre_parameter_code)
                if parameter_load:
                    if ParameterTypeEnum.List.name.__eq__(parameter_load.parameter_type):
                        pre_param_name = parameter_load.name
                        sub_parameter_data_list = []
                        sub_parameter_data = {}
                        sub_parameter_data[crawlingRuleData.parameter_name] = crawlingRuleData.value
                        sub_parameter_data_list.append(sub_parameter_data)
                        if pre_param_name in parameter_data.keys():
                            parameter_data[pre_param_name] = parameter_data[pre_param_name] + sub_parameter_data_list
                        else:
                            parameter_data[pre_param_name] = sub_parameter_data_list
            else:
                parameter_data[crawlingRuleData.parameter_name] = crawlingRuleData.value
                sub_id_list, sub_parameter_data = self.__build_param(crawlingRuleData.code, parameter_data)
                if id_list:
                    id_list = id_list + sub_id_list

            id_list.append(crawlingRuleData.id)

        return id_list, parameter_data

    def __data_cache(self, api_code, api_parameter_list):
        """
        缓存 数据
        :param api_code: 接口编码
        :param api_parameter_list: 数据集合
        :return:
        """
        dataCache = DataCache()
        dataCache.api_code = api_code
        dataCache.data = json.dumps(api_parameter_list)
        self.dataCacheService.save(dataCache)


if __name__ == '__main__':
    constructDataThread = ConstructDataThread()
    constructDataThread.start()
