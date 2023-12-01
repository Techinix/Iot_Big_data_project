# Big Data Project for IoT

This project is part of a school module called IoT Applications, focusing on connecting sensors to a database and a dashboard for real-time and batch-mode data visualization. The codebase predominantly consists of Python scripts, with the pivotal `mqttConsumer.py` file responsible for consuming sensor data and publishing it to Kafka topics. Subsequently, the data from Kafka topics is stored in a MongoDB database. Ongoing efforts include the development of a dashboard to showcase analytics.

## How to Run

To run the demonstration, follow these steps:

1. Begin by navigating to the Docker folder and executing the following command:

    ```bash
    sudo docker-compose up -d --build
    ```

2. After the Docker setup, proceed to the `src` folder:

    ```bash
    cd src
    ```

3. Within the `src` directory, run `createKafkaTopic.py` to initialize the required Kafka topics.

4. Simulate sensor data by running either `mqttTHC.py`, `mqttPersons.py`, or `mqttFire.py`.

5. Execute `mqttConsumer.py` to activate MQTT consumers, responsible for transmitting consumed data to Kafka topics. Access the data through dedicated consumers such as `FireConsumer.py`, `HumidityConsumer.py`, `PersonsConsumer.py`, `TemperatureConsumer.py`, or `CO2Consumer.py`. These consumers listen to topics and store received values in a MongoDB database. Ensure to create a MongoDB database named `iotbigdataproject` with collections under names like `fire`, `humidity`, and others.

A dashboard, intended to present comprehensive analytics, is part of future development.
