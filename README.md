# Smart Vitals Streamer

This project generates realistic human vitals and streams them to a Kafka topic. It also includes anomaly injection for heart rate and breaths per minute.

## Prerequisites

*   Docker
*   Kafka

## Usage

1.  Clone the repository:

    ```bash
    git clone https://github.com/Gautam0610/smart-vitals-streamer.git
    cd smart-vitals-streamer
    ```

2.  Build the Docker image:

    ```bash
    docker build -t smart-vitals-streamer .
    ```

3.  Run the Docker container (replace `localhost:9092` and `vitals` with your Kafka broker and topic):

    ```bash
    docker run -e KAFKA_BROKER=localhost:9092 -e KAFKA_TOPIC=vitals smart-vitals-streamer
    ```

## Configuration

The following environment variables can be used to configure the project:

*   `KAFKA_BROKER`:  The Kafka broker address (default: `localhost:9092`)
*   `KAFKA_TOPIC`:  The Kafka topic to send vitals to (default: `vitals`)
