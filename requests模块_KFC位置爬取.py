# -*- coding: utf-8 -*-                                                       
# @Time       :   2021/5/22 21:20
import requests
import json
import time


def KFC():
    f = open(r'D:\pycharm_community\project\爬虫\KFC.json', 'w+', encoding='utf-8')
    f.write('')
    # g = open(r'D:\pycharm_community\project\爬虫\KFC.txt', 'w+', encoding='utf-8')
    # g.write('')
    place = input('输入你想搜索的关键字(例如：北京)：')
    url_1 = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    # UA伪装：
    headers_1 = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                      '90.0.4430.212 Safari/537.36 Edg/90.0.818.66'}
    data_1 = {
        'cname': '',
        'pid': '',
        'keyword': place,
        'pageIndex': 1,
        'pageSize': '10000'
    }
    response = requests.post(url=url_1, data=data_1, headers=headers_1)
    page_text = response.text
    fp = open('../project/爬虫/KFC.json', 'a', encoding='utf-8')
    json.dump(page_text, fp=fp, ensure_ascii=False)


def file_formatting():
    with open(r'D:\pycharm_community\project\爬虫\KFC.json', 'r+', encoding='utf-8') as f:
        i = json.load(f)
        str_1 = str(i)
        k = json.loads(i)
        list_table = k['Table1']
        time_inquiry = time.strftime('%Y-%m-%d，%H：%M：%S', time.localtime())
        with open('../project/爬虫/KFC.txt', 'a', encoding='utf-8') as fp:
            fp.write(f'{time_inquiry}\n')
        for dic_place in list_table:
            num = dic_place['rownum']
            name = dic_place['storeName']
            address = dic_place['addressDetail']
            pro = dic_place['pro']
            pn = dic_place['provinceName']
            cn = dic_place['cityName']
            with open('../project/爬虫/KFC.txt', 'a', encoding='utf-8') as fp:
                fp.write(f'{num} --- [{pn},{cn}] 详细地址：{address} 【店名】：{name} （pro功能）：{pro}\n\n')
            print(f'{num} --- [{pn},{cn}] 详细地址：{address} 【店名】：{name} （pro功能）：{pro}')
        with open('../project/爬虫/KFC.txt', 'a', encoding='utf-8') as fp:
            fp.write(f'\n\n\n')


if __name__ == "__main__":
    KFC()
    file_formatting()
