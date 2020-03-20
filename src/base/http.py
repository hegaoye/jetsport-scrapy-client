# coding=utf-8
from urllib import request, parse

from src.base.command import Command
from src.base.log4py import logger
from src.base.r import R
from src.dao.setting_dao import SettingDao


def get(url):
    setting_dao = SettingDao()
    host = setting_dao.load_value(Command.Host)
    url = host + url
    logger.debug("请求url: " + url)
    response = request.urlopen(url)
    result = response.read().decode(encoding='utf-8')
    if result != None:
        r = R()
        r.to_obj(result)
        return r


def post(url, data=None, headers=None):
    try:
        logger.info(url)
        setting_dao = SettingDao()
        host = setting_dao.load_value(Command.Host.name)
        url = host + url
        postdata = parse.urlencode(data).encode('utf-8')
        logger.info("请求url: " + url)
        logger.info("请求参数: " + str(postdata))
        if headers:
            req = request.Request(url, data=postdata, method="POST", headers=headers)
        else:
            req = request.Request(url, data=postdata, method="POST")
        response = request.urlopen(req)
        result = response.read().decode(encoding='utf-8')
        beanret = R().to_obj(result)
        headers_return = response.headers
        if headers_return:
            if headers_return["authorization"]:
                beanret.authorization = str(headers_return["authorization"]).replace("'", "")
        return beanret
    except Exception as e:
        print(e)
        return R(success=False)
