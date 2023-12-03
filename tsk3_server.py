from flask import Flask, request, jsonify
import time as time
import bcrypt

"""
В данном случае мною решена проблема CWE-799: Improper Control of Interaction Frequency. Это стало возможным благодаря 
счётчику попыток и блокировке попыток на 2 минуты. 

Еще мною был использован хороший алгоритм хэширования, что решает проблемы #CWE-327: Use of a Broken or Risky 
Cryptographic Algorithm и #CWE-328: Use of Weak Hash.
"""

app = Flask("server")

users = {
    'mikhail': {
        "password": bcrypt.hashpw(b'password', bcrypt.gensalt()),
        "last_login":0,
        "count":0
    }
}

@app.route('/')
def login():
    username = request.args.get('username')
    password = request.args.get('password')
    time_moment_now = time.time()

    if username in users:
        us_password = users[username]["password"]
        us_try_auth = users[username]["count"]
        us_last_login = users[username]["last_login"]

        if time_moment_now - users[username]["last_login"] >= 120:
            users[username]["last_login"] = 0
            users[username]["count"] = 0

        if us_try_auth >= 3:
            time_remaining = max(0, int(120 - (time_moment_now - us_last_login)))
            return jsonify({"msg": f"Превышено количество попыток, повторите через {time_remaining} секунд."}), 404

        if bcrypt.checkpw(password.encode(), us_password):
            users[username]["count"] = 0
            users[username]["last_login"] = time_moment_now
            return jsonify({"msg": "Успешный вход"}), 200
        else:
            users[username]["last_login"] = time_moment_now
            users[username]["count"] += 1
            return jsonify({"msg": "Неправильный логин или пароль"}), 404
    else:
        return jsonify({"msg": "Проверьте логин и пароль"}), 404

if __name__ == '__main__':
    app.run()
