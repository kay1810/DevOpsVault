# ✅ Docker Interview Preparation Checklist for DevOps Engineers

## 📦 Docker Basics
- [ ] Understand what Docker is and why it's used
- [ ] Difference between Docker and Virtual Machines
- [ ] Docker Architecture (Engine, CLI, Daemon, Registry)
- [ ] Install Docker on Linux/Mac/Windows

## 🏗️ Docker Images & Containers
- [ ] Build custom images using Dockerfile
- [ ] Understand image layers and caching
- [ ] Run containers (interactive, detached modes)
- [ ] Lifecycle of a container (create, start, stop, restart, remove)
- [ ] Docker image tagging and versioning

## 📝 Dockerfile Deep Dive
- [ ] FROM, RUN, CMD, ENTRYPOINT, COPY, ADD
- [ ] ENV, ARG, WORKDIR, EXPOSE, VOLUME
- [ ] Understand ENTRYPOINT vs CMD
- [ ] Use multi-stage builds for smaller images
- [ ] Dockerignore files

## 💾 Volumes & Storage
- [ ] Bind mounts vs Named volumes
- [ ] Creating, inspecting, removing volumes
- [ ] Backup and restore data from volumes

## 🌐 Networking
- [ ] Docker network types: bridge, host, overlay
- [ ] Creating custom networks
- [ ] Container-to-container communication
- [ ] Port mapping (`-p`) and linking containers

## ⚙️ Docker Compose
- [ ] Structure of docker-compose.yml
- [ ] Define services, networks, and volumes
- [ ] Build and run multi-container applications
- [ ] Use environment variables in Compose
- [ ] Scale services (`docker-compose up --scale`)

## 🗂️ Registries & Image Management
- [ ] Push/pull images to/from Docker Hub
- [ ] Use private registries (Harbor, AWS ECR, GitHub)
- [ ] Authenticate and work with private repos

## 🔐 Security & Best Practices
- [ ] Run containers as non-root users
- [ ] Scan images for vulnerabilities (Trivy, Docker Scan)
- [ ] Secrets management (basic ENV, Docker secrets in Swarm)
- [ ] Best practices for image optimization and Dockerfiles

## 🔄 CI/CD Integration
- [ ] Docker in Jenkins pipelines
- [ ] Docker with GitHub Actions or GitLab CI
- [ ] Tagging and pushing versioned images from CI

## 🛠️ Debugging & Monitoring
- [ ] Logs: `docker logs`
- [ ] Inspect container: `docker inspect`, `docker exec`
- [ ] Monitor with `docker stats`, `top`
- [ ] Clean up unused containers, images, volumes: `docker system prune`

## ☸️ Orchestration & Advanced (Optional)
- [ ] Basic knowledge of Docker Swarm (init, service, stack)
- [ ] Understand difference between Swarm and Kubernetes
- [ ] Docker Compose vs Kubernetes YAML comparison

