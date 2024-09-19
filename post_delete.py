from mahdix import *
import re,requests,os,sys
from concurrent.futures import ThreadPoolExecutor

sec=requests.Session()
clear()

hedars_golba = {
'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7','cache-control': 'max-age=0','dpr': '1','sec-ch-prefers-color-scheme': 'light',
'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.117", "Google Chrome";v="118.0.5993.117", "Not=A?Brand";v="99.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent':W_ueragnt(),'viewport-width': '455',
}

hedars_grapql={ 'authority': 'www.facebook.com',
'accept': '*/*','accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7','content-type': 'application/x-www-form-urlencoded','dpr': '1','origin': 'https://www.facebook.com','referer': 'https://www.facebook.com/groups/1944912799181203/permalink/2045697582436057/?mibextid=oMANbw','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"','sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.117", "Google Chrome";v="118.0.5993.117", "Not=A?Brand";v="99.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin','user-agent': W_ueragnt(),'viewport-width': '752','x-asbd-id': '129477','x-fb-friendly-name': 'useGroupRemovePostAsAdminMutation','x-fb-lsd': 'RiDxK9cbLXTaMyAzkOl9Gx',}

os.system("xdg-open https://www.facebook.com/ma4D1")
logo=("""\033[1;33m  
╔═════════════════════════════════════════════════╗\033[1;32m
║             WELCOME TO FB-BOOT(G.P.D)           ║\033[1;33m
║═════════════════════════════════════════════════║\033[1;33m                     
║\033[1;37m##     ##    ###    ##     ## ########  ####     ║
║\033[1;92m###   ###   ## ##   ##     ## ##     ##  ##      ║
║\033[1;93m#### ####  ##   ##  ##     ## ##     ##  ##      ║
║\033[1;91m## ### ## ##     ## ######### ##     ##  ##      ║
║\033[1;92m##     ## ######### ##     ## ##     ##  ##      ║
║\033[1;93m##     ## ##     ## ##     ## ##     ##  ##      ║
║\033[1;33m##     ## ##     ## ##     ## ########  ####     ║ 
║                                   \033[1;37mVERSION : 1.2 ║
║╭───────────\033[1;91m[POWERED BY MAHDI HASAN ]\033[1;33m────────────║
│ ╭──────────────────────────────────────────────╮│
│ │ [A] AUTHOR   : \033[1;37mMAHDI HASAN SHUVO             ││
│ │ \033[1;32m[F] FACEBOOK : m.me/bk4human                 ││
│ │ \033[1;32m[G]GITHUB    : SHUVO-BBHH                    ││ 
│ │ \033[1;37m[W] WHATSAPP : +8801616406924                ││
│ ╰─\033[1;33m─────────────────────────────────────────────╯│
╰\033[1;33m─────────────────────────────────────────────────╯\033[1;32m""")
print(logo)
ck=input(f'{LI_WHITE}Input my facebook id link : {LI_YELLOW}')
if 'bk4human'  in ck:
    pass
else:
    os.system("xdg-open https://www.facebook.com/bk4human")
    print(f'{LI_CYAN}Wrong input')
    print(f'{LI_WHITE}go to my facebook id and copy my id link and past is')
    exit()
clear()
print(logo)
coki=input(f'{LI_WHITE}Input Admin ids Cookie : {LI_GREEN}')
print(mahdilinx())
group_id=input(f'{LI_GREEN}Group Uid : {LI_YELLOW}')

def infor():
    headers_mbasic = {'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7',
    'cache-control': 'max-age=0','dpr': '1','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.117", "Google Chrome";v="118.0.5993.117", "Not=A?Brand";v="99.0.0.0"','sec-ch-ua-mobile': '?0','sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"','sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': W_ueragnt(),'viewport-width': '708',}
    url='https://mbasic.facebook.com/profile.php'
    name_profile=html(sec.get(url,cookies={'cookie':coki},headers=headers_mbasic).text, 'html.parser').find('title').text
    name_group=html(sec.get(f'https://mbasic.facebook.com/groups/{group_id}',cookies={'cookie':coki},headers=headers_mbasic).text, 'html.parser').find('title').text
    return (name_profile,name_group)
