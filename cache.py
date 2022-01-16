import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class URLCache:
    """
    used for storage of ulrs.
    """

    def __init__(self, url_file):
        self.cache = []

        if os.path.exists(url_file):
            logger.info('cache file is found')
            self.cache = URLCache.read(url_file)

    def check(self, url):
        """
        Checks if a url presents in a cache.
        """
        is_cached = False

        if url in self.cache:
            is_cached = True

        return is_cached

    def add(self, url):
        if url not in self.cache:
            self.cache.append(url)

    def remove(self, url):
        if url in self.cache:
            self.cache.remove(url)

    def clean_all(self):
        self.cache = []

    @property
    def cached_urls(self):
        return self.cache

    @staticmethod
    def read(url_file):
        """
        To read the file the implemention depences on file's extention (txt, csv, xlsx)...
        """
        raise NotImplementedError("Not implemented")


if __name__ == '__main__':
    cache = URLCache(url_file='')
    cache.add('www.google.com')
    logger.info('cache internals:\n{}'.format(cache.cached_urls))
