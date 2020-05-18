# -*- coding:utf-8 -*-
import urllib



geocoding = {'key': '50ace0067201128f9781da8128e942f0',
             'address': '北京市朝阳区朝阳公园'}
geocoding = urllib.urlencode(geocoding)
ret = urllib.urlopen("%s?%s" % ("http://restapi.amap.com/v3/geocode/geo", geocoding))
print(ret.url)