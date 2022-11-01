import os
import random
import requests
import threading
from pystyle import Write, Colors, Center, Colorate

banner = """
       __                                                   __                   __     
      |  \                                                 |  \                 |  \    
  ____| $$  _______   _______      ______    ______        | $$____    ______  _| $$_   
 /      $$ /       \ /       \    /      \  /      \       | $$    \  /      \|   $$ \  
|  $$$$$$$|  $$$$$$$|  $$$$$$$   |  $$$$$$\|  $$$$$$\      | $$$$$$$\|  $$$$$$\\$$$$$$  
| $$  | $$ \$$    \ | $$         | $$  | $$| $$  | $$      | $$  | $$| $$  | $$ | $$ __ 
| $$__| $$ _\$$$$$$\| $$_____  __| $$__| $$| $$__| $$      | $$__/ $$| $$__/ $$ | $$|  
 \$$    $$|       $$ \$$     \|  \\$$    $$ \$$    $$      | $$    $$ \$$    $$  \$$  $$
  \$$$$$$$ \$$$$$$$   \$$$$$$$ \$$_\$$$$$$$ _\$$$$$$$       \$$$$$$$   \$$$$$$    \$$$$ 
                                 |  \__| $$|  \__| $$                                   
                                  \$$    $$ \$$    $$                                   
                                   \$$$$$$   \$$$$$$                                    

"""


print(Center.XCenter, Colorate.Horizontal(Colors.yellow_to_red, banner, 1))

class stats():
    hits = 0
    failed = 0


threads = Write.Input("Threads -> ", Colors.red_to_purple, interval=0.020)
code = Write.Input("Code to bot -> ", Colors.red_to_purple, interval=0.020)


def click():
    try:
        os.system(f"title dsc.gg/hackinghub ^| Hits: {stats.hits} ^| Failed {stats.failed}")

        proxys = open('proxies.txt', 'r').read().splitlines()
        proxy = random.choice(proxys)
        proxies = {'http': f'http://{proxy}', 'https':f'http://{proxy}'}

        headers = {
            'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        }

        r = requests.get(f"https://dsc.gg/{code}?ref=homepage", headers=headers, proxies=proxies)
        stats.hits += 1
    except:
        stats.failed += 1
while True:
    if threading.active_count() < threads:
        for x in range(threads):
            threading.Thread(target=click).start()
