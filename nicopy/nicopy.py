import requests
import urllib.parse
import re
from bs4 import BeautifulSoup
from .exception import *


def login(mailaddress, password):
    response = requests.post(
        "https://secure.nicovideo.jp/secure/login?site=niconico",
        data={'mail_tel': mailaddress,
              'password': password},
        allow_redirects=False
    )
    if response.status_code != 302:
        raise FailedLoginError()
    return response.cookies


def get_video_info(video_id, timeout=5):
    response = requests.get(
        "http://ext.nicovideo.jp/api/getthumbinfo/{0}".format(video_id), timeout=timeout)
    xml = response.content
    soup = BeautifulSoup(xml, 'xml')
    exists = lambda element: element.get_text() if element is not None else 'undefined'
    thumb_info = {'video_id': soup.find('video_id'),
                  'title': soup.find('title'),
                  'description': soup.find('description'),
                  'thumbnail_url': soup.find('thumbnail_url'),
                  'first_retrieve': soup.find('first_retrieve'),
                  'length': soup.find('length'),
                  'movie_type': soup.find('movie_type'),
                  'size_high': soup.find('size_high'),
                  'size_low': soup.find('size_low'),
                  'view_counter': soup.find('view_counter'),
                  'comment_num': soup.find('comment_num'),
                  'mylist_counter': soup.find('mylist_counter'),
                  'last_res_body': soup.find('last_res_body'),
                  'watch_url': soup.find('watch_url'),
                  'thumb_type': soup.find('thumb_type'),
                  'embeddable': soup.find('embeddable'),
                  'no_live_play': soup.find('no_live_play'),
                  'tags': [{'tag': tag.get_text(), 'lock': int(tag.attrs['lock']) if 'lock' in tag.attrs else 0}
                           for tag in soup.find('tags').find_all('tag')],
                  # use_* は無い可能性があるので上で定義したlambda式で包む
                  'user_id': exists(soup.find('user_id')),
                  'user_nickname': exists(soup.find('user_nickname')),
                  'user_icon_url': exists(soup.find('user_icon_url'))}
    return thumb_info


def get_flv(video_id, cookies, timeout=300):
    flv_url = get_flv_url(video_id, cookies)
    response = requests.get(flv_url, cookies=cookies, timeout=timeout)
    content = response.content
    return content


def get_mylist_info(mylist_id, timeout=5):
    response = requests.get(
        'http://www.nicovideo.jp/mylist/{0}?rss=2.0&lkang=ja-jp'.format(mylist_id), timeout=timeout)
    if response.status_code == 404:
        raise NotFoundError()
    else:
        xml = response.content.decode('utf-8')
        xml = xml.replace('dc:creator', 'creator').encode('utf-8')
        soup = BeautifulSoup(xml, 'xml')
        mylist_info = {'id': mylist_id,
                       'title': soup.find('title').get_text(),
                       'creator': soup.find('creator').get_text(),
                       'link': soup.find('link').get_text(),
                       'description': soup.find('description').get_text(),
                       'pubDate': soup.find('pubDate').get_text(),
                       'lastBuildDate': soup.find('lastBuildDate').get_text(),
                       'generator': soup.find('generator').get_text(),
                       'language': soup.find('language').get_text(),
                       'copyright': soup.find('copyright'),
                       'docs': soup.find('docs'),
                       'items': [{'title': item.find('title').get_text(),
                                  'link': item.find('link').get_text(),
                                  'guid': item.find('guid').get_text(),
                                  'pubDate': item.find('pubDate').get_text(),
                                  'description': item.find('description').get_text(),
                                  'id': re.search(r'[^/]*$', item.find('link').get_text()).group(0),
                                  } for item in soup.find_all('item')]
                       }

        return mylist_info


def get_flv_url(video_id, cookies, timeout=5):
    cookies.update(get_nicohistory_cookie(video_id, cookies))
    getflv_url = 'http://flapi.nicovideo.jp/api/getflv/{0}'.format(video_id)
    if video_id[:2] == 'nm':
        getflv_url = 'http://flapi.nicovideo.jp/api/getflv/{0}?as3=1'.format(
            video_id)
    response = requests.get(getflv_url, cookies=cookies, timeout=timeout)
    response_body = urllib.parse.unquote(response.text)
    flv_url = re.search(r'url=([^&]+)', response_body).group(1)
    return flv_url


def get_nicohistory_cookie(video_id, cookies, timeout=5):
    response = requests.get(
        'http://www.nicovideo.jp/watch/' + video_id, cookies=cookies, timeout=timeout)
    return response.cookies
