# coding=utf-8

import urllib
import urllib.request
import json


def search(s):
    for i in range(50000, 100000):
        url_save = 'http://10.3.4.52:8070/test?param=' + str(i);

        try:
            s_save = urllib.request.urlopen(url_save).read()

            print("UTF-8 解码：", s_save.decode('UTF-8', 'strict'))
            data2 = json.loads(s_save.decode('UTF-8', 'strict'))
            if data2['flag'] == 1:
                print('success')
                print(data2['data'])
                break
            else:
                pass


        except Exception as e:
            print(e)


        print(str(i))

search("s")
