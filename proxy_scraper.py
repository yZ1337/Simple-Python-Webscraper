import requests
from bs4 import BeautifulSoup
import base64
import codecs
import random

def scrape_proxies():
    proxies_file = open('outputs/proxies.txt', 'r')
    proxies_list = [line.strip() for line in proxies_file.readlines()]
    proxies_file.close()
    random.shuffle(proxies_list)

    for proxy in proxies_list:
        ip_port, protocol = proxy.split(',')
        ip, port = ip_port.split(':')
        proxies = {protocol.lower(): f'{protocol}://{ip}:{port}'}
        timeout = 5

        try:
            url1 = 'https://free-proxy-list.net'
            # url2 = 'http://free-proxy.cz/en/'
            url3 = 'https://www.freeproxy.world/'

            values = []

            response1 = requests.get(url1, proxies=proxies, timeout=timeout)
            # response2 = requests.get(url2, proxies=proxies, timeout=timeout)
            response3 = requests.get(url3, proxies=proxies, timeout=timeout)

            soup1 = BeautifulSoup(response1.content, 'html.parser')
            # soup2 = BeautifulSoup(response2.content, 'html.parser')
            soup3 = BeautifulSoup(response3.content, 'html.parser')

            table1 = soup1.find('table', {'class': 'table'})
            # table2 = soup2.find('table', {'id': 'proxy_list'})
            table3 = soup3.find('table', {'class': 'layui-table'})

            rows1 = table1.find_all('tr')
            # rows2 = table2.find_all('tr')
            rows3 = table3.find_all('tr')

            for row in rows1:
                cells = row.find_all('td')
                if len(cells) >= 7:
                    ip_port = ':'.join([cell.text.strip() for cell in cells[0:2]])
                    protocol = cells[6].text.strip()
                    # This is to get the Country and Anonymity if you want to.
                    # country = cells[3].text.strip()
                    # anonymity = cells[4].text.strip()
                    if protocol == "yes":
                        protocol = "https"
                    elif protocol == "no":
                        protocol = "http"
                    values.append(f"{ip_port},{protocol}")

            ### This website does not work on Proxies all the time.
            ### But you can use it for your own good, so that is why it is here :)
            # for row in rows2:
            #     cells = row.find_all('td')
            #     if len(cells) >= 7:
            #         js_code = ''.join([cell.text.strip() for cell in cells[0]])
            #         encoded_string = js_code.split('Base64.decode("')[1].split('")')[0]
            #         decoded_bytes = base64.b64decode(encoded_string)
            #         ip = codecs.decode(decoded_bytes, 'utf-8')
            #         port = cells[1].text.strip()
            #         protocol = cells[2].text.strip()
            #         # This is to get the Country and Anonymity if you want to.
            #         # country = cells[3].text.strip()
            #         # anonymity = cells[6].text.strip()
            #         values.append(f"{ip}:{port},{protocol}")

            for row in rows3:
                cells = row.find_all('td')
                if len(cells) >= 7:
                    ip = cells[0].text.strip()
                    port = cells[1].text.strip()
                    protocol = cells[5].text.strip()
                    # This is to get the Country and Anonymity if you want to.
                    # country = cells[2].text.strip()
                    # anonymity = cells[6].text.strip()
                    values.append(f"{ip}:{port},{protocol}")

            break

        except requests.exceptions.Timeout:
            print(f'\n Request timed out using proxy {proxy}. Skipping it...')
            continue

        except requests.exceptions.RequestException as e:
            print(f'\n Request failed using proxy {proxy}: {e}. Skipping it...')

    return values

