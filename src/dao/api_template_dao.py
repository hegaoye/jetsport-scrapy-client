# coding=utf-8
from src.entity.api_template import ApiTemplate


class ApiTemplateDao:
    """
    接口参数模板Dao
    """

    def insert(self, apiTemplate) -> None:
        ApiTemplate.create(api_code=apiTemplate.api_code, args_template=apiTemplate.args_template)

    def load(self, api_code) -> ApiTemplate:
        return ApiTemplate.get(ApiTemplate.api_code == api_code)
