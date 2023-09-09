from flask import Flask
import time
import redis



app = Flask(__name__)
cache = redis.Redis(host="redis", port=6379)

def get_hit_count():
    retries = 5 
    while True:
        try:
            return cache.incr("hits")
        except redis.exceptions.ConnectionError as exc:
            if retries ==0:
                raise exc
            retries -= 1
            time.sleep(0.5) 


@app.route('/')
def home():
    count = get_hit_count()
    return(f'''
        <div>
            <p> hello, this web site has been consulted {count} </p>
        </div>
           ''')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4800)