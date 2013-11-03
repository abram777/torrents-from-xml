"""http://www.python.org/dev/peps/pep-0263/"""
# coding=utf-8

from xml.dom import minidom

try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen


class TorrentFeed(object):
    __base_url = None
    __dom = None
    __limit = 0
    __modes = None
    __sortBySeedersParams = None
    _torrents = []
    url = None

    @staticmethod
    def _safe_format(safe, error):
        try:
            return safe()
        except (UnicodeDecodeError, UnicodeEncodeError):
            return error()

    @staticmethod
    def _normalize(s):
        """http://stackoverflow.com/questions/9589183/django-and-mysql-encoding-difficulties"""
        try:
            return s.encode('utf-8').replace('Ã¡', 'á').replace('Ã³', 'ó').replace('Ã§', 'ç').replace('Ã£', 'ã')\
                .replace('Ã', 'í')
        except TypeError:
            pass

    def __init__(self, mode):
        self.mode = mode
        self.__set_url()

    def __set_url(self):
        if self.mode in self.__modes:
            self.url = str.format(self.__base_url, self.mode)
        else:
            self.url = None

    def __get_dom(self, sort_option=None):
        if self.is_valid():
            url = self.url if not sort_option else str.format("{0}&{1}", self.url, sort_option)
            self.__dom = minidom.parse(urlopen(url))

        return self

    def _get_items(self):
        return self.__dom.getElementsByTagName('item') if self.__limit <= 0 \
            else self.__dom.getElementsByTagName('item')[0:self.__limit]

    def _set_base_url(self, base_url):
        self.__base_url = base_url

    def _set_sort_by_seeders_params(self, params):
        self.__sortBySeedersParams = params

    def _set_available_modes(self, modes):
        self.__modes = modes

    def set_limit(self, limit):
        self.__limit = limit

    def is_valid(self):
        return self.url

    def get_new_torrents(self):
        self.__get_dom()

        return self

    def get_top_seeded_torrents(self):
        self.__get_dom(self.__sortBySeedersParams)

        return self

    def fetch(self):
        raise NotImplementedError

    def get_formatted_list(self):
        raise NotImplementedError

    def __nonzero__(self):
        """@Override"""
        return bool(self.is_valid())

    #Forwards compatibility with Python3
    __bool__ = __nonzero__
