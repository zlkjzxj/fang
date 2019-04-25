import urllib.request


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)
        if 200 != response.getCode():
            return None
        return response.read()
