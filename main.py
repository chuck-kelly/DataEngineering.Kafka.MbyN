import appscript

def main():

    appscript.app("Terminal").do_script("python3 labs/DataEngineering.Kafka.MbyN/small_area_consumer.py")
    appscript.app("Terminal").do_script("python3 labs/DataEngineering.Kafka.MbyN/small_peri_consumer.py")
    appscript.app("Terminal").do_script("python3 labs/DataEngineering.Kafka.MbyN/small_square_consumer.py")
    appscript.app("Terminal").do_script("python3 labs/DataEngineering.Kafka.MbyN/big_area_consumer.py")
    appscript.app("Terminal").do_script("python3 labs/DataEngineering.Kafka.MbyN/big_peri_consumer.py")
    appscript.app("Terminal").do_script("python3 labs/DataEngineering.Kafka.MbyN/big_square_consumer.py")
    
    appscript.app("Terminal").do_script("python3 labs/DataEngineering.Kafka.MbyN/small_rect_producer.py")
    appscript.app("Terminal").do_script("python3 labs/DataEngineering.Kafka.MbyN/big_rect_producer.py")

if __name__ == "__main__":
    main()
