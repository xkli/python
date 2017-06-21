import urllib2
from bs4 import BeautifulSoup


def parse_html(url):
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
                img_url = "http:" + tag.find('img')['src'];
                print img_url
    return pins


last_max = '1030893410'
i = 0
while not (not last_max):
    start_page_url = 'https://huaban.com/boards/15729161/?md=newbn&beauty=&j46r9bt2&max=' + last_max + '&limit=20&wfl=1'
    last_max = parse_html(start_page_url)
    if last_max == '-1':
        print 'The page has no picture!'
        break
    i = i + 1
    if i == 3:
        break
