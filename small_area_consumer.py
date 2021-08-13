from kafka import KafkaConsumer, TopicPartition
from rectangle import rectangle_area, rectangle_perimeter, is_rectangle_square
import ast

if __name__ == "__main__":
    consumer = KafkaConsumer('small-rectangle-size')
    for msg in consumer:
        rectangle = ast.literal_eval(msg.value.decode("utf-8"))
        print(f"The small Recangle {rectangle} has an area of {rectangle_area(rectangle)}")