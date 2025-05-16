import requests

headers = {
    'User-Agent': 'BaIII User-agent 007',
    'Accept': 'Shinies',
    'Accept-Language': 'Draconic, Sylvain',
    'Accept-Encoding': 'br, gzip, dzen, sarcasm',
    'Referer': 'where_did_you_come_from.com',
    'DFSHDRFAEHERHRAEH': 'where_did_you_come_from.com',
}

response = requests.get('http://31.130.149.237/user_agent', headers=headers)
