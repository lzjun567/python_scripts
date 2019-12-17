"""
获取youtube视频下的评论

思路：

基于youtube官方的API来获取, 这里是关于如何初始化配置的文档https://developers.google.com/youtube/v3/getting-started

接口文档：https://developers.google.com/youtube/v3/docs/channelSections/list

视频地址：https://www.youtube.com/watch?v=FWMIPukvdsQ

"""
import requests

#  在 API Console 配置生成
key = "xxxxxx"
# 视频ID
videoId = "FWMIPukvdsQ"

url = f"https://www.googleapis.com/youtube/v3/commentThreads?" \
      f"key={key}&" \
      f"textFormat=plainText&" \
      f"part=snippet&" \
      f"videoId={videoId}&" \
      f"maxResults=100"

proxies = {
    'http': 'socks5://127.0.0.1:1080',
    'https': 'socks5://127.0.0.1:1080',
}


# 获取一下页的凭证


def main():
    nextPageToken = "QURTSl9pMkR0YkxlcE1iOHhlLU1lNi1XWGhzTHdpUmlCN2w1UmJDNlVBaEhnT1dyejVFb3dnVGdWbExRSFNtMVRrNjE1TWVPWC04UVN2VGJrMkhjZ01KVmJpNllrRlVkdUFRWk1yVHp2cW1ZbjVNcXpFc2ZzRlI3ZkRlM3ZPUm1CalZSX1NkaE9qcEY4Tl8yUWRyMmN3"
    while nextPageToken is not None:
        if nextPageToken:
            params = {"pageToken": nextPageToken}
        else:
            params = None
        res = requests.get(url, proxies=proxies, params=params)
        data = res.json()
        import pprint
        nextPageToken = data.get("nextPageToken")
        print(nextPageToken)
        items = data.get("items")
        for item in items:
            comment = item.get("snippet").get("topLevelComment").get("snippet").get("textDisplay")
            print(comment)
        import time
        time.sleep(1)
        print("==================")




if __name__ == '__main__':
    main()
