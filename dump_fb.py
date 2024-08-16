from mahdix import *
import os,sys,requests
import requests, random, json, hashlib, uuid, time
from concurrent.futures import ThreadPoolExecutor as threads
logo=mahdi_logo
clear()
def generate_token(email,password):
    r    = requests.Session()
    head = {'Host':'b-graph.facebook.com','X-Fb-Connection-Quality':'EXCELLENT','Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32','User-Agent':'Dalvik/2.1.0 (Linux; U; Android 7.1.2; RMX3740 Build/QP1A.190711.020) [FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/in_ID;FBBV/480086274;FBCR/Corporation Tbk;FBMF/realme;FBBD/realme;FBDV/RMX3740;FBSV/7.1.2;FBCA/x86:armeabi-v7a;FBDM/{density=1.0,width=540,height=960};FB_FW/1;FBRV/483172840;]','X-Tigon-Is-Retry':'false','X-Fb-Friendly-Name':'authenticate','X-Fb-Connection-Bandwidth':str(random.randrange(70000000,80000000)),'Zero-Rated':'0','X-Fb-Net-Hni':str(random.randrange(50000,60000)),'X-Fb-Sim-Hni':str(random.randrange(50000,60000)),'X-Fb-Request-Analytics-Tags':'{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}','Content-Type':'application/x-www-form-urlencoded','X-Fb-Connection-Type':'WIFI','X-Fb-Device-Group':str(random.randrange(4700,5000)),'Priority':'u=3,i','Accept-Encoding':'gzip, deflate','X-Fb-Http-Engine':'Liger','X-Fb-Client-Ip':'true','X-Fb-Server-Cluster':'true','Content-Length':str(random.randrange(1500,2000))}
    data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':email,'password':'#PWD_FB4A:0:{}:{}'.format(str(time.time())[:10], password),'generate_analytics_claim':'1','community_id':'','linked_guest_account_userid':'','cpl':True,'try_num':'1','family_device_id':str(uuid.uuid4()),'secure_family_device_id':str(uuid.uuid4()),'credentials_type':'password','account_switcher_uids':[],'fb4a_shared_phone_cpl_experiment':'fb4a_shared_phone_nonce_cpl_at_risk_v3','fb4a_shared_phone_cpl_group':'enable_v3_at_risk','enroll_misauth':False,'generate_session_cookies':'1','error_detail_type':'button_with_disabled','source':'login','machine_id':str(''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(24)])),'jazoest':str(random.randrange(22000,23000)),'meta_inf_fbmeta':'V2_UNTAGGED','advertiser_id':str(uuid.uuid4()),'encrypted_msisdn':'','currently_logged_in_userid':'0','locale':'id_ID','client_country_code':'ID','fb_api_req_friendly_name':'authenticate','fb_api_caller_class':'Fb4aAuthHandler','api_key':'882a8490361da98702bf97a021ddc14d','sig':str(hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:32]),'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
    pos  = r.post('https://b-graph.facebook.com/auth/login', data=data, headers=head).json()
    if ('session_key' in str(pos)) and ('access_token' in str(pos)):
        uid    = pos['uid']
        token  = pos['access_token']
        cookie = ''.join(['{}={};'.format(i['name'],i['value']) for i in pos['session_cookies']])

        print(mahdilinx())
        print(f'{LI_GREEN}Success Login!')
        return token
    else:
        print('Failed Login!')
        slps(5)


def main():
    clear()
    print(logo)
    print(f'{LI_WHITE}[1] {LI_GREEN}Dump From Friendlist')
    print(f'{LI_WHITE}[2] {LI_GREEN}Dump From Group')
    print(f'{LI_WHITE}[3] {LI_GREEN}Dump From Comment')
    print(f'{LI_WHITE}[4] {LI_GREEN}Dump From Reaction')
    chouse=input(f'====>>{LI_CYAN}')




all_ID=[]


#-------[using user name And password Dumping public Friendlistusing user name And password Dumping public Friendlist]--------------------
def friend_list():
    clear()
    all_ID.clear()
    print(logo)
    print('  Login a facebook ID ')
    email=input(f'{LI_BLUE}Input Email : {LI_GREEN}')
    print(mahdilinx())
    pasword=input(f'{LI_BLUE}Input Password : {LI_GREEN}')
    token=generate_token(email,pasword)
    if token:
        clear()
        print(f'Your Token : {token}')
        print(mahdilinx())
        file_name=input('Save as : ')
        clear()
        limite_ID=int(input('limite Of ID : '))
        for i in range(limite_ID):
            UID_id=input(f'[{i}] Input ID : {LI_GREEN}')
            all_ID.append(UID_id)
        with threads(max_workers=len(all_ID)) as submite:
            for id in all_ID:
                submite.submit(DumpFriendlist,id, token,file_name=file_name)
def DumpFriendlist(id:str, token:str,file_name='Dump.txt',cursor=None):
    r    = requests.Session()
    var  = {"friends_paginating_at_stream_use_customized_batch":False,"profile_image_size":60,"friends_paginating_first":20,"profile_id":id,"paginationPK":id,"friends_paginating_after_cursor":cursor}
    data = {'access_token':token,'method':'post','pretty':False,'format':'json','server_timestamps':True,'locale':'user','purpose':'fetch','fb_api_req_friendly_name':'FriendListContentQuery_At_Connection_Pagination_User_friends_paginating','fb_api_caller_class':'ConnectionManager','client_doc_id':'24605340972600723188569773708','fb_api_client_context':json.dumps({"load_next_page_counter":1,"client_connection_size":20}),'variables':json.dumps(var),'fb_api_analytics_tags':["At_Connection","GraphServices"],'client_trace_id':str(uuid.uuid4())}
    pos  = r.post('https://graph.facebook.com/graphql', data=data).json()
    try:
        for i in pos['data']['node']['friends']['edges']:
            try:
                id, name = i['node']['id'], i['node']['name']
                open(file_name,'a',encoding='utf=8').write(f'{id}|{name}\n')
                print('{}|{}'.format(id, name))
            except Exception: continue
        if pos['data']['node']['friends']['page_info']['has_next_page']:
            next_cursor = pos['data']['node']['friends']['page_info']['end_cursor']
            DumpFriendlist(id=id, token=token,cursor=next_cursor,file_name=file_name)
    except Exception: print(pos)
