**What does the volume parameter do in a docker run command?**
The volume parameter syncs a directory in a container with a host directory.

For example:
docker run -v nginx-sites:/etc/nginx/sites-available nginx
This command mounts the nginx-sites directory in the host to the /etc/nginx/sites-available directory. In this way, you can sync nginx sites without restarting the container they’re in. Also, you can protect your data that is generated in your container using a directory in the host. Otherwise, if you delete your container, your data that was generated and stored in your container will naturally be deleted.
When you use the volume parameter, you can use the same data that was generated in a previous container using the same command.

**What is Docker Compose? What can it be used for?**

Docker Compose is a tool that lets you define multiple containers and their configurations via a YAML or JSON file.
The most common use for Docker Compose is when your application has one or more dependencies, e.g., MySQL or Redis. Normally, during development, these dependencies are installed locally—a step that then needs re-doing when moving to a production setup. You can avoid these installation and configuration parts by using Docker Compose.
Once set up, you can bring all of these containers/dependencies up and running with a single docker-compose up command.

**Is there any problem with just using the latest tag in a container orchestration environment? What is considered best practice for image tagging?**

If you’re running your image via the latest tag with a container orchestration environment like Kubernetes, it may cause a problem.
The problem is if you push a new image with just the latest tag, you lose your old image and your deployments will use the new image. If the new image has any problem, your deployments might fail, resulting in downtime.
When you use explicit version numbers to tag Docker images instead, you can roll back to old images easily. Also, when you push a new image to your private registry, your deployments will continue to use the old version number due to your tag until you’re ready to switch each of them over.
The best practice of Docker image tagging is to use both types of tagging. First, tag your Docker images with latest and a version number, then push twice, separately for each tag. For example:
docker tag nginx:latest nginx:0.0.1
docker push nginx:latest
docker push nginx:0.0.1

**What is Docker Swarm and which network driver should be used with it?**

Docker Swarm is an open-source container orchestration tool that is integrated with the Docker engine and CLI. If you want to use Docker Swarm, you should use the overlay network driver. Using an overlay network enables the Swarm service by connecting multiple docker host daemons together.

**What is container orchestration and why should we use it?**

When you have to manage large and dynamic environments, the docker command alone does not suffice. You will face many problems automating scaling and health checks for containers. In this case, software teams use container orchestration tools like Kubernetes. Such software enables another level of automation:

Deploy or scale your containers easily, securely, and with high availability
Provide a service (internally or externally) from a container group
Move your containers from one host to another when there’s a host-specific problem
Manage your configuration data—like environment variables—easily

** Is it possible to pull/push Image, run/stop other docker containers from inside a container ? **



** talk to host docker daemon from inside a container ?**

**I have an app and a db container running on a host. How can these 2 containers talk to each other ? **
