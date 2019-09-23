# -*- encoding:UTF-8

import requests
from sys import argv
import pyquery,os,time,re


def downloadAsXXX(url,fileName,trials):
    if trials == None:
        trials == 3
    print("Downloading "+url)
    for i in range(0, trials):
        pic = requests.get(url, stream=True)
        if pic.status_code == 200:
            with open(fileName, "wb") as f:
                f.write(pic.content)
                return
        else:
            print("Sorry,try again.")
    print("Fail to save", fileName)


if __name__ == "__main__":
    base_url = ""
    page = requests.get(base_url+"")
    html = page.text.encode(page.encoding)
    print(html)