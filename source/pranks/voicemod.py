import requests
from source.utils.emailformatter import getmail

def voicemod():
    headers = {
    'authority': 'api.voicemod.net',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': '_vwo_uuid_v2=DFA347C667FD4A568C6950ADD71EE353A|d24caf96ef53ce5c574d673b50eccf36; vm_device_id=74a807b1-3e4f-476c-933d-1df5e98fc73c; vm_initial_url=aHR0cHM6Ly93d3cudm9pY2Vtb2QubmV0Lw==; vm_initial_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8=; _vwo_uuid=DFA347C667FD4A568C6950ADD71EE353A; _vwo_sn=0%3A1%3A%3A%3A1; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_ds=3%3Aa_0%2Ct_0%3A0%241706394899%3A92.95305096%3A%3A%3A6_0%3A1; _gcl_au=1.1.478046286.1706394901; _rdt_uuid=1706394901435.5856cbfd-6e73-440e-bee4-6b6a8722d77d; vm_mparticle_device_id=a1367e4a-c64e-4bac-2954-7b41dc728adb; _hjSessionUser_3329268=eyJpZCI6ImQ4NDE0ZTgwLWQ1NDctNTNmZS1hOTRjLTQ1ZTc4ODcyZGYyOSIsImNyZWF0ZWQiOjE3MDYzOTQ5MDE3MTMsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_3329268=eyJpZCI6IjQ5YTJiM2IyLTMzNGUtNDY2Yi1iYjA0LWJkYzlhNDY5YzQyMyIsImMiOjE3MDYzOTQ5MDE3MTcsInMiOjEsInIiOjAsInNiIjoxLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; no_signup_xp={%22treatment%22:%22ab126_download_no_signup__default%22}; _ga=GA1.1.957275418.1706394903; _ga_GLK7CYZ4FD=GS1.1.1706394903.1.0.1706394907.0.0.0; mprtcl-v4_9F04B7AE={\'gs\':{\'ie\':1|\'dt\':\'us1-10e1620394b1c644896bc3a9e5775cf3\'|\'cgid\':\'c497fd54-bd28-49bd-2a37-cea07908817d\'|\'das\':\'a1367e4a-c64e-4bac-2954-7b41dc728adb\'|\'csm\':\'WyIzMDQzMzU2MjUwNDc5MzMyOTkzIl0=\'|\'sid\':\'178E6E2F-3B60-40BC-B1DD-F05071190584\'|\'les\':1706394908507|\'ssd\':1706394901485}|\'l\':0|\'3043356250479332993\':{\'fst\':1706394901793|\'ua\':\'eyJXZWJfQUJfVGVzdF9TcGxpdCI6WyJhYjEyNl9kb3dubG9hZF9ub19zaWdudXBfX2RlZmF1bHQiXX0=\'}|\'cu\':\'3043356250479332993\'}',
    'origin': 'https://account.voicemod.net',
    'referer': 'https://account.voicemod.net/',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Opera GX";v="106"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0'
    }

    while True:
        useemail = getmail()

        data = {
            'email': useemail
        }

        response = requests.post('https://api.voicemod.net/v1/accounts/users/send-verification-code', headers=headers, json=data)
        if response.status_code == 202:
            print("(Voicemod) Account created successfully - Email: {}".format(useemail))
        else:
            if response.status_code != 503:
                print("(Voicemod) Account creation failed - Status code: {}".format(response.status_code))