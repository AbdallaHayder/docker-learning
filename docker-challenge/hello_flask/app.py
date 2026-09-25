from flask import Flask
import os
import redis

redis_host=os.getenv("REDIS_HOST", "myredis")
redis_port=int(os.getenv("REDIS_PORT", 6379))
app = Flask(__name__)
r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/count')
def count_visit():
    no_visits= r.incr('visits')
    return f'Number of visits:{no_visits}'

if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)