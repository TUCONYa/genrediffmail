import requests,random,os,sys,random
from threading import Thread
import concurrent.futures

os.system("clear")
headers={'user-agent':'Mozilla/5.0 (Linux; Android 11; Joy 4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36'}
nuoc=['af_ZA', 'ge', 'ar', 'id_ID', 'az', 'it', 'cz', 'ja', 'de', 'ko', 'de_AT', 'lv', 'de_CH', 'nb_NO', 'el', 'en', 'nl', 'en_AU', 'nl_BE', 'pl', 'pt_BR', 'en_CA', 'pt_PT', 'en_GB', 'ro', 'en_IE', 'ru', 'sk', 'en_US', 'sv', 'en_ZA', 'tr', 'es', 'uk', 'es_MX', 'vi', 'fa', 'zh_CN', 'fr', 'zh_TW', 'fr_CA', 'zu_ZA', 'fr_CH']
lc='en_US'
duoi='rediffmail.com'
print ("TOOL ĐÀO REDIFFMAIL V2 \n")
print ("© Bản Quyền By: Nguyễn Hào \n")

HaHa=input('File Lưu mail: ')
os.system("clear")
def daomail():
    while True:
        try:
            luu=''
            data={
    'number':'1',
    'culture': lc,