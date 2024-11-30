import requests
import re
from mahdix import *
clear()
from concurrent.futures import ThreadPoolExecutor

headers = {
    'authority': 'www.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '1',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Google Chrome";v="119.0.6045.160", "Chromium";v="119.0.6045.160", "Not?A_Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    #'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'viewport-width': '658',
}
todaypost=20
create_date=2015
loop=0
def trying(ii):
    global loop
    headers['user-agent']=W_ueragnt()
    response_group = requests.get(f'https://www.facebook.com/groups/{ii}/about',headers=headers)
    #open('group_data.txt','a',encoding='UTF-8').write(str(response_group.text))
    try:
        try:
            today_post=re.search('"number_of_posts_in_last_day":(.\d?),', str(response_group.text)).group(1)
        except:today_post=0
        name_goup=re.search('"Group","name":"(.*?)"', str(response_group.text)).group(1)
        members=re.search('"formatted_count_text":"(.*?)"', str(response_group.text)).group(1).split(' ')[0]
        try:
            created=re.search('"created_time":(.\d+),"', str(response_group.text)).group(1)
            dt_object = datetime.utcfromtimestamp(int(created))
            created_time=dt_object.strftime("%Y")
        except:pass
        if int(today_post) >= int(todaypost)and int(created_time) >= int(create_date):
            loop+=1
            print(f'[{loop}] {LI_WHITE}{ii} |{LI_CYAN} {members} | {LI_YELLOW}{(today_post)} posts today | {LI_WHITE}{dt_object.strftime("%Y")} | {LI_GREEN} {name_goup} ')
            open('group_idx.txt','a',encoding='UTF-8').write(f'{ii}\n')

        else:pass
    except Exception as e :print(e)
def main():
    all_elements=open('group_id.txt','r').read().splitlines()
    print(len(set(all_elements)))
    with ThreadPoolExecutor(max_workers=100) as sub:
        for ii in set(all_elements):
            sub.submit(trying,ii)
main()

