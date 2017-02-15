# encoding: utf-8
import requests

__author__ = 'liuzhijun'

if __name__ == '__main__':
    cookies = {
        "wordpress_logged_in_0efdf49af511fd88681529ef8c2e5fbf": "liuzhijun%7C1489451730%7Ch1qqRwDqQsBrt3MdwKXXen1IMV1m31tHXITLutHszlT%7C7c5e634d83279f3cf8d37ec7db76a80d775198593d55a165cf579c9f17308c28"
    }

    data = {"action": "user_login",
            "user_login": "youname",
            "user_pass": "youpassword",
            "remember_me": "1",}
    # redirect_url	http://www.jobbole.com}
    url = "http://python.jobbole.com/wp-admin/admin-ajax.php"
    response = requests.post(url, data)

    for name, value in response.cookies.items():
        print(name, value)

    response = requests.get("http://python.jobbole.com/87305/", cookies=response.cookies)
    print(response.content.decode('utf-8'))
