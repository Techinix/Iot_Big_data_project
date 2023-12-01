# Big Data Project for IoT

This project is part of a school module called IoT Applications. The project aims to establish a connection from sensors to a database and a dashboard, displaying values in real-time and batch mode. The code is primarily composed of Python scripts, with the main file being `mqttConsumer.py`. This file consumes data from sensors and publishes them to Kafka topics. The data from Kafka topics are then inserted into a MongoDB database. Future work includes implementing a dashboard that displays analytics.

## How to Run

To run the demo, follow these steps:

1. Navigate to the Docker folder and run the following command:

    ```
    sudo docker-compose up -d --build
    ```

2. After that, run `createKafkaTopic.py` to create Kafka topics.

3. Run either `mqttTHC.py`, `mqttPersons.py`, or `mqttFire.py` to simulate the sensors.

4. Finally, run `mqttConsumer.py` to execute MQTT consumers, which will send consumed data to Kafka topics. You can access the data through one of the following consumers: `FireConsumer.py`, `HumidityConsumer.py`, `PersonsConsumer.py`, `TemperatureConsumer.py`, or `CO2Consumer.py`. These consumers will listen to topics and save received values into MongoDB. Make sure to create a MongoDB database named `iotbigdataproject` and collections under the names `fire`, `humidity`, and so on.

A dashboard will be implemented in the future to display analytics.
