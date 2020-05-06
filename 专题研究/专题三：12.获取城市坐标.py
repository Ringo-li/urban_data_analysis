# -*- coding: utf-8 -*-

import arcpy
import pandas  as pd

#中国城市地图位置
fc = r'D:\rui\code_analysis\file\subject\chapter3\市界_region.shp'

#设置空间参照坐标系，在arcgis中设置好中国城市地图坐标系，右击图层layer——属性——坐标系——另存坐标系文件
sr = arcpy.SpatialReference(r'D:\rui\code_analysis\file\subject\chapter3\Xian 1980 3 Degree GK CM 108E.prj')

#创建游标，遍历表格,获取城市名称，X/Y坐标
with arcpy.da.SearchCursor(fc,['NAME','shape@X','shape@Y'],spatial_reference=sr) as cursor:
    ls = []
    for row in cursor:
        #游标获取元组数据，转换为列表
        print list(row)
        data = list(row)
        #将获得的列表数据保存到ls中
        ls.append(data)
    #ls为二维数值形式，将其转换为pandas对象并导出，注意导出编码为utf8
    pd.DataFrame(ls).to_csv(r'D:\rui\code_analysis\file\subject\chapter3\coor_xian80.csv',encoding='utf8')





