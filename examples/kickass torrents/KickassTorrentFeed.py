from TorrentFeed import TorrentFeed


class KickassTorrentFeed(TorrentFeed):
    def __init__(self, mode=None):
        self._set_available_modes(['movies', 'music', 'applications', 'anime', 'books'])
        self._set_base_url('http://kickass.to/{0}/?rss=1')
        self._set_sort_by_seeders_params('field=seeders&sorder=desc')
        self.set_limit(10)
        super(KickassTorrentFeed, self).__init__(mode)

    def fetch(self):
        get_data = lambda tag: lambda i: [ii.data for ii in i.getElementsByTagName(tag)[0].childNodes
                                          if ii.nodeType == ii.TEXT_NODE][0]

        get_title = get_data('title')
        get_link = get_data('link')
        get_content_length = get_data('torrent:contentLength')
        get_seeds = get_data('torrent:seeds')
        get_peers = get_data('torrent:peers')
        get_is_verified = get_data('torrent:verified')

        for item in self._get_items():
            self._torrents.append({
                "title": get_title(item),
                "contentLength": get_content_length(item),
                "link": get_link(item),
                "seeds": get_seeds(item),
                "peers": get_peers(item),
                "isVerified": get_is_verified(item),
            })

        return self
