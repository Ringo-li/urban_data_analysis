import pandas as pd
from selenium import webdriver
from lxml import etree
import time
import requests
import json

#ip = '{"code":0,"data":[{"ip":"58.218.214.152","port":6013,"outip":"182.90.203.164"}],"msg":"0","success":true}'

def get_proxy():

    targetUrl = "http://http.tiqu.alicdns.com/getip3?num=1&type=2&pro=&city=0&yys=0&port=1&pack=94107&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions=&gm=4"
    try:
        response = requests.get(targetUrl)
        if response.status_code == 200:
            data = json.loads(response.text)
            time.sleep(1)
            return data['data'][0]['ip'] + ':' + str(data['data'][0]['port'])
    except:
        return None

def search(company):
    PROXY = get_proxy()
    print(PROXY)
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--proxy-server=http://' + PROXY)
    lst = []
    driver = webdriver.Firefox(firefox_options=firefox_options)
    driver.get('https://www.qixin.com/')
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div/span[1]/input[2]').send_keys(company)
    driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[3]/div/div/div[2]/div/span[2]').click()
    html = driver.page_source
    sel = etree.HTML(html)
    check = sel.xpath('/html/body/div[2]/div/div/div/div/button')
    if check:
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/button').click()
    else:
        pass
    href = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div[3]/div[2]/div[1]/div[2]/div[1]/div[1]/a').get_attribute('href')
    driver.get(href)
    time.sleep(1)
    html = driver.page_source
    sel = etree.HTML(html)
    address = sel.xpath('/html/body/div[6]/div/div[1]/div[2]/table/tbody/tr[12]/td[2]/text()')[0]
    page_href = href.replace('publicly','related')
    driver.get(page_href)
    time.sleep(1)
    html_page = driver.page_source
    ht = etree.HTML(html_page)
    pages = int(ht.xpath('//div[@id="investment"]/div/span/text()')[0])//10+1
    lst.append(address)
    lst.append(pages)
    driver.quit()
    return lst


        # return search(company)

if __name__ == "__main__":
    companies = pd.read_excel(r'D:/rui/code_analysis/file/subject/chapter3/company_list.xlsx')
    for company in companies.name:
        dt = search(company)
        dt.append(company)
        pd.DataFrame([dt]).to_csv(r'D:/rui/code_analysis/file/subject/chapter3/company_list.csv',mode='a',header=False,index=False)