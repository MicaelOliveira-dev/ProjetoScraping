import json
import requests
from bs4 import BeautifulSoup


class Scraping:
    def main(self):
        try:
            response = self.get_page()
            html = self.get_html(response)
            proxies = self.get_proxies(html)
            self.process_proxies(proxies)
            self.save_proxies(proxies)
        except Exception:
            raise Exception

    def get_page(self):
        try:
            headers = {
                'authority': 'www.freeproxylists.net',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                          '*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9,pt;q=0.8',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/114.0.0.0 Safari/537.36',
            }

            response = requests.get('https://www.freeproxylists.net/', headers=headers)
            return response
        except Exception:
            raise Exception

    def get_html(self, response):
        try:
            html = BeautifulSoup(response.content, 'html.parser')
            return html
        except Exception:
            raise Exception

    def get_proxies(self, html):
        try:
            proxies = []
            table = html.find('table', {'class': 'DataGrid'})
            if table:
                rows = table.find_all('tr')
                for row in rows[1:]:
                    cells = row.find_all('td')
                    if len(cells) >= 9:
                        ip = cells[1].text.strip()
                        port = cells[2].text.strip()
                        protocol = cells[4].text.strip()
                        country = cells[5].text.strip()
                        uptime = cells[7].text.strip()
                        proxy = {
                            'ip': ip,
                            'port': port,
                            'protocol': protocol,
                            'country': country,
                            'uptime': uptime
                        }
                        proxies.append(proxy)
                return proxies
        except Exception:
            raise Exception

    def process_proxies(self, proxies):
        try:
            for proxy in proxies:
                return proxy
        except Exception:
            raise Exception

    def save_proxies(self, proxies):
        try:
            with open('/app/proxies.json', 'w') as file:
                json.dump(proxies, file, indent=4)
        except Exception:
            raise Exception
