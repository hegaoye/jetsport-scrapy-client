from src.dao.crawling_data_dao import CrawlingDataDao
from src.service.base_service import BaseService


class CrawlingDataService(BaseService):
    def __init__(self):
        self.crawlingDataDao = CrawlingDataDao()

    def save(self, crawling_data) -> None:
        self.crawlingDataDao.insert(crawling_data)

    def saveOrModify(self,crawling_data):
        self.crawlingDataDao
        self.crawlingDataDao.insert(crawling_data)
