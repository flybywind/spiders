import os
import shutil
from common import add_src2path

add_src2path()

parent_dir = "test_db"


def test_sqlit_ppl():
    from src.sqlite_pipeline import SqlitePipeline

    mock_spider = "mock spider"
    if os.path.exists(parent_dir):
        shutil.rmtree(parent_dir)
    os.mkdir(parent_dir)
    ppl = SqlitePipeline(parent_dir=parent_dir)
    ppl.open_spider(mock_spider)
    ppl.process_item({
        "title": "test",
        "author": "a",
        "url": "url1",
        "poem": ['lin1', 'line2'],
        "yiwen": ['yiwen1', 'yiwen2', 'yiwen3']
    }, mock_spider)
    ppl.process_item({
        "title": "test2",
        "author": "a",
        "url": "url3",
        "poem": ['lin1', 'line2'],
        "yiwen": ['yiwen1', 'yiwen2', 'yiwen3']
    }, mock_spider)
    ppl.process_item({
        "title": "test",
        "author": "a",
        "url": "url1",
        "poem": ['lin1', 'line2'],
        "yiwen": ['yiwen1', 'yiwen2', 'yiwen3']
    }, mock_spider)
    ppl.process_item({
        "title": "test1",
        "author": "b",
        "url": "url2",
        "poem": ['lin1', 'line2'],
        "yiwen": ['yiwen1', 'yiwen2', 'yiwen3']
    }, mock_spider)
    ppl.process_item({
        "title": "test1",
        "author": "b",
        "url": "url",
        "poem": ['lin1', 'line2'],
        "yiwen": ['yiwen1', 'yiwen2', 'yiwen3']
    }, mock_spider)
    ppl.cursor.execute(
        f"SELECT author from {SqlitePipeline.table_name} where author = 'a'")
    lst = ppl.cursor.fetchall()
    assert len(lst) == 2
    ppl.cursor.execute(
        f"SELECT author from {SqlitePipeline.table_name} where author = 'b'")
    lst = ppl.cursor.fetchall()
    assert len(lst) == 2
    shutil.rmtree(parent_dir)
