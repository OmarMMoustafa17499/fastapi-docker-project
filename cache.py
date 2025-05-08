import redis
import json
from typing import Optional

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def get_cache(key: str) -> Optional[dict]:
    value = redis_client.get(key)
    if value:
        return json.loads(value)
    return None

def set_cache(key: str, value: dict, ttl: int = 300):
    redis_client.setex(key, ttl, json.dumps(value))pyt
