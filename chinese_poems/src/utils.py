import os
from os import path


def get_url_from_href(parent, href):
    if href.startswith("http://") or href.startswith("https://"):
        return href
    else:
        host = "/".join(parent.split("/")[:3])
        return host + href


def init_db_dir(dir_name):
    if not path.exists(dir_name):
        os.mkdir(dir_name)
