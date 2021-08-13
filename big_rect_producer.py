from kafka import KafkaProducer
from rectangle import make_rectangle
from time import sleep

if __name__=="__main__":
    
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    id = 0
    for _ in range(20):
        rectangle = bytes(str(make_rectangle(1,20)), encoding = 'utf-8')
        producer.send('big-rectangle-size',key = bytes(str(id), encoding = 'utf-8'), value = rectangle)

        print(f'added the big rectangle of id {id} and size {rectangle}')
        id += 1
        sleep(1)