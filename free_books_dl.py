import requests
import lxml
from lxml import html
import urllib2
import os.path


base_url = 'http://www.learndatasci.com/free-data-science-books/'

session = requests.Session()

response = session.get(base_url)
if response.status_code == 200:
    doc = html.fromstring(response.content)
    urls = doc.xpath("//a[@class='w-button ebook btn btn-3 btn-3e icon-arrow-right']/@href")
    for url in urls:
        if url.lower().endswith('.pdf'):
            # print "Downloading " + url
            '''
            res = session.get(url)
            if res.status_code == 200:
                filename = url.split('/')[-1]
                with open(filename, 'w') as f:
                    f.write(res.content)
                f.close()
            else:
                print "Downloading field"
            '''
            filename = url.split('/')[-1]
            if not os.path.exists(filename):
                print "Downloading " + url
                try:
                    res = session.get(url, timeout=30)
                    if res.status_code == 200:
                        try:
                            with open(filename, 'wb') as f:
                                f.write(res.content)
                            f.close()
                            print "Downloaded " + filename
                        finally:
                            f.close()
                    else:
                        continue
                except Exception as e:
                    print e
                    print "Time out"
                    with open('urls.txt', 'a') as f:
                        f.write(url + '\n')
                    continue
            else:
                print filename + " exists"
        else:
            with open('urls.txt', 'a') as f:
                f.write(url+'\n')
            f.close()

