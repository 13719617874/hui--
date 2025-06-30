import requests
from bs4 import BeautifulSoup
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = 'https://so.gushiwen.cn/gushi/tangshi.aspx'
response = requests.get(url, headers=headers)
html = response.text

tree = etree.HTML(html)
soup = BeautifulSoup(html, 'html.parser')

for i in range(1,9):

    strong_text = tree.xpath(f'/html/body/div[2]/div[1]/div[2]/div[{i}]/div/strong/text()')

    div_list = tree.xpath(f'/html/body/div[2]/div[1]/div[2]/div[@class="typecont"][{i}]/span')
    for div in div_list:
        title = div.xpath('.//a/text()')
        author = div.xpath('./text()')
        url_list= div.xpath('.//a/@href')
        html_url = url_list[0] if url_list else None
        detail_url = 'https://so.gushiwen.cn/' + html_url
        detail = requests.get(url=detail_url, headers=headers).text
        detail_tree = etree.HTML(detail)

        content = detail_tree.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/text()')
        #/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div
        #/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div/text()

        item = {}
        item['诗歌类型'] = strong_text if strong_text else None
        item['题目'] = title[0] if title else None
        item['作者'] = author[0] if author else None
        # item['详情网址'] = url_list[0] if url_list else None
        item['详情'] = content[0] if content else None


        with open('poems.txt', 'a') as f:

            f.write(str(item)+ "\n")