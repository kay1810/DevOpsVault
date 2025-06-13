## Docker Architecture

Docker makes use of a client-server architecture. The Docker client talk with the docker daemon which helps in building, running, and distributing the docker containers. The Docker client run with the daemon on the same system or we can connect the docker client with the docker daemon remotely. With the help of REST API over a  UNIX socket or a network, the docker client and daemon interact with each other. 


![image](https://user-images.githubusercontent.com/29191813/229864265-bcfa7b8d-b787-4c30-9f9e-e2d2fe37f706.png)

### Docker Daemon
Docker daemon manages all the services by communicating with other daemons. It manages docker objects such as images, containers, networks, and volumes with the help of the API requests of Docker.( A persistent, background process that manages running containers, images, and volumes. It handles API requests by the client, builds and runs Docker images, creates containers from those images, and allows clients to connect with those containers using a namespace for volume storage.)

### Docker Client
With the help of the docker client, the docker users can interact with the docker. The docker command uses the Docker API. The Docker client can communicate with multiple daemons. When a docker client runs any docker command on the docker terminal then the terminal sends instructions to the daemon. The Docker daemon gets those instructions from the docker client withinside the shape of the command and REST API’s request.

The main objective of the docker client is to provide a way to direct the pull of images from the docker registry and run them on the docker host. The common commands which are used by clients are docker build, docker pull, and docker run.

### Docker Engine
It is the core part of the whole Docker system. Docker Engine is an application which follows client-server architecture. It is installed on the host machine. There are three components in the Docker Engine:

Server: It is the docker daemon called dockerd. It can create and manage docker images. Containers, networks, etc.
Rest API: It is used to instruct docker daemon what to do.
Command Line Interface (CLI): It is a client which is used to enter docker commands.

### Docker Engine REST API: The Docker API allows the Docker Engine to be controlled by other applications. They can use it to query information about containers or images, manage or upload images, or perform actions such as creating new containers. This function is accessed through a web service called HTTP client.

### Docker CLI: A command-line tool used for interacting with the Docker daemon. This is one of the key reasons why people like to use Docker in the developer environment.

### Docker Host
A Docker host is a type of machine which is responsible for running more than one container. It comprises of the Docker daemon, Images, Containers, Networks, and Storage.

### Docker Registry
All the docker images are stored in the docker registry. There is a public registry which is known as a docker hub that can be used by anyone. We can run our private registry also. With the help of docker run or docker pull commands, we can pull the required images from our configured registry. Images are pushed into configured registry with the help of the docker push command.

### Docker Objects
Whenever we are using a docker, we are creating and use images, containers, volumes, networks and other objects. 

## Docker States

What is Docker Container Lifecycle?
A container is a process in OS. A process is an instance of a computer program that is being executed. But container processes are different. Container processes are fully-functional environments, and they have more isolation from the OS than the processes in OS

![image](https://user-images.githubusercontent.com/29191813/229866655-b55a90e7-a408-433f-b1dc-4c60c6d759dc.png)

By default, the docker ps command displays the current state of all the Docker containers:

![image](https://user-images.githubusercontent.com/29191813/229867374-515b02aa-4c81-4be4-8758-486eb28bac25.png)


## Docker file, Image & Container

### Docker file
Docker can build images automatically by reading the instructions from a Dockerfile. A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. This page describes the commands you can use in a Dockerfile.
### Dockerfile Commands

![image](https://user-images.githubusercontent.com/29191813/229875468-cc25eafe-e635-47fb-83d3-0e736e082c90.png)

![image](https://user-images.githubusercontent.com/29191813/229875562-69b56bb5-721b-47d3-bb12-2bdf000a45e0.png)

![image](https://user-images.githubusercontent.com/29191813/229875631-909ef026-6228-4ea1-902d-8141cbf97aea.png)



Images
An image contains instructions for creating a docker container. It is just a read-only template. It is used to store and ship applications. Images are an important part of the docker experience as they enable collaboration between developers in any way which is not possible earlier.

Containers
Containers are created from docker images as they are ready applications. With the help of Docker API or CLI, we can start, stop, delete or move a container. A container can access only those resources which are defined in the image unless additional access is defined during the building of an image in the container.

### Docker file - In depth

![image](https://user-images.githubusercontent.com/29191813/229868215-0d480711-4278-4ca3-8d05-69127deda0ff.png)
![image](https://user-images.githubusercontent.com/29191813/229868303-040d29cf-133e-4654-bb6a-9a0d9e878837.png)
![image](https://user-images.githubusercontent.com/29191813/229868378-03cd498b-f786-4817-8cc1-2be9f98a79a8.png)
![image](https://user-images.githubusercontent.com/29191813/229868436-b2aabab0-1df1-4af1-95bd-0c062aa97d5e.png)
![image](https://user-images.githubusercontent.com/29191813/229868527-81dc7986-459d-4a8b-90e5-374d3b713110.png)
![image](https://user-images.githubusercontent.com/29191813/229868604-b92d36b6-39f3-4e0a-b618-8c0f414ff5a5.png)
![image](https://user-images.githubusercontent.com/29191813/229868697-f2d574f9-e2b4-40ef-8195-93d967475f88.png)
![image](https://user-images.githubusercontent.com/29191813/229868850-519b4476-36ec-4a01-862f-b39521cac712.png)
![image](https://user-images.githubusercontent.com/29191813/229868924-50a7123f-2358-4001-b139-563c74540e59.png)
![image](https://user-images.githubusercontent.com/29191813/229869017-93c2bb7e-1cde-4c7e-a5c7-80be26c5f6d2.png)
![image](https://user-images.githubusercontent.com/29191813/229869071-931bf1b3-7ca8-49a0-9293-18471bca119e.png)

Sample Docker file to install nginx :

![image](https://user-images.githubusercontent.com/29191813/229869882-4368f325-047c-4fe0-bde5-f05978745ace.png)

Sample Docker file to install jenkins :

FROM jenkins/jenkins:lts-jdk11
USER root
RUN apt update && \
    apt install -y --no-install-recommends gnupg curl ca-certificates apt-transport-https && \
    curl -sSfL https://apt.octopus.com/public.key | apt-key add - && \
    sh -c "echo deb https://apt.octopus.com/ stable main > /etc/apt/sources.list.d/octopus.com.list" && \
    apt update && apt install -y octopuscli
USER jenkins

## Docker volume

Storage
We can store data within the writable layer of the container but it requires a storage driver. Storage driver controls and manages the images and containers on our docker host. 

Keeping the persistent storage as a reference, docker offer 4 options:-

Data Volumes
Volume Container
Directory Mounts
Storage Plugins


##  Docker compose
##  Docker registry
##  Docker API & CLI
## Environment variables in Docker
## Monitoring , Logging in Docker
## Docker Networking

Networking 
Docker networking provides complete isolation for docker containers. It means a user can link a docker container to many networks. It requires very less OS instances to run the workload.

There are primarily 5 network drivers in docker:

Bridge: It is the default network driver. We can use this when different containers communicate with the same docker host.
Host: When you don’t need any isolation between the container and host then it is used.
Overlay: For communication with each other, it will enable the swarm services.
None: It disables all networking.
macvlan: This network assigns MAC(Media Access control) address to the containers which look like a physical address.

## Docker swarm
## Security in Docker
## Troubleshooting

Use COPY for standard file copying (recommended).
Use ADD only if you need to extract archives or download from URLs.

##################
ENTRYPOINT
Purpose:
Sets the main executable that always runs when the container starts.
Overridable:
Not easily overridden by docker run arguments (unless you use --entrypoint).
Typical use:
When you want your container to always run a specific command.
Example: ENTRYPOINT ["python", "app.py"]
CMD
Purpose:
Provides default arguments for the container’s main process.
Overridable:
Easily overridden by arguments passed to docker run.
Typical use:
To set default parameters or commands, but allow users to change them.
Example: CMD ["app.py"]
Combined Usage
You can use both together:
ENTRYPOINT ["python"]
CMD ["app.py"]
By default, runs python app.py.
You can override app.py with another script when running the container.
Summary:

ENTRYPOINT defines the fixed executable.
CMD provides default arguments or commands, which can be overridden.
Use ENTRYPOINT for required commands, CMD for defaults.
###
**Docker EcoSystem**

![image](https://user-images.githubusercontent.com/29191813/225827998-c45deb18-992e-42db-847a-29418893c71b.png)
