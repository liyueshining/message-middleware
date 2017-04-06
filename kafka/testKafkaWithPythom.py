from pykafka import KafkaClient
client = KafkaClient(hosts="192.168.1.1:9092, 192.168.1.2:9092") # 可接受多个Client这是重点
client.topics  # 查看所有topic
topic = client.topics['my.test'] # 选择一个topic
producer = topic.get_producer()
producer.produce(['test message ' + str(i ** 2) for i in range(4)])
