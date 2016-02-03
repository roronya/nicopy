nicopy
======

nicopy is python library for http://www.nicovideo.jp.

Features
--------

-  Get video info
-  Get mylist info
-  Get movie flv

Installation
------------

::

    $ pip install nicopy

Usage
-----

import
~~~~~~

::

    >>> import nicopy

Get video info
~~~~~~~~~~~~~~

::

    >>> video_info =_nicopy.get_video_info('sm9')
    >>> import pprint
    >>> pp = pprint.PrettyPrinter(indent=4)
    >>> pp.pprint(video_info)
    {   'comment_num': '4358837',
        'description': 'レッツゴー！陰陽師（フルコーラスバージョン）',
        'embeddable': '1',
        'first_retrieve': '2007-03-06T00:33:00+09:00',
        'last_res_body': '悪霊退散★悪霊退散★悪 ',
        'length': '5:19',
        'movie_type': 'flv',
        'mylist_counter': '161612',
        'no_live_play': '0',
        'size_high': '21138631',
        'size_low': '17436492',
        'tags': [   {'lock': 1, 'tag': '陰陽師'},
                    {'lock': 1, 'tag': 'レッツゴー！陰陽師'},
                    {'lock': 1, 'tag': '公式'},
                    {'lock': 1, 'tag': '音楽'},
                    {'lock': 1, 'tag': 'ゲーム'},
                    {'lock': 0, 'tag': '豪血寺一族'},
                    {'lock': 0, 'tag': 'β時代の英雄'},
                    {'lock': 0, 'tag': '最古の動画'}],
        'thumb_type': 'video',
        'thumbnail_url': 'http://tn-skr2.smilevideo.jp/smile?i=9',
        'title': '新・豪血寺一族 -煩悩解放 - レッツゴー！陰陽師',
        'user_icon_url': 'http://usericon.nimg.jp/usericon/s/0/4.jpg?1271141672',
        'user_id': '4',
        'user_nickname': '運営長の中の人',
        'video_id': 'sm9',
        'view_counter': '15429057',
        'watch_url': 'http://www.nicovideo.jp/watch/sm9'}

Get mylist info
~~~~~~~~~~~~~~~

