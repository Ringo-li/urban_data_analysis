import pandas as pd
import numpy as np
import requests 
import json
import time
from sqlalchemy import create_engine



class LocaDiv(object):
    #创建初始化参数
    def __init__(self,loc_all,divd):
        self.loc_all =  loc_all
        self.divd = divd
        
    #获取以divd分割的每个维度列表
    def lat_all(self):
        bl_lat = self.loc_all[0]
        ur_lat = self.loc_all[2]
        ls = [str(ur_lat)]
        while bl_lat < ur_lat:
            m = ur_lat - self.divd
            ls.append('%.2f' % m)
            ur_lat = m
        return sorted(ls)

    #获取以divd分割的每个经度列表
    def lng_all(self):
        bl_lng = self.loc_all[1]
        ur_lng = self.loc_all[3]
        ls = [str(ur_lng)]
        while bl_lng < ur_lng:
            m = ur_lng - self.divd
            ls.append('%.2f' % m)
            ur_lng = m
        return sorted(ls)
    
    #依次组合每个方格左下到右上的点
    def com_coor(self):
        lat_lst = self.lat_all()
        lng_lst = self.lng_all()
        lst = []
        for i in range(len(lat_lst)-1):
            for j in range(len(lng_lst)-1):
                lst.append(lat_lst[i])
                lst.append(lng_lst[j])
                lst.append(lat_lst[i+1])
                lst.append(lng_lst[j+1]) 
        arr = np.array(lst).reshape(len(lst)//4,4)
        return arr
    
        
class Baidupoi(object):
    def __init__(self,query,bounds,path):
        self.query = query
        self.bounds = bounds
        self.path = path
        
    def get_urls(self):
        urls = []
        for i in range(20):
            url = 'http://api.map.baidu.com/place/v2/search?query={}&bounds={}&output=json&\
ak=VYt6ipe4cG9t1CpURQr58ulXep2pcpY6&page_size=20&page_num={}'.format(self.query,self.bounds,i)
            urls.append(url)
        return urls

    def get_data(self):
        for i,url in enumerate(self.get_urls()):
            try:
                # print(i,url)
                js_obj = requests.get(url).text
                data = json.loads(js_obj)
                if data['status'] == 302 :
                    print('天配额超限，限制访问')
                    break
                elif data['total'] == 0 :
                    print('The {} data has been processed!'.format(self.query))
                    break
                elif data['total'] != 0 :
                    for item in data['results']:
                        js = {}
                        js['name'] = item['name']
                        js['lat'] = item['location']['lat']
                        js['lng'] = item['location']['lng']
                        yield js
                    pass
                else:
                    print('The {} data error!'.format(self.query))
                    break
            except:
                print('error!')
                with open(self.path,'a') as file:
                    file.write(time.ctime() + ' status:error' +'\n' + url + '\n')
                
if __name__ == '__main__':
    # pois = {'政府机构':['中央机构','各级政府','行政单位','公检法机构','涉外机构','党派团体','福利机构','政治教育机构','社会团体','民主党派','居民委员会']}

    pois = {'美食':['中餐厅','外国餐厅','小吃快餐店','蛋糕甜品店','咖啡厅','茶座','酒吧'],
'酒店':['星级酒店','快捷酒店','公寓式酒店','民宿'],
'购物':['购物中心','百货商场','超市','便利店','家居建材','家电数码','商铺','市场'],
'生活服务':['通讯营业厅','邮局','物流公司','售票处','洗衣店','图文快印店','照相馆','房产中介机构','公用事业','维修点','家政服务','殡葬服务','彩票销售点','宠物服务','报刊亭','公共厕所','步骑行专用道驿站'],
'丽人':['美容','美发','美甲','美体'],
'旅游景点':['公园','动物园','植物园','游乐园','博物馆','水族馆','海滨浴场','文物古迹','教堂','风景区','景点','寺庙'],
'休闲娱乐':['度假村','农家院','电影院','ktv','剧院','歌舞厅','网吧','游戏场所','洗浴按摩','休闲广场'],
'运动健身':['体育场馆','极限运动场所','健身中心'],
'教育培训':['高等院校','中学','小学','幼儿园','成人教育','亲子教育','特殊教育学校','留学中介机构','科研机构','培训机构','图书馆','科技馆'],
'文化传媒':['新闻出版','广播电视','艺术团体','美术馆','展览馆','文化宫'],
'医疗':['综合医院','专科医院','诊所','药店','体检机构','疗养院','急救中心','疾控中心','医疗器械','医疗保健'],
'汽车服务':['汽车销售','汽车维修','汽车美容','汽车配件','汽车租赁','汽车检测场'],
'交通设施':['飞机场','火车站','地铁站','地铁线路','长途汽车站','公交车站','公交线路','港口','停车场','加油加气站','服务区','收费站','桥','充电站','路侧停车位','普通停车位','接送点'],
'金融':['银行','ATM','信用社','投资理财','典当行'],
'房地产':['写字楼','住宅区','宿舍','内部楼栋'],
'公司企业':['公司','园区','农林园艺','厂矿'],
'政府机构':['中央机构','各级政府','行政单位','公检法机构','涉外机构','党派团体','福利机构','政治教育机构','社会团体','民主党派','居民委员会']
            }
    engine = create_engine('mssql+pyodbc://:@CLAIRE/baidu_poi?driver=SQL server')
    path = r'../../file/subject/chapter5/log.txt'
    # coor = [34.32016,108.962152,34.328478,108.972357]
    coor = [34.16985,108.756009,34.395586,109.146952]
    divd = 0.02
    print('Start crawling data...')
    start_time = time.time()
    loc = LocaDiv(coor,divd)
    locs_to_use = loc.com_coor()
    for h1,v in pois.items():
        print('##############################爬取 ',h1)
        file_name = 'baidu_poi_{}'.format(h1)
        for loc_to_use in locs_to_use[200:]:
            coor_use = ','.join(loc_to_use)
            print('##################200:/{} starting ...#####################'.format(len(locs_to_use)))
            for h2 in v:
                par = Baidupoi(h2,coor_use,path)
                dt = par.get_data()
                df = pd.DataFrame(dt)
                df['sort1'] = h1
                df['sort2'] = h2
                if len(df) !=0:
                    print(df)
                    df.to_sql(file_name,engine,if_exists='append')
                    time.sleep(1)
                    print('写入数据库成功！')
                else:
                    pass
            # time.sleep(1)
    end_time = time.time()
    print('All data download completed, it took {}s'.format(end_time-start_time))