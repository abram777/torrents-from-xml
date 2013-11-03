#!/usr/bin/env python

from sys import argv
from GeekToolKickassTorrentFeed import GeekToolKickassTorrentFeed

if __name__ == "__main__" and len(argv) > 1:
    mode = argv[1]

    print(str.format("{0}{1}", "\t" * 4, mode.capitalize()))

    feed = GeekToolKickassTorrentFeed(mode)
    if feed:
        feed_data = feed.get_top_seeded_torrents().fetch().get_formatted_list()
        print(feed_data)
    else:
        print("No torrents available")
