import redis
from datetime import datetime

r = redis.Redis(
    host='172.28.128.13',
    port=6379
)

current_time=datetime.now()

r.set('last_updated_at', current_time)
output = r.get('last_updated_at')

print('last_updated_at: {}', output)