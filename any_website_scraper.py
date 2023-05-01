import requests
from bs4 import BeautifulSoup
import random


def any_website_scraper(website):
    url = 'https://' + website
    proxies_file = open('outputs/proxies.txt', 'r')
    proxies_list = [line.strip() for line in proxies_file.readlines()]
    proxies_file.close()
    random.shuffle(proxies_list)

    for proxy in proxies_list:
        ip_port, protocol = proxy.split(',')
        ip, port = ip_port.split(':')
        proxies = {protocol.lower(): f'{protocol}://{ip}:{port}'}

        try:
            response = requests.get(url, proxies=proxies)

            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            break

        except requests.exceptions.RequestException as e:
            print(f'\n Request failed using proxy {proxy}: {e}')

    return str(soup)

