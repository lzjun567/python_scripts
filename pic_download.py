import requests
from bs4 import BeautifulSoup

url = "https://www.zhihu.com/question/33797069/answer/965775379"

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
    "authority": "www.zhihu.com"
}

response = requests.get(url, headers=headers)

print(response.content)

soup = BeautifulSoup(response.content)

div = soup.find("div", class_="RichContent")
images = div.find_all("img")

i = 0

for image in images:
    # print(image)

    src = image.get("data-actualsrc")
    if src:
        res = requests.get(src, stream=True)
        file_name = str(i) + ".jpg"
        with open(file_name, "wb") as f:
            for chunk in res.iter_content(1024):
                f.write(chunk)

        print(f"{file_name}保存成功")
        i += 1
