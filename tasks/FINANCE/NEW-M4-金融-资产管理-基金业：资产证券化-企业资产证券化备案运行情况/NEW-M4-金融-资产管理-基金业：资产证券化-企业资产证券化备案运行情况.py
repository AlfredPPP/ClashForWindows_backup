import json
import os
import logging
import requests
from datetime import datetime
from lxml import etree

def go_spider():
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    }

    origin_url = 'https://www.amac.org.cn/researchstatistics/report/zczjhhybg/'
    url = 'https://www.amac.org.cn/researchstatistics/report/zczjhhybg/'

    # 请求网址

    logging.info("正在抓取：NEW-M4-金融-资产管理-基金业：资产证券化-企业资产证券化备案运行情况")
    res = requests.request(method='get', url=url, headers=header, timeout=10)
    search_article_items = etree.HTML(res.content.decode()).xpath("//li[contains(string(),'企业资产证券化业务备案运行情况简报')]")
    for items in search_article_items:

        # 取网页的前10条数据，对应url中的pagesize=10
        res_text = ''.join(items.xpath(".//a/text()"))
        res_pub_date = ''.join(items.xpath(".//i/text()"))
        if res_text.__contains__('企业资产证券化业务备案运行情况简报'):
            res_data = {
                "title": res_pub_date + res_text,
                "data": f'''
                    检测到数据更新——
                    模板明细：NEW-M4-金融-资产管理-基金业：资产证券化-企业资产证券化备案运行情况
                    指标代码：1530097300
                    更新内容：{res_text}
                    更新时间：{res_pub_date}
                    抓取时间：{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                    模板网址：{origin_url}
                    '''
            }
            return res_data

        # 若到此步仍未返回，则说明不含关键字，则返回no_data
        res_data = {"title": 'no_data'}

    return res_data


def run():
    new_data = False

    # 读取现有数据
    file_path = os.path.dirname(os.path.abspath(__file__)) + '\\NEW-M4-金融-资产管理-基金业：资产证券化-企业资产证券化备案运行情况.json'
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                existing_data = json.load(file)
        except json.JSONDecodeError:
            existing_data = {"no_data": 'no_data'}
    else:
        existing_data = {"no_data": 'no_data'}

    # 运行爬虫
    crawled_data = go_spider()

    # 检查数据是否更新
    if not existing_data.__contains__(crawled_data['title']):
        new_data = crawled_data['data']
        logging.info("发现新数据")
        # 更新 JSON 文件
        with open(file_path, 'w', encoding='utf-8') as file:
            existing_data[f"{crawled_data['title']}"] = crawled_data['data']
            json.dump(existing_data, file, ensure_ascii=False)
    else:
        logging.info("网站数据未更新")

    return new_data


if __name__ == "__main__":
    run()
