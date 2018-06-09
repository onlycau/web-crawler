import requests

headers = {
    'Cookie': 'd_c0="AEDmxd4_rA2PTl8z-RA90dEiMDRHJQ6OeVw=|1527677767"; q_c1=3355c8f85f9b43ad9cc891f20a7ff76d|1527677767000|1527677767000; _zap=e9ebd1e5-ec8b-4192-8ba3-d00656274b92; l_n_c=1; _xsrf=20402289be4b906b32f035745115f3da; r_cap_id="Y2QwY2QyZGJkMDBmNDUwZGI3Y2M2ZDQwNGVlYzhmYjI=|1528441137|bc0eb3408c9b38f095e1b2295434d3f56134cc9c"; cap_id="MjNkNTA1ZDMxYTA3NGE4Njk0MTlmNTI4YzNkNzMzZDg=|1528441137|5db57c478acb0266e3f9e693befce493fb0c571f"; l_cap_id="Y2QyMmRjZGRhN2U5NGEyZDk4ODhmMDk1Nzk3NjJmNmQ=|1528441137|4fa2dc6a343605af9c481e5228ddb4bad2bf430b"; n_c=1; __utma=51854390.1055570851.1528441160.1528441160.1528441160.1; __utmb=51854390.0.10.1528441160; __utmc=51854390; __utmz=51854390.1528441160.1.1.utmcsr=germey.gitbooks.io|utmccn=(referral)|utmcmd=referral|utmcct=/python3webspider/content/3.2.1-%E5%9F%BA%E6%9C%AC%E4%BD%BF%E7%94%A8.html; __utmv=51854390.000--|3=entry_date=20180530=1; tgw_l7_route=56f3b730f2eb8b75242a8095a22206f8; capsion_ticket="2|1:0|10:1528442750|14:capsion_ticket|44:NTQ2YTBlMjljNTJiNDZiYmI3OTI5NDkxMzc2MzI3NzY=|b4d2dfebfbd2a8a26cb960d77e6f9bfc41048bcf690e95dd77a026b1a29e9b7b"; z_c0="2|1:0|10:1528442775|4:z_c0|92:Mi4xeE8yakF3QUFBQUFBUU9iRjNqLXNEU1lBQUFCZ0FsVk5sMzBIWEFDdG1MTTZ4WVRWaVBpWjlTUUd6U01PZlFZNjFB|842918d39e0a07246e4ba9085b26b9be80ae5a1c5e4452af416fda43cf61aef2"',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
r = requests.get('https://www.zhihu.com', headers=headers)
print(r.text)