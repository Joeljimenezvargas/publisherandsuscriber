import redis
import time
import os


redis_host = os.getenv('REDIS_HOST', 'redis-16535.c16.us-east-1-2.ec2.redns.redis-cloud.com:16535')
redis_port = int(os.getenv('REDIS_PORT', 16535 ))
redis_password = os.getenv('REDIS_PASSWORD', 'yc6e9Ndro0eVxC9g0MdZhUTOvV9YfXpK')
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)


def publicar():
    while True:
        message = input("Introduce un mensaje para publicar: ")
        redis_client.publish('canal_prueba', message)
        print(f"Publicado: {message}")

if __name__ == "__main__":
    publicar()
