import pytest
from ..Ahospital.pipelines import AhospitalPipeline
from ..Ahospital.spiders.spider import HospitalSpider

def test_pipeline():
    spider = HospitalSpider()
    ppl = AhospitalPipeline()
    ppl.open_spider(spider)

    assert type(spider.start_urls[0]).__name__ == 'str'
    if len(spider.start_urls) > 1:
        assert type(spider.start_urls[1]).__name__ == 'str'

