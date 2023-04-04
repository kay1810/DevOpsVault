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
## Docker file, Image & Container

Images
An image contains instructions for creating a docker container. It is just a read-only template. It is used to store and ship applications. Images are an important part of the docker experience as they enable collaboration between developers in any way which is not possible earlier.

Containers
Containers are created from docker images as they are ready applications. With the help of Docker API or CLI, we can start, stop, delete or move a container. A container can access only those resources which are defined in the image unless additional access is defined during the building of an image in the container.


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


**Docker EcoSystem**

![image](https://user-images.githubusercontent.com/29191813/225827998-c45deb18-992e-42db-847a-29418893c71b.png)
