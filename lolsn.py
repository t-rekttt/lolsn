import requests, os, re, subprocess, ctypes, sys, traceback
from random import shuffle
 
def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

s = requests.session()

def getToken():
    #League Client command line query
    command = "WMIC PROCESS WHERE name='LeagueClient.exe' GET commandline"
    #Get WMIC output
    output = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True).stdout.read().decode('utf-8')
    #Parse landing token
    return re.findall(r'--landing-token=(.*?)\s\-?\-?', output)[0]

def useCode(code, accountToken):
    res = s.post('https://bargain.lol.garena.vn/api/enter',
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) LeagueOfLegendsClient/11.15.388.2387 (CEF 74) Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'Token': accountToken,
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9,vi;q=0.8',
            'Via': '1.1 vegur',
            'Referer': 'https://bargain.lol.garena.vn/?token=' + accountToken
        },
        json = {"code": code.strip(),"confirm":True},
        #proxies = {'https': 'http://localhost:8888'},
        #verify = False
    )

    return res.json()

if __name__ == '__main__':
    try:
        #Please leave credits
        print('LOL code tool by T-Rekt - J2TEAM. Get token function contributed by Nomi')
        
        if not isAdmin():
            print('Please run as admin!')
            sys.exit(0)

        #Fill in your code file path (or leave it default)
        codes = open('lolcode.txt', encoding='utf-8').readlines()
        shuffle(codes)

        token = getToken()
        print('Your token: ', token)

        for code in codes:
            try:
                print(code)
                
                res = useCode(code, token)

                print(res)

                if 'error' in res and res['error'] == 'ERROR__ENTER_CODE_AMOUNT_OUT_OF_QUOTA':
                    print('You reached code input limit')
                    break
            except Exception as e:
                print(traceback.format_exc())
    except Exception as e:
        print(traceback.format_exc())
    finally:
        input()