::

    >>> mylist_info = nicopy.get_mylist_info('36079068')
    >>> pp.pprint(mylist_info)
    {   'copyright': <copyright>(c) DWANGO Co., Ltd.</copyright>,
        'description': 'http://www.lovelastsforever.net\n'
                    '\n'
                    'YouTube\n'
                    'http://www.youtube.com/user/LoveLastsForeverJPN',
        'docs': <docs>http://blogs.law.harvard.edu/tech/rss</docs>,
        'generator': 'ニコニコ動画',
        'items': [   {   'description': '<p class="nico-memo">plan : 2.5 '
                                        '「HASHTAG LADY -Official '
                                        'Trailer-」</p><p '
                                        'class="nico-thumbnail"><img alt="LOVE '
                                        'LASTS FOREVER  &amp;quot;HASHTAG '
                                        'LADY&amp;quot; (Official Trailer)" '
                                        'src="http://tn-skr1.smilevideo.jp/smile?i=20638700" '
                                        'width="94" height="70" '
                                        'border="0"/></p><p '
                                        'class="nico-description">バンドのアルバムを出します。iTunes '
                                        'ver.は2013/5/1、USBメモリver. '
                                        'Amazonにて2013/5/22発売です。http://www.lovelastsforever.net/musicmylist/36079068LOVE '
                                        'LASTS FOREVER  "HASHTAG LADY" '
                                        '(Official Trailer)Design by Himemi '
                                        'Sakamoto & yuxuki '
                                        'wagaYouTubehttp://youtu.be/rdwmU_Db7Hg</p><p '
                                        'class="nico-info"><small><strong '
                                        'class="nico-info-length">3:27</strong>｜<strong '
                                        'class="nico-info-date">2013年04月18日 '
                                        '21：15：57</strong> 投稿</small></p>',
                        'guid': 'tag:nicovideo.jp,2013-04-18:/watch/1366287357',
                        'link': 'http://www.nicovideo.jp/watch/sm20638700',
                        'pubDate': 'Thu, 18 Apr 2013 21:41:52 +0900',
                        'title': 'LOVE LASTS FOREVER  &quot;HASHTAG '
                                'LADY&quot; (Official Trailer)'},
                    {   'description': '<p class="nico-memo">plan : 02 「アイバリィ '
                                        '-plan B-」</p><p '
                                        'class="nico-thumbnail"><img alt="LOVE '
                                        'LASTS FOREVER「アイバリィ -plan B-」" '
                                        'src="http://tn-skr1.smilevideo.jp/smile?i=20616364" '
                                        'width="94" height="70" '
                                        'border="0"/></p><p '
                                        'class="nico-description">アルバム出します！iTunes '
                                        'ver.は2013/5/1、USBメモリver. '
                                        'Amazonにて2013/5/22発売です。http://lovelastsforever.net/musicmylist/36079068"アイバリィ '
                                        '/ Love Needle" Music '
                                        'VideoGraphic：Himemi '
                                        'SakamotoMovie：akkaYouTubehttp://youtu.be/F3gs0JIXOvE</p><p '
                                        'class="nico-info"><small><strong '
                                        'class="nico-info-length">3:08</strong>｜<strong '
                                        'class="nico-info-date">2013年04月15日 '
                                        '20：57：56</strong> 投稿</small></p>',
                        'guid': 'tag:nicovideo.jp,2013-04-15:/watch/1366027076',
                        'link': 'http://www.nicovideo.jp/watch/sm20616364',
                        'pubDate': 'Tue, 16 Apr 2013 07:27:44 +0900',
                        'title': 'LOVE LASTS FOREVER「アイバリィ -plan B-」'},
                    {   'description': '<p class="nico-memo">plan : '
                                        '01「高所恐怖症」</p><p '
                                        'class="nico-thumbnail"><img alt="LOVE '
                                        'LASTS FOREVER「高所恐怖症」" '
                                        'src="http://tn-skr1.smilevideo.jp/smile?i=20194320" '
                                        'width="94" height="70" '
                                        'border="0"/></p><p '
                                        'class="nico-description">DECOです。バンドとしての新曲です。アルバム出します。iTunes '
                                        'ver.は2013/5/1、USBメモリver. '
                                        'Amazonにて2013/5/22発売です。http://www.lovelastsforever.net/musicMusic '
                                        'by LOVE LASTS FOREVER  '
                                        'mylist/36079068Movie by hie  '
                                        'mylist/9655416YouTubehttp://youtu.be/nYEB_FJBmbE</p><p '
                                        'class="nico-info"><small><strong '
                                        'class="nico-info-length">3:38</strong>｜<strong '
                                        'class="nico-info-date">2013年02月26日 '
                                        '22：06：04</strong> 投稿</small></p>',
                        'guid': 'tag:nicovideo.jp,2013-02-26:/watch/1361883964',
                        'link': 'http://www.nicovideo.jp/watch/sm20194320',
                        'pubDate': 'Tue, 16 Apr 2013 07:27:52 +0900',
                        'title': 'LOVE LASTS FOREVER「高所恐怖症」'}],
        'language': 'ja-jp',
        'lastBuildDate': 'Thu, 17 Oct 2013 17:27:55 +0900',
        'link': 'http://www.nicovideo.jp/mylist/36079068',
        'pubDate': 'Thu, 17 Oct 2013 17:27:55 +0900',
        'title': 'マイリスト LOVE LASTS FOREVER‐ニコニコ動画'}

Get flv
~~~~~~~

::

    >>> cookie = nicopy.login('ronyaaaaaaa@gmail.com', 'niconicoT40b9t319')
    >>> flv = nicopy.get_flv('sm9', cookie)
    >>> with open('sm9.flv', 'wb') as f:
    ...     f.write(flv)
