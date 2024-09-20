import os
try:
    from mahdix import *
except:
    os.system('pip install mahdix')
logo=mahdi_logo   # this Is logo
clear() # clear terminal
print(logo)
coki=input(f'{LI_GREEN}Input Cookes : {LI_WHITE}')  # Id Cookie
print(mahdilinx())
group_id=input(f'{LI_WHITE}Input Group Id {LI_YELLOW} : ')   # Group Id wich group are inviting
url=f'https://mbasic.facebook.com/groups/members/search/?group_id={group_id}'
headers = {'authority': 'mbasic.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7','cache-control': 'max-age=0','dpr': '1.1','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.71", "Google Chrome";v="120.0.6099.71"',
'sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1',
'user-agent': W_ueragnt(),'viewport-width': '657',
}
clear() # clear terminal
print(logo)
def _():#
    while True:
        try:
            headers['cookie']=coki
            sop=html_req(url,Headers=headers).find_all('form')[1] # send Html get requests use mahdix
            inps=sop.find_all("input")
            data={} # data of post requests
            for i in inps:
                try:data[i["name"]]=i["value"]
                except:pass
            acton_url='https://mbasic.facebook.com/'+sop['action']  # Post requests url
            addees_count = len([key for key in data.keys() if key.startswith('addees[')])
            if 2 > int(addees_count):break
            sop2=html_req(acton_url,Headers=headers,Data=data,Cookie={'cookie':coki}) # send Html Pos requests use mahdix
            if 'account is' in sop2.text:
                print(f'{LI_RED}Your account is restricted right now');break
            else:
                print(f'{LI_GREEN}Invited Done {LI_WHITE}{addees_count}')
        except Exception as e:print(e)

_()