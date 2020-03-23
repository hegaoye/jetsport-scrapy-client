from src.base.singleton import Singleton
from src.entity.crawling_data import CrawlingData


class CrawlingDataDao(Singleton):

    def insert(self, crawling_data) -> None:
        CrawlingData.create(crawling_code=crawling_data.crawling_code, value=crawling_data.value,
                            data_type=crawling_data.data_type, pre_code=crawling_data.pre_code)
