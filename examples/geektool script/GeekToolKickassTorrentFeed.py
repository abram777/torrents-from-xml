from KickassTorrentFeed import KickassTorrentFeed
from utils import DiskSizeUtil


class GeekToolKickassTorrentFeed(KickassTorrentFeed):
    def get_formatted_list(self):
        result = []
        for torrent in self._torrents:
            format_str = "{0}, Seeds: {1}, Peers: {2}, Size: {3}{4}"

            title = torrent["title"]
            format_title = lambda t: lambda: str.format("{0}{1}", t[0:75], "...")
            title = title if len(title) < 90 else self._safe_format(format_title(title),
                                                                    format_title(self._normalize(title)))

            content_length = DiskSizeUtil.format_bytes(torrent["contentLength"])
            content_length_type = DiskSizeUtil.get_storage_type(torrent["contentLength"])["abbr"]

            format_torrent = lambda f, t, s, p, cl, clt: lambda: str.format(f, t, s, p, cl, clt)
            torrent = self._safe_format(
                format_torrent(format_str, title, torrent["seeds"], torrent["peers"], content_length,
                               content_length_type),
                format_torrent(format_str, self._normalize(title), torrent["seeds"], torrent["peers"], content_length,
                               content_length_type))

            result.append(torrent)
        return '\n'.join(result)