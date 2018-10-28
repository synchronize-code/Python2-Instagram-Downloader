import requests,re,wget
from random import randint

headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}

HIJAU='\033[0;32m'
MERAH='\033[01;31m'
NORMAL='\033[0m'
CYAN='\033[0;36m'
BIRU='\033[0;34m'
PUTIH='\033[1;37m'

def banner():
	print """ {}
  /$$$$$$                       /$$$$$$                  /$$          
 /$$__  $$                     /$$__  $$                | $$          
| $$  \__/ /$$   /$$ /$$$$$$$ | $$  \__/  /$$$$$$   /$$$$$$$  /$$$$$$ 
|  $$$$$$ | $$  | $$| $$__  $$| $$       /$$__  $$ /$$__  $$ /$$__  $$
 \____  $$| $$  | $$| $$  \ $$| $$      | $$  \ $$| $$  | $$| $$$$$$$$
 /$$  \ $$| $$  | $$| $$  | $$| $$    $$| $$  | $$| $$  | $$| $$_____/
|  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$
 \______/  \____  $$|__/  |__/ \______/  \______/  \_______/ \_______/
           /$$  | $$                                                  
          |  $$$$$$/ Instagram Dowloander By ZahidCode                                                  
           \______/  Thanks Support ZeroByte.id                                                 
	{}""".format(BIRU,CYAN)

def menu():
	print """
1. Download Instagram Photos [Use Link Photo IG]
2. Download All Instagram Photos [Use Username]
	 """	

def singlephoto(link):
	req = requests.get(link,headers=headers).text
	url = re.findall(r'(?<="display_url":")[^",]*',req)
	url = "".join(url)
	wget.download(url)
	print "{} \n[OK] Dowloand Done . . . . . ".format(HIJAU)	 

def manyphoto(username):
	link = "https://www.instagram.com/{}/".format(username)
	req = requests.get(link,headers=headers).text
	url = re.findall(r'(?<="display_url":")[^",]*',req)
	for i in url:
		url = "".join(i)
		wget.download(url)
	print "{} \n[OK] Dowloand Done . . . . . ".format(HIJAU)	
		

if __name__ == '__main__':
	banner()
	menu()
	pilih = input("ZahidCode$ ")
	if pilih == 1:
		url = raw_input('Url [ex:https://www.instagram.com/p/Bm0ObGdlwFP/]: ')
		print "{}[!] Wait . . . . . ".format(MERAH)
		singlephoto(url)
	elif pilih == 2:
		user = raw_input('Username [ex:pria_kacamata98nan]: ')	
		print "{}[!] Wait . . . . . ".format(MERAH)
		manyphoto(user)
	else:
		print "{}Invalid Number".format(PUTIH)
		exit()
		
	


	
		

