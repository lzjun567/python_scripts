"""
获取youtube视频下的评论
思路：
基于youtube官方的API来获取, 这里是关于如何初始化配置的文档 https://developers.google.com/youtube/v3/getting-started

评论接口文档：https://developers.google.com/youtube/v3/docs/channelSections/list

任意视频地址：https://www.youtube.com/watch?v=FWMIPukvdsQ
"""
import requests

#  在 API Console 配置生成
key = "AIzaSyCtJuC7oMed0xxZYPcid913vPxOnl72sHg"
# 视频ID
videoId = "FWMIPukvdsQ"

url = f"https://www.googleapis.com/youtube/v3/commentThreads?" \
      f"key={key}&" \
      f"textFormat=plainText&" \
      f"part=snippet&" \
      f"videoId={videoId}&" \
      f"maxResults=100"  # 分页参数

proxies = {
    'http': 'socks5://127.0.0.1:1080',
    'https': 'socks5://127.0.0.1:1080',
}


def spider(next_page_token):
    if next_page_token:
        params = {"pageToken": next_page_token}
    else:
        params = None
    res = requests.get(url, proxies=proxies, params=params)
    data = res.json()
    import pprint
    next_page_token = data.get("nextPageToken")

    items = data.get("items")
    for item in items:
        comment = item.get("snippet").get("topLevelComment").get("snippet").get("textDisplay")
        print(comment)
    return next_page_token


def run():
    next_page_token = spider(None)

    while next_page_token:
        try:
            print(next_page_token)
            next_page_token = spider(next_page_token)
            import time
            time.sleep(1)
        except Exception as e:
            # 请求超时重试
            import traceback
            print(next_page_token)
            print(traceback.format_exc())


if __name__ == '__main__':
    run()
