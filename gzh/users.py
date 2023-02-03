"""
导出公众号用户
"""
import csv
import pprint

import requests

field_order = ["用户", "关注时间", "头像", ]

csv.register_dialect('myDialect',
                     quoting=csv.QUOTE_ALL,
                     skipinitialspace=True)

url = "https://mp.weixin.qq.com/cgi-bin/user_tag"

params = {
    "action": "get_user_list",
    "groupid": -2,
    "begin_openid": "",
    "begin_create_time": 1633689214,
    "limit": 20,
    "offset": 0,
    "backfoward": 1,
    "token": 1830971770,
    "lang": "zh_CN",
    "f": "json",
    "ajax": 1,
    "random": 0.29653470243423685,
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    "HOST": "mp.weixin.qq.com",
    "Cookie": "appmsglist_action_2393828411=card; appmsglist_action_2393291452=card; appmsglist_action_2397322000=card; pgv_pvid=5422600736; RK=FAIdRbY8Hq; ptcz=f284ef07e30510ca4de096c3a2c609c24239ce649730ff32922337bcbc96c62c; tvfe_boss_uuid=eda94597299f6f90; o_cookie=253421576; pac_uid=1_253421576; _ga=GA1.2.11487159.1587366826; iip=0; pt_sms_phone=158******20; wxuin=03951858983307; openid2ticket_o8uaO6kKiXBtnsUlETb2A4RtJpp4=; UM_distinctid=17944bc50b4c-0cf5c1c972f9ea-3f356b-1fa400-17944bc50b52c2; eas_sid=W1B6e2c1P3o2s825h7L449n642; mm_lang=zh_CN; CNZZDATA1272960370=1269357260-1592369408-https%253A%252F%252Fmp.weixin.qq.com%252F%7C1624334587; CNZZDATA1272425418=1699923129-1592372262-https%253A%252F%252Fmp.weixin.qq.com%252F%7C1624333219; ua_id=8vO2bkcLMNeldl9JAAAAAARMJnerzvqXqrhZO5-2ZL4=; _tc_unionid=28741bd1-95d8-4004-b608-c93597a49688; ptui_loginuin=3152728896; rewardsn=; wxtokenkey=777; wyctoken=1047229450; cert=r_gnLEwDCmRmSctNwSzh7aFRv5ljtc8i; noticeLoginFlag=1; openid2ticket_om422jrdTnEAB1r7-zXTmKubGER0=qqaTXD9mZypTBOgsxUAKpwokMgP0bslDrUl51B0AtzU=; pgv_info=ssid=s3224305654; __root_domain_v=.weixin.qq.com; _qddaz=QD.685431855347487; qm_authimgs_id=1; qm_verifyimagesession=h01288f28f42f57f799b739f029a1fd6dd00411cc253d46ef3c49e95a203eb481fa1872a9d7cd2d9ac8; uin=o3152728896; skey=@qa7daF93n; verifysession=h0198482c9a961b40d48d9be0c086737b622244718f7f0b716609bf466f2589f1d5e39e3e720cccc715; openid2ticket_oPGiXjhP6KzS5g8fMV3OHuuZkwmg=G+j8HQkDFdF5q0VfaEJrQ9g2Fw5KhQ4O/4IQ2BIqBa0=; remember_acct=253421576%40qq.com; openid2ticket_ow-uujmHSiUtZWYpm7jDnwkAnt44=CTJSCoZR2Y7HbBnUXOhcSyKCah+fm/M44cd93sTGaEc=; _qpsvr_localtk=1633743705330; uuid=42c3b6618c2e2428b33c9d77957f072b; rand_info=CAESIB3yvUn/wRelwvbLVgFflUsR7vvGg5J5npDY/aewR4nE; slave_bizuin=3579961954; data_bizuin=3579961954; bizuin=3579961954; data_ticket=o4ZvZYyx/3A+0PYP8WZ9QcNHQaiFooXo+IELaIF/86dMx3jouQzyLaiLss/DYfGb; slave_sid=dlJmODk5cGdEaUNycVFDZnlyZU9QZ0ZNazZTdmNWZjQwOGN3QVVTME93VU9fMEVMS1JZUk93ZF94S25Ga1NfX3JRcEJQRml3a2p3RzJRTkZkZEpGWDVSd0tmUUE2UkJQeWlHTHZoWjg1ZEkwWVZhbEhQREFDb3ptMUVKWUI3Z3paQUtjaE03OURBa09nSUsz; slave_user=gh_a0467681d76f; xid=297e610c2b2fa8697d48ecd9e05ce948"
}

cookie = {
    "verifysession": "",
    "data_ticket": "o4ZvZYyx/3A+0PYP8WZ9QcNHQaiFooXo+IELaIF/86dMx3jouQzyLaiLss/DYfGb",
    "openid2ticket_oPGiXjhP6KzS5g8fMV3OHuuZkwmg": ""
}


