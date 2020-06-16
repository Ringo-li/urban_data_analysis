import multiprocessing as mp
import time
import pandas as pd

data = pd.read_csv(r'../../file/subject/chapter5/检查.csv')
data['lat_wgs84'] = 0.00
data['lng_wgs84'] = 0.00
data02 = data.copy()

def coor_trans(i):
    for j in  range(i*100):
        data02.loc[j:j,('lat_wgs84','lng_wgs84')] = [data02.lat[j],data02.lng[j]]

def job(i):
    lst[i] = i ** 2

if __name__ == '__main__': 
    lst = list(range(10))

    start_time = time.time()
    

    for i in range(10):
        # print(i)
        # job(i)
        job_multi = mp.Process(target=job,args=(i,))
        job_multi.start()


    #最后一个非100整数对象
    # for i in range(len(data02)-(len(data02)%100),len(data02)):
    #     data02.loc[i:i,('lat_wgs84','lng_wgs84')] = [data02.lat[i],data02.lng[i]]
    #主线程
    end_time = time.time()
    print('time use:{}'.format(end_time-start_time))
    # print(data02.loc[2995:3003])
    print(lst)