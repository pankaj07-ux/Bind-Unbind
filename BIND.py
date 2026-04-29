import requests
from os import system

def CancEL(access):
	UrL = "https://100067.connect.garena.com/game/account_security/bind:cancel_request"
	PyL = {'app_id': "100067" , 'access_token': access}
	Hr = {'User-Agent': "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)" , 'Connection': "Keep-Alive" , 'Accept-Encoding': "gzip"}
	RsP = requests.post(UrL , data = PyL , headers = Hr)
	if RsP.status_code == 200:
		print('- ResPonsE => ' , RsP.json())
	else:
		print('- No ResPonsE !')

def SEnd(email , access):
	UrL = "https://100067.connect.garena.com/game/account_security/bind:send_otp"	
	PyL = {'app_id': "100067" , 'access_token': access , 'email': email , 'locale': "en_MA"}	
	Hr = {'User-Agent': "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)" , 'Connection': "Keep-Alive" , 'Accept': "application/json" , 'Accept-Encoding': "gzip" , 'Cookie': "datadome=q2ZtAABCjPFEIWeaxYM2YvfxEUPXT_GLUp4gpUOEUPlI9jGXkQLS5uoG_HBUBnJvC0s0CBfHF6h4FUg7mBumLRO1jpLh4um4CbF4ykEKTLv5f27DgR_nkEJcZm_Sj1E~"}	
	RsP = requests.post(UrL , data = PyL , headers = Hr)	
	if RsP.status_code == 200:
		OTp = input('- OtP => ')
		return VeriFy(OTp , email , access)
	else:
		print('- Bad ResPonsE No OtP GeT !')
		
def VeriFy(OTp , email , access):
	UrL = "https://100067.connect.garena.com/game/account_security/bind:verify_otp"	
	PyL = {'app_id': "100067" , 'access_token': access , 'otp': OTp , 'email': email}	
	Hr = {'User-Agent': "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)" , 'Connection': "Keep-Alive" , 'Accept-Encoding': "gzip"}	
	RsP = requests.post(UrL , data = PyL , headers = Hr)	
	if RsP.status_code == 200:
		auth = RsP.json().get("verifier_token")
		print('- AuTh AccEss : ' , auth)
		return Add(auth , access , email)
	
def Add(auth , access , email):
	CancEL(access)
	UrL = "https://100067.connect.garena.com/game/account_security/bind:create_bind_request"	
	PyL = {'app_id': "100067" , 'access_token': access , 'verifier_token': auth , 'secondary_password': "91B4D142823F7D20C5F08DF69122DE43F35F057A988D9619F6D3138485C9A203" , 'email': email}	
	Hr = {'User-Agent': "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)" , 'Connection': "Keep-Alive" , 'Accept-Encoding': "gzip"}	
	RsP = requests.post(UrL , data = PyL , headers = Hr)	
	if RsP.status_code == 200:
		print(RsP.json())
		print(f'- SuccesFuLy AddinG : {email} To AccounT !')

def convert(s):
    d,h=divmod(s,86400);h,m=divmod(h,3600);m,s=divmod(m,60)
    return f"{d} Day {h} Hour {m} Min {s} Sec"

def ChK(access):
    url = "https://100067.connect.garena.com/game/account_security/bind:get_bind_info"
    payload = {'app_id': "100067", 'access_token': access}
    headers = {'User-Agent': "GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)" , 'Connection': "Keep-Alive" , 'Accept-Encoding': "gzip"}
    rsp = requests.get(url, params=payload, headers=headers)
    if rsp.status_code == 200:
        data = rsp.json()
        print(data)
        email = data.get("email", "")
        email_to_be = data.get("email_to_be", "")
        countdown = data.get("request_exec_countdown", 0)
        if email == "" and email_to_be != "":
            print(f"Email : {email_to_be}\nConFirmEd in : {convert(countdown)}")
        elif email != "" and email_to_be == "":
            print(f"Email : {email}\nConFirmEd : Yes Good !")
        elif email == "" and email_to_be == "":
            print(f"No IsTi3ada !")       
    else:
        print("Error => ", rsp.status_code)
        
def GeT_PLaFTroms(t):
 system('clear')
 r = requests.get("https://100067.connect.garena.com/bind/app/platform/info/get",
  params={'access_token': t},
  headers={'User-Agent':"GarenaMSDK/4.0.19P9(Redmi Note 5 ;Android 9;en;US;)","Connection":"Keep-Alive","Accept-Encoding":"gzip","If-Modified-Since":"Sun, 18 May 2025 09:37:03 GMT"})
 if r.status_code not in [200,201]: return print("Failed to fetch.")
 j=r.json();m={3:"Facebook",8:"Gmail",10:"iCloud",5:"VK",11:"Twitter",7:"Huawei"};b,a=j.get("bounded_accounts",[]),j.get("available_platforms",[])
 print("> SEcondary LinKs : <"); l=False
 for x in b:
  try:
   p = x.get('platform')
   u = x.get('uid')
   uinfo = x.get('user_info',{})
   e = uinfo.get('email','')
   n = uinfo.get('nickname','')
   if p in m:
    print(f"\n=> {m[p]} !")
    if e: print(f"- Email : {e}")
    if n: print(f"- Email NamE : {n}")
    print(); l=True
  except: continue
 if not l: print("=> Secondary Links Not Found ! ")
 print("\n> ResPonsE : <\n\n", b)
 for k in m:
  if k not in a:
   print(f"\n> Main Platform => {m[k]} ! <")
   break
   		
def MenU():
    system('clear')
    print('[1] - Add RecovEry EmaiL\n[2] - ChEcK RecovEry EmaiL\n[3] - ChEcK LinKs\n[4] - CanCeL RecovEry EmaiL')
    sH = input('\nChoosE : ')
    if sH in ['1']:
        system('clear')
        SEnd(input('- EnTer EmaiL : ' ) , input('- EnTer AccEss : '))
    elif sH in ['2']:
        system('clear')
        ChK(input('- EnTer AccEss : '))
    elif sH in ['3']:
        system('clear')
        GeT_PLaFTroms(input('- EnTer AccEss : '))
    elif sH in ['4']:
        system('clear')
        CancEL(input('- EnTer AccEss : '))
    else:
        exit('No ChoosinG !')
#SEnd(input(' - EnTer EmaiL : ' ) , input('\n - EnTer AccEss : '))
MenU()