def execute(begin_openid, begin_create_time):
    params = {
        "action": "get_user_list",
        "groupid": -2,
        "begin_openid": begin_openid,
        "begin_create_time": begin_create_time,
        "limit": 20,
        "offset": 0,
        "backfoward": 1,
        "token": 95651471,
        "lang": "zh_CN",
        "f": "json",
        "ajax": 1,
        "random": 0.6784559357687705,
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        "HOST": "mp.weixin.qq.com",
        "Cookie": "appmsglist_action_2393828411=card; appmsglist_action_2397322000=card; appmsglist_action_2393291452=card; noticeLoginFlag=1; remember_acct=lzjun567%40gmail.com; pgv_pvid=5422600736; RK=FAIdRbY8Hq; ptcz=f284ef07e30510ca4de096c3a2c609c24239ce649730ff32922337bcbc96c62c; tvfe_boss_uuid=eda94597299f6f90; o_cookie=253421576; pac_uid=1_253421576; _ga=GA1.2.11487159.1587366826; iip=0; pt_sms_phone=158******20; wxuin=03951858983307; openid2ticket_o8uaO6kKiXBtnsUlETb2A4RtJpp4=; UM_distinctid=17944bc50b4c-0cf5c1c972f9ea-3f356b-1fa400-17944bc50b52c2; eas_sid=W1B6e2c1P3o2s825h7L449n642; mm_lang=zh_CN; CNZZDATA1272960370=1269357260-1592369408-https%253A%252F%252Fmp.weixin.qq.com%252F%7C1624334587; CNZZDATA1272425418=1699923129-1592372262-https%253A%252F%252Fmp.weixin.qq.com%252F%7C1624333219; ua_id=8vO2bkcLMNeldl9JAAAAAARMJnerzvqXqrhZO5-2ZL4=; _tc_unionid=28741bd1-95d8-4004-b608-c93597a49688; noticeLoginFlag=1; __root_domain_v=.weixin.qq.com; _qddaz=QD.685431855347487; ptui_loginuin=253421576; openid2ticket_om422jrdTnEAB1r7-zXTmKubGER0=2IFQ/MFb3NNLzCUhgt0XKtzFcJJn6Qcf2SxemWCxzQo=; rewardsn=; wxtokenkey=777; cert=flxHAVShHHKtsHaGR2XZN3VDKjjekUsh; remember_acct=253421576%40qq.com; openid2ticket_ow-uujmHSiUtZWYpm7jDnwkAnt44=/KeBMKI0fyiYdbdwzphNtjjfOxVPcdGjKN+jBKfBCtg=; openid2ticket_oPGiXjhP6KzS5g8fMV3OHuuZkwmg=8gHgxo/ylpS6dCkv7OOeAmDGnZrSMHxE1PLqHS51CEg=; uuid=996152af21663eeaf1716f6d056cd573; rand_info=CAESINIiq2GeUQvsMzW7aoZgT4PyCe/bXGkX6ICCnqvhR4sn; slave_bizuin=3579961954; data_bizuin=3579961954; bizuin=3579961954; data_ticket=SDKlNn7nRnZ6d5Zz9ug6EhgEBY7rYZg6ydm5KdrncdR9rMuP1YmWzwyXqEKW/1J9; slave_sid=VUxRbjBMVWhRTlVUeVh4Z2JHVXM2TDR1RlVmR01kQkZjcVJzUVY3YWRGYTFhYzdaclNyMFBlTURVcFVrTHF1SHRXazZtQmFfVldRek1JTU9sS01HbEZYNUY4enZhVnNqVFBKUlF4TEZnQUJlbm5LdERKOFlPZEozWWFUelg2UzU4MEdHTEtrRHZ6MTVHaGsx; slave_user=gh_a0467681d76f; xid=d6cbe1d708f0d720a5cae0ff84b94e68"
    }
    res = requests.get(url, params=params, headers=headers)
    pprint.pprint(res.json())
    return res.json().get("user_list").get("user_info_list")


with open(
        "公众号关注用户表10_28.csv",
        'w',
        encoding="utf8",
        newline="") as csvfile:
    writer = csv.DictWriter(csvfile, field_order, dialect='myDialect')
    writer.writeheader()

    # 第二页的起始ID
    begin_openid = "oYuJh1WSIFbLZBFCQO6Jz5Bimbxo"
    begin_create_time = 1635423536

    data = execute(begin_openid, begin_create_time)
    while data:
        import time

        time.sleep(1)
        for item in data:
            begin_create_time = user_create_time = item.get("user_create_time")
            begin_openid = item.get("user_openid")
            import datetime

            time = datetime.datetime.fromtimestamp(user_create_time).strftime("'%Y-%m-%d %H:%M:%S'")
            writer.writerow(dict(zip(field_order,
                                     [item.get("user_name").replace("\t", "").replace(",", ""),
                                      time,
                                      item.get("user_head_img")])))

        data = execute(begin_openid, begin_create_time)
