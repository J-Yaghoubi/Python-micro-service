# Python Micro-Service

As you know there is different approach and protocols that can use to make communication over different services in micro-service architecture. In this simple project i want to show how we can do it over gRPC protocol in python.

<br>

## Project info

Suppose we have a factory or any working station with sensors that fetch the amounts of different gases in the air, and we want to monitor this data from a central monitoring office. This is exactly what this project aims to implement.

n the picture below, you can see that we have three sensors sending their data to a queue through **RabbitMQ**. On the other side, the Monitoring Office sends requests over the **gRPC** protocol to the station to fetch the data from the queue.

In a real-world scenario, you can enhance this workflow by integrating additional components such as time-series databases, various communication protocols, etc., in order to meet the project requirements.

![diagram](docs/diagram.png)

<br>

## Run the project

After cloning the project and installing dependencies based on **requirements.txt**, you need to run 3 modules in serrate terminals: Sensors, Station app, and Monitoring app:

```bash
# in first terminal:
cd station
python -m app

# in second terminal:
python -m sensors

# in third terminal:
cd monitoring
python -m app
```

![execute](docs/execute.png)

<br>
