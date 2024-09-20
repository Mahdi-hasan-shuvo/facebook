from mahdix import *
clear()
logo=mlog()
sec=requests.Session()
coki=input(f'{LI_GREEN}INput Ids Cookie : {LI_WHITE}')
headers = {'authority': 'mbasic.facebook.com',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7','cache-control': 'max-age=0','dpr': '1','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"','sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.117", "Google Chrome";v="118.0.5993.117", "Not=A?Brand";v="99.0.0.0"',
'sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""',
'sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent':W_ueragnt(),'viewport-width': '636',}
def get_group_ID():
    clear()
    print(mlog())
    for i in range(10):
        try:
            get_G_html=sec.get('https://mbasic.facebook.com/groups',headers=headers,cookies={'cookie':coki}).content
            sop=html(get_G_html,'html.parser');find_link=sop.find_all('a')
            for grouplink in find_link:
                link=str(grouplink['href'])
                if 'https://mbasic.facebook.com/groups/' in link:
                    group_id=link.split('/groups/')[1].split('/')[0]
                    leave(group_id)
        except:print(f'{mahdilinx()}\n{LI_GREEN}ALL Group leave Done \n{linex()}');exit()
total=[]
def leave(group_id):
    leave_url=f'https://mbasic.facebook.com/group/leave/?group_id={group_id}'
    req_url=sec.get(leave_url,headers=headers,cookies={'cookie':coki}).content
    sop=html(req_url,'html.parser');find_action=sop.find_all('form')[1]['action']
    learve_url='https://mbasic.facebook.com'+find_action
    req_for_leave=sec.get(learve_url,headers=headers,cookies={'cookie':coki}).content
    total.append(group_id)
    print(f'{LI_YELLOW}[{len(total)}] {LI_GREEN}leave Form Group ID : {LI_WHITE}{group_id}')
get_group_ID()