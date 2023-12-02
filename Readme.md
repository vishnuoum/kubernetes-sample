# Kubernetes Deployment Sample

Basic flask app deployment with docker and kubernetes using minikube (local)

## Steps
1. Write the appplication
2. Up the minikube
3. Build the docker image
4. Tag the docker image locally
5. Push the docker image to dockerhub
6. Create a yml file with deployment and service configurations
7. Apply the yml file
8. Check if pods and service is running. Then start a tunnel using minikube


## Commands

**Starting minikube**

```
minikube start
```

**Building the docker image**

```
docker build -t <image-name> .
```

**Tagging the docker image and push to dockerhub**

```
docker tag <image> <username>/<repo>

docker push <username>/<repo>
```

**Deploying the image in kubernetes**

```
kubectl apply -f <filename>.yml
```

**Start tunnel with minikube**

```
minikube service <kubernetes-service>
```