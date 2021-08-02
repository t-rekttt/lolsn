import requests, os, re, subprocess, ctypes, sys, traceback, time
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

def getProfile(accountToken):
    res = s.get('https://bargain.lol.garena.vn/api/profile',
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
        }
    )

    return res.json()

def redeem(accountToken):
    res = s.post('https://bargain.lol.garena.vn/api/redeem',
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
        json = {"type":0,"is_consumption":False}
    )

    return res.json()

if __name__ == '__main__':
    try:
        #Please leave credits
        print('LOL code tool by T-Rekt - J2TEAM. Get token function contributed by Nomi')
        
        if not isAdmin():
            print('Please run as admin!')
            sys.exit(0)

        while True:
            try:
                token = getToken()
                print('Your token:', token)
                
                thanthien = getProfile(token)['invitation_reward']['progress']

                print('Your reward score:', thanthien)

                if thanthien == 100:
                    print('Reward score reached 100, redeeming')

                    redeemResult = redeem(token)

                    if 'reward' in redeemResult:
                        print('Reward: ', redeem['reward']['name'])
                    else:
                        print('Redeem error', redeemResult)

                print('Sleeping 30 seconds')
                time.sleep(30)
            except Exception as e:
                print(traceback.format_exc())
    except Exception as e:
        print(traceback.format_exc())
    finally:
        input()