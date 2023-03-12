import os
import shutil
from common import add_src2path

add_src2path()

parent_dir = "test_db"


def init_db_path():
    if os.path.exists(parent_dir):
        shutil.rmtree(parent_dir)
    os.mkdir(parent_dir)


def test_sqlit_ppl():
    from src.sqlite_pipeline import SqlitePipeline

    mock_spider = "mock spider"
    init_db_path()
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
        "title": "test3",
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


def test_sql_dal():
    from src.sqlite_dao import SqliteDB
    from src.sqlite_pipeline import SqlitePipeline
    mock_spider = "mock spider"
    init_db_path()
    db = SqliteDB(parent_dir)
    ppl = SqlitePipeline(parent_dir=parent_dir)
    ppl.open_spider(mock_spider)
    with db.db_conn:
        db.db_conn.execute(f'''insert into {SqliteDB.table_name}(author, url, title, poem, yiwen, created_at) 
                                values('a', 'url1', 'title', 'poem1,poem2', 'yiwen1, yiwen2', datetime('now', '-10 days'))
                        ''')
        db.db_conn.execute(f'''insert into {SqliteDB.table_name}(author, url, title, poem, yiwen, created_at) 
                                values('a', 'url2', 'title', 'poem1,poem2', 'yiwen1, yiwen2', datetime('now'))
                        ''')
    assert db.has_crawled("url1", 7) == False
    assert db.has_crawled("url2", 7) == True
    shutil.rmtree(parent_dir)
