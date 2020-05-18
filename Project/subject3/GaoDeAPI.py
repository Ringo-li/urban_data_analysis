# -*- coding: utf-8 -*-
import arcpy
import requests
import json
import pandas as pd

url = 'https://restapi.amap.com/v3/direction/transit/integrated?\key=50ace0067201128f9781da8128e942f0&\
origin={}&destination={}&city=%E8%A5%BF%E5%AE%89&cityd=%E8%A5%BF%E5%AE%89&strategy=0&nightflag=0'.format('109.121117,34.447047','108.883543,34.197582')

dest = pd.read_excel(r'D:\rui\sw_analysis\homework\part5.comprehensive\chapter3\城市实时交通出行数据_数据模板\输入_终点_WGS84坐标系.xlsx')

print(url,dest)