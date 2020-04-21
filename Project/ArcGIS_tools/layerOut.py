# -*- coding: utf-8 -*-
import arcpy
import os

##########################################################
#设置目标mxd对象路径

mxd_path = arcpy.GetParameterAsText(0)
# mxd_path = r'D:\rui\code_analysis\file\GIS\class2101\MD.mxd'

#设置导出目录

lyronlist = arcpy.GetParameterAsText(1)

# lyronlist = ['XZQ_town','XZQ_vill_dt']

#常开图层列表

output_path = arcpy.GetParameterAsText(2)

# output_path = r'D:\rui\code_analysis\file\GIS\class2101\jpg'

#设置分辨率

resolution = arcpy.GetParameterAsText(3)
# resolution = 300

##########################################################
#实例化一个mxd对象

mxd = arcpy.mapping.MapDocument(mxd_path)

#将所有图层列出

lyrlist = arcpy.mapping.ListLayers(mxd)

#将所有图层名列出

lyrnlist = [i.name for i in arcpy.mapping.ListLayers(mxd)]

####################test#############################


#for循环每个需要打印的图层

for plyr in [ i for i in lyrnlist if i not in lyronlist]:

    #设置一个变量，容纳打开的图层对象

    layon = ''

    #for循环所有图层，打开需要打开的图层

    for lyr in lyrlist:
        if lyr.name in lyronlist:
            lyr.visible =  True
        elif lyr.name == plyr:
            lyr.visible = True
            layon = lyr
        else:
            lyr.visible = False

    #如果需要打印的图层已经打开，导出图片

    if layon.visible:
        arcpy.mapping.ExportToJPEG(mxd,
                              os.path.join(output_path,'{}.jpg'.format(plyr)),
                              resolution = resolution)
        arcpy.AddMessage('{} done!'.format(plyr))

#记得删除mxd实例

del mxd
arcpy.AddMessage('All layers done!')