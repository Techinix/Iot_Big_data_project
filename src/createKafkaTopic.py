from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='grp1')

topic_list = []
topic_list.append(NewTopic(name="Temperature_Topic", num_partitions=1, replication_factor=1))
topic_list.append(NewTopic(name="Humidity_Topic", num_partitions=1, replication_factor=1))
topic_list.append(NewTopic(name="CO2_Topic", num_partitions=1, replication_factor=1))
topic_list.append(NewTopic(name="FireDetection_Topic", num_partitions=1, replication_factor=1))
topic_list.append(NewTopic(name="PersonsCount_Topic", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)
