# coding=utf-8
# Creator        :kelvin
# Date           :2015.12.10
# Description    :
# 分析日志数据
import re
import requests
import time


def get_city_by_ip(ip):
    """获取ip所在城市

    :param ip:
    """

    try:
        r = requests.get('http://ip.taobao.com/service/getIpInfo.php?ip=%s' % ip)
        time.sleep(0.1)
        city = r.json()['data']['country'] + r.json()['data']['city']
    except Exception as e:
        city = ''
        print('ERROR network error')

    return city


if __name__ == '__main__':
    pattern = re.compile(r"^\[.*\]\[INFO\]"
                         r"\ssearch"
                         r"\skeyword=(?P<keyword>.+)"
                         r"\sip=(?P<ip>\d+\.\d+\.\d+\.\d+)"
                         r"\sbrowser=(?P<browser>.+)$")

    with open('../clmvp.log', encoding='utf-8') as f:
        for line in f:
            match = pattern.match(line)
            theip = match.group('ip')
            print('ip=%s city=%s' % (theip, get_city_by_ip(theip)))
