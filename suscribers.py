import redis
import os
import redis

redis_host = os.getenv('REDIS_HOST', 'redis-16535.c16.us-east-1-2.ec2.redns.redis-cloud.com:16535')
redis_port = int(os.getenv('REDIS_PORT', 16535 ))
redis_password = os.getenv('REDIS_PASSWORD', 'yc6e9Ndro0eVxC9g0MdZhUTOvV9YfXpK')
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)


redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)


def subscriptor():
    pubsub = redis_client.pubsub()
    pubsub.subscribe('canal_prueba')
    
    print("Esperando mensajes...")
    for message in pubsub.listen():
        if message['type'] == 'message':
            print(f"Recibido: {message['data']}")

if __name__ == "__main__":
    subscriptor()
