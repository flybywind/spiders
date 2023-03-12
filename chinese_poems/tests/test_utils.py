from common import add_src2path

add_src2path()


def test_href_url():
    from src.utils import get_url_from_href
    assert get_url_from_href(
        "http://a.b/d", "/xy.html") == "http://a.b/xy.html"
    assert get_url_from_href("http://a.b", "/xy.html") == "http://a.b/xy.html"
    assert get_url_from_href("https://a.b/d/xx.html",
                             "/xy.html") == "https://a.b/xy.html"
