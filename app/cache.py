import redis
import time

r = redis.Redis(host='localhost', port=6379, db=0)

def cache_response(key, value, timeout=300):
    r.setex(key, timeout, value)

def get_cached_response(key):
    return r.get(key)

def log_inference_time(user_id, start_time):
    end_time = time.time()
    r.lpush(f'{user_id}_inference_time', end_time - start_time)
