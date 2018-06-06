# coding=utf-8

import requests


def main():
    url = "https://lucky.nocode.com/public_lottery?page=1&size=5"
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjc0NjUxLCJuaWNrX25hbWUiOiJsemp1biIsImF2YXRhciI6Imh0dHBzOi8vd3gucWxvZ28uY24vbW1vcGVuL3ZpXzMyL2liRWYwaWFZZFV2R3hMbXVmcVpDQmxtQ1pBMUlGZVdwWUc1aWJQQ0dTOUZNaFRwY2xyaWJRWDFjakEwN2lhcnhNaWNxODVRdzQ2aWNFWDRwTmg0a3k1WXdoRjJhdy8wIiwiaWF0IjoxNTIyOTcwNzc2LCJleHAiOjE1MjM1NzU1NzZ9.9tl6PYffqtUitVIYAYr_TCo9CD_h7Qn-mWsA32KN4Cg"}
    res = requests.get(url, headers=headers)
    lotteries = res.json().get("data")
    join_url = "https://lucky.nocode.com/lottery/{id}/join"
    for lottery in lotteries:
        res = requests.post(join_url.format(id=lottery.get("id")), headers=headers)
        data = res.json()
        if res.status_code == 200 and 'errors' not in data:
            print("成功参与抽奖：《%s》" % lottery.get("prizes").get("data")[0].get("name"))


if __name__ == '__main__':
    main()
