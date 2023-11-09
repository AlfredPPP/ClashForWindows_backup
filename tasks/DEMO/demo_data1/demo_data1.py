import json
import os
from datetime import datetime

import requests


def go_spider():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

    origin_url = 'https://www.cbirc.gov.cn/cn/view/pages/ItemList.html?itemPId=953&itemId=954&itemUrl=ItemListRightList.html&itemName=%E7%BB%9F%E8%AE%A1%E4%BF%A1%E6%81%AF'
    url = 'https://www.cbirc.gov.cn/cn/static/data/DocInfo/SelectItemAndDocByItemPId/data_itemId=953,pageSize=10.json'

    # 请求网址
    res = requests.request(method='get', url=url, headers=header, timeout=10)
    res_text = res.json().get('data')[0].get('docInfoVOList')[0].get('docSubtitle')
    res_pub_date = res.json().get('data')[0].get('docInfoVOList')[0].get('publishDate')
    print(res)


def run():
    go_spider()

    new_data = False
    # 爬虫逻辑，更新以下数据
    crawled_data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "title": "New Title",
        "data": [{"date": "20231026", "price": 100}]
    }

    # 读取现有数据
    file_path = 'tasks/FINANCE/finance_data1/finance_data1.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = json.load(file)
    else:
        existing_data = {}

    # 检查数据是否更新
    if crawled_data['date'] != existing_data.get('date') or crawled_data['title'] != existing_data.get('title'):
        new_data = True
        # 更新 JSON 文件
        with open(file_path, 'w') as file:
            json.dump(crawled_data, file)

    return new_data


if __name__ == "__main__":
    run()
