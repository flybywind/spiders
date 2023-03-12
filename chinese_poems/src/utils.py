def get_url_from_href(parent, href):
    if href.startswith("http://") or href.startswith("https://"):
        return href
    else:
        host = "/".join(parent.split("/")[:3])
        return host + href
