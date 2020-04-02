# coding=utf-8
__author__ = 'leo.he'

import logging

from settings import LOGGIN_FILE

logger = logging.getLogger()

fh = logging.FileHandler(LOGGIN_FILE)
fh.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)
