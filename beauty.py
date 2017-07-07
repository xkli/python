import urllib2
from bs4 import BeautifulSoup
import json


class Img:
    pic = ''
    height = 0

    def __init__(self, _pic, _height):
        self.pic = _pic
        self.height = _height


def img2dict(self):
    return {'pic': self.pic,
            'height': self.height}


def parse_html(fp, url):
    print url
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()

    soup = BeautifulSoup(html)
    tags = soup.findAll('a')

    pins = '-1'
    for tag in tags:
        if isinstance(tag.get('class'), list):
            if 'layer-view' in tag.get('class'):
                pins = tag.get('href')[6:-1]
                img_url = "http:" + tag.find('img')['src']
                img = Img(img_url, 0)
                img_json = json.dumps(img, default=img2dict)
                fp.write(img_json+',')
                print img_json
    return pins


fp = open('beauty.txt', 'w')

last_max = '1030893410'
i = 0
while not (not last_max):
    start_page_url = 'https://huaban.com/boards/15729161/?md=newbn&beauty=&j46r9bt2&max=' + last_max + '&limit=20&wfl=1'
    last_max = parse_html(fp, start_page_url)
    if last_max == '-1':
        print 'The page has no picture!'
        break
    i = i + 1
    if i == 3:
        break

fp.close()
