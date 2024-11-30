import os
try:
    from mahdix import *
    import re,requests
    from bs4 import BeautifulSoup as bs
except:
    os.system('pip install mahdix')
all_link=[]
clear()
logo=mahdi_logo

headers_mbasic = {
'viewport-width': '737', 
'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7',
'cache-control': 'max-age=0','dpr': '1.1','sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"','sec-ch-ua-full-version-list': '"Google Chrome";v="119.0.6045.160", "Chromium";v="119.0.6045.160", "Not?A_Brand";v="24.0.0.0"','sec-ch-ua-mobile': '?0',
'sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"',
'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',

}

def main():
    clear()
    print(logo)
    print(mahdilinx())
    coki=input(f'{LI_CYAN}Cookies : {LI_WHITE}')
    headers_mbasic['cookie']=coki
    print(mahdilinx())
    print(f'{LI_YELLOW}use multipul use [{LI_GREEN}/ {LI_YELLOW}]')
    print(linex())
    name_of_group=input(f'{LI_GREEN}inpute Name :{LI_WHITE} ').split('/')
    print(mahdilinx())
    save_as=input(f'{LI_CYAN}save as : {LI_WHITE}')
    print(mahdilinx())
    limeite_page=input(f'Input Page limite : ')
    clear()
    print(logo)
    print(mahdilinx())
    for group_name in name_of_group:
        headers_mbasic['user-agent']=W_ueragnt()
        params = {
        'q': group_name,}
    response = requests.get('https://mbasic.facebook.com/search/groups/', params=params,headers=headers_mbasic).text
    sop=bs(response,'html.parser').find('a',string='See more results')['href']
    all_link.append(sop)
    for ii in range(int(limeite_page)):
        req_link=all_link[-1]
        respon=requests.get(req_link,params=params,headers=headers_mbasic).text
        sop=bs(respon,'html.parser').find('a',string='See more results')['href']
        all_link.append(sop)
        pattern = '"https://mbasic.facebook.com/groups/(.*?)/'
        all_elements = re.findall(pattern, respon)
        for ids in set(all_elements):
            open(save_as,'a',encoding='UTF-8').write(f'{ids}\n')
            print(ids)
        print(mahdilinx())
main()
