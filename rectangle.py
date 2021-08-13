import random
from kafka import KafkaConsumer, KafkaProducer, producer

def make_rectangle(a,b):
    rectangle = []
    for i in range(2):
        side = random.randint(a,b)
        rectangle.append(side)
    return rectangle

def rectangle_area(rectangle):
    area = rectangle[0] * rectangle [1]
    return area

def rectangle_perimeter(rectangle):
    perimeter = 2 * (rectangle[0] + rectangle[1])
    return perimeter

def is_rectangle_square(rectangle):
    if rectangle[0] == rectangle[1]:
        return True
    else:
        return False

def use_producer(id):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('rectangle-size',{id: make_rectangle()})

def use_consumer():
    #use rectangle-size topic for info
    #push new data into rectangle-facts topic 
    consumer = KafkaConsumer('rectangle-size', group_id='rectangle-size')
    for msg in consumer:
        tuple_of_facts = [('area', rectangle_area(msg)),('peri', rectangle_perimeter(msg)),('square', is_rectangle_square(msg))]
    

def main():
    for i in range(5):
        use_producer(i)

    use_consumer()

if __name__=='__main__':
    main()