all_link=[]
def my_group():
    try:
        headers = {
            'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7','cache-control': 'max-age=0','dpr': '1','sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"','sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.117", "Google Chrome";v="118.0.5993.117", "Not=A?Brand";v="99.0.0.0"','sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""','sec-ch-ua-platform': '"Windows"','sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1',
            'user-agent': W_ueragnt(),'viewport-width': '658',
        }
        responce = requests.get(f'https://www.facebook.com/groups/{group_id}', cookies={'cookie':coki}, headers=headers).text
        pattern = fr'"https:\\\/\\\/www\.facebook\.com\\\/groups\\\/{group_id}\\\/posts\\\/\d+\\\/"'
        matches = re.findall(pattern, responce)
        for match in matches:
            post_linkx=str(match.replace('\\','')).replace('"','')
            all_link.append(post_linkx)
            #delete_post(post_linkx)
        with ThreadPoolExecutor(max_workers=len(set(all_link))) as ex:
            for post_link in set(all_link): 
                ex.submit(delete_post,post_link)
                #delete_post(post_link)
            all_link.clear()
    except:print('wrong Cookei');pass

sucessa=[]
fail=[]
def delete_post(post_link):
    try:
        response = sec.get(post_link, cookies={'cookie':coki}, headers=hedars_golba)
        storyID=re.search('"storyID":"(.*?)"',str(response.text)).group(1)
        actorID=re.search('"actorID":"(.*?)"',str(response.text)).group(1)
        owning_profile_id=re.search('"owning_profile_id":"(.*?)"',str(response.text)).group(1)
        data = {
        'av': actorID,
        'dpr':re.search('"pr":(.*?),',str(response.text)).group(1),
        'fb_dtsg':re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(response.text)).group(1),
        'jazoest':re.search('&jazoest=(.*?)"',str(response.text)).group(1),
        'lsd':re.search('"LSD",\[\],{"token":"(.*?)"}',str(response.text)).group(1),
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'useGroupRemovePostAsAdminMutation',
        'variables': '{"input":{"admin_notes":"","group_id":"%s","selected_rules":[],"send_warning":false,"share_feedback":false,"source":"group_mall","story_id":"%s","actor_id":"%s","client_mutation_id":"7"},"profileID":"%s"}'%(group_id,storyID,actorID,owning_profile_id),
        'server_timestamps': 'true',
        'doc_id': '6790245574365368',
        }
        response = requests.post('https://www.facebook.com/api/graphql/', cookies={'cookie':coki}, headers=hedars_grapql,data=data)
        #print(f"\r{LI_GREEN}Post Delete Done : {LI_WHITE}{post_link}")
        print(f"\r\r{LI_GREEN}Deleted Post ID : {LI_WHITE}{post_link.split('/posts/')[1].split('/')[0]}")
        sucessa.append(actorID)
    except:
        fail.append('actorID')
        pass   
    
    sys.stdout.write(f'\r\r{LI_GREEN}[Deleted] {LI_RED}: {LI_WHITE}%s  {LI_YELLOW}[Faield] : {LI_RED}%s'%(len(sucessa),len(fail))),
    sys.stdout.flush()
clear()
print(logo)
print(f'{LI_WHITE}Terget Group : {LI_CYAN}{group_id}')
print(f'{LI_WHITE}GROUP NAME  :{LI_YELLOW} {infor()[1]}')
print(f'{LI_WHITE}ADMIN NAME  :{LI_GREEN} {infor()[0]}')
print(mahdilinx())
with ThreadPoolExecutor(max_workers=3) as ex:
    while True:
        ex.submit(my_group)
        #my_group()