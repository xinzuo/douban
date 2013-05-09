# -*- coding : utf8 -*-
import urllib2
import ujson as json
from pprint import pprint


class DouBan:
    def __init__(self):
        url = 'http://www.douban.com/j/app/radio/channels'
        page = urllib2.urlopen(url, timeout=10)
        self.data = page.read()

    def get_channels(self):
        info_dic = json.loads(self.data)
        channels = sorted(info_dic["channels"][1:], key=lambda x:x["channel_id"])
        return channels

    def get_songs(self, _cid):
        url = 'http://douban.fm/j/mine/playlist?type=n&sid=759462&pt=8.2&channel=%s&pb=64&from=mainsite&r=f25a616873'%_cid
        page = urllib2.urlopen(url, timeout=10)
        data = page.read()
        return json.loads(data)["song"]



if __name__ == '__main__':
    douban = DouBan()
    channels = douban.get_channels()
    #for x in channels:
        #print x["channel_id"], x["name"]
    songs = douban.get_songs(1)
    for x in songs:
        print x["title"]
        print x["url"]
        print x["rating_avg"]

