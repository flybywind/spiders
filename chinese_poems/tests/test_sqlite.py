import os
import shutil
import pytest
from common import add_src2path

add_src2path()

parent_dir = "test_db"


def init_db_path():
    if os.path.exists(parent_dir):
        shutil.rmtree(parent_dir)
    os.mkdir(parent_dir)


@pytest.fixture
def mock_spider():
    return "mock spider"


@pytest.fixture
def db_ppl(mock_spider):
    from src.sqlite_pipeline import SqlitePipeline
    init_db_path()
    ppl = SqlitePipeline(parent_dir=parent_dir)
    ppl.open_spider(mock_spider)
    return ppl


@pytest.fixture
def db_dao(db_ppl):
    from src.sqlite_dao import SqliteDB
    return SqliteDB(parent_dir)


@pytest.fixture
def table_name(db_ppl):
    return db_ppl.table_name


def test_sqlit_ppl(db_ppl, table_name, mock_spider):
    ppl = db_ppl
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
        f"SELECT author from {table_name} where author = 'a'")
    lst = ppl.cursor.fetchall()
    assert len(lst) == 2
    ppl.cursor.execute(
        f"SELECT author from {table_name} where author = 'b'")
    lst = ppl.cursor.fetchall()
    assert len(lst) == 2
    shutil.rmtree(parent_dir)


def test_sql_dal(db_dao, table_name):
    db = db_dao
    with db.db_conn:
        db.db_conn.execute(f'''insert into {table_name}(author, url, title, poem, yiwen, created_at) 
                                values('a', 'url1', 'title', 'poem1,poem2', 'yiwen1, yiwen2', datetime('now', '-10 days'))
                        ''')
        db.db_conn.execute(f'''insert into {table_name}(author, url, title, poem, yiwen, created_at) 
                                values('a', 'url2', 'title', 'poem1,poem2', 'yiwen1, yiwen2', datetime('now'))
                        ''')
    assert db.has_crawled("url1", 7) == False
    assert db.has_crawled("url2", 7) == True
    shutil.rmtree(parent_dir)


def test_sql_scan(db_dao, table_name):
    with db_dao.db_conn:
        db_dao.db_conn.execute(f'''insert into {table_name}(author, url, title, poem, yiwen, created_at) 
                                values('a', 'url1', 'title', 'poem1,poem2', 'yiwen1, yiwen2', datetime('now', '-10 days'))
                        ''')
        db_dao.db_conn.execute(f'''insert into {table_name}(author, url, title, poem, yiwen, created_at) 
                                values('a', 'url2', 'title', 'poem1,poem2', 'yiwen1, yiwen2', datetime('now'))
                        ''')
        db_dao.db_conn.execute(f'''insert into {table_name}(author, url, title, poem, yiwen, created_at) 
                                values('b', 'url3', 'title', 'poem1,poem2', 'yiwen1, yiwen2', datetime('now'))
                        ''')
    item = db_dao.scan_db("author = 'a'")
    assert len(item) == 2
    assert item[0].author == 'a'
    assert item[1].url == 'url2'
