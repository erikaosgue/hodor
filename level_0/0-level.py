#!/usr/bin/python3
import requests
"""
    A program that votes 1024 times for your id
    in the url specified
"""


def main():

    url = 'http://158.69.76.135/level0.php'
    my_data = {'id': '1476', 'holdthedoor': 'pizza'}
    for i in range(1024):
        requests.post(url, data=my_data)

if __name__ == "__main__":
    main()
