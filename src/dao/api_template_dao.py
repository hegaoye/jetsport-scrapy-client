# coding=utf-8
from src.entity.api_template import ApiTemplate


class ApiTemplateDao:
    """
    接口参数模板Dao
    """

    def insert(self, apiTemplate) -> None:
        """
        插入一条 api 模板
        :param apiTemplate: 模板对象
        """
        ApiTemplate.create(api_code=apiTemplate.api_code, args_template=apiTemplate.args_template)

    def load(self, api_code) -> ApiTemplate:
        """
        加载一个接口模板
        :param api_code: 接口code
        :return: ApiTemplate
        """
        return ApiTemplate.get(ApiTemplate.api_code == api_code)
