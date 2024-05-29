Cluster Components
Kubernetes Proxy
The Kubernetes proxy is responsible for routing network traffic to loadbalanced services in the Kubernetes cluster. To do its job, the proxy must be
present on every node in the cluster
Kubernetes DNS
Kubernetes also runs a DNS server, which provides naming and discovery for the services that are defined in the cluster. This DNS server also runs as
a replicated service on the cluster

Kubernetes uses namespaces to organize objects in the cluster. You can think of each namespace as a folder that holds a set of objects. By default,
the kubectl command-line tool interacts with the default namespace. If you want to use a different namespace, you can pass kubectl the --
namespace flag. 


Contexts
If you want to change the default namespace more permanently, you can use a context. This gets recorded in a kubectl configuration file, usually
located at $HOME/.kube/config

kubectl config set-context my-context --namespace=mystuff
kubectl config use-context my-context

Creating, Updating, and Destroying
Kubernetes Objects
Objects in the Kubernetes API are represented as JSON or YAML files
You can use these YAML or JSON
files to create, update, or delete objects on the Kubernetes server.
kubectl apply -f obj.yaml
after you make changes to the object, you can use the apply
command again to update the object:
$ kubectl apply -f obj.yaml

If the objects you are creating already exist in the cluster, it will simply exit successfully without making any changes

If you want to see what the apply command will do without actually making the changes, you can use the --dry-run flag to print the objects
to the terminal without actually sending them to the server The apply command also records the history of previous configurations in
an annotation within the object. You can manipulate these records with the  edit-last-applied, set-last-applied, and view-lastapplied commands. 

When you want to delete an object, you can simply run:
$ kubectl delete -f obj.yaml

Debugging Commands
to see the logs for a running container:
$ kubectl logs <pod-name>
If you have multiple containers in your Pod, you can choose the container to view using the -c flag.
By default, kubectl logs lists the current logs and exits

You can also use the exec command to execute a command in a running
container:
$ kubectl exec -it <pod-name> -- bash
If you don’t have bash or some other terminal available within your container, you can always attach to the running process:
$ kubectl attach -it <pod-name>

copy files to and from a container using the cp command:
$ kubectl cp <pod-name>:</path/to/remote/file>
</path/to/local/file>

If you want to access your Pod via the network, you can use the portforward command to forward network traffic from the local machine to
the Pod
kubectl port-forward <pod-name> 8080:80
opens up a connection that forwards traffic from the local machine on port 8080 to the remote container on port 80.

If you want to view Kubernetes events, you can use the kubectl get events command to see a list of the latest 10 events on all objects in a
given namespace.
$ kubectl get events

if you are interested in how your cluster is using resources, you can use the top command to see the list of resources in use by either nodes or
Pods. This command:
kubectl top nodes
will display the total CPU and memory in use by the nodes in terms of both absolute units (e.g., cores) and percentage of available resources (e.g., total
number of cores). Similarly, this command:
kubectl top pods
will show all Pods and their resource usage. By default it only displays Pods in the current namespace, but you can add the --all-namespaces
flag to see resource usage by all Pods in the cluster.

Cluster Management
The kubectl tool can also be used to manage the cluster itself. The most common action that people take to manage their cluster is to cordon and drain a particular node. When you cordon a node you prevent future Pods from being scheduled onto that machine. When you drain a node, you remove any Pods that are currently running on that machine. A good example use case for these commands would be removing a physical machine for repairs or upgrades.

The Pod Manifest
Pods are described in a Pod manifest., which is just a text-file representation
of the Kubernetes API object The Kubernetes API server accepts and processes Pod manifests before
storing them in persistent storage (etcd). The scheduler also uses the
Kubernetes API to find Pods that haven’t been scheduled to a node It then
places the Pods onto nodes depending on the resources and other constraints
expressed in the Pod manifests. 

Listing Pods
kubectl get pods
kubectl describe pods kuard

Deleting a Pod
When it is time to delete a Pod, you can delete it either by name:
$ kubectl delete pods/kuard 
or 
kubectl delete -f kuard-pod.yaml


When a Pod is deleted, it is not immediately killed. Instead, if you run
kubectl get pods, you will see that the Pod is in the Terminating
state. All Pods have a termination grace period. By default, this is 30
seconds. When a Pod is transitioned to Terminating it no longer
receives new requests. In a serving scenario, the grace period is important
for reliability because it allows the Pod to finish any active requests that it
may be in the middle of processing before it is terminated.
The
kubectl logs command downloads the current logs from the running instance:
$ kubectl logs kuard
The kubectl logs command always tries to get logs from the currently
running container. Adding the --previous flag will get logs from a
previous instance of the container. This is useful, for example, if your
containers are continuously restarting due to a problem at container startup.

Health Checks

Liveness health checks run application-specific logic, like loading
a web page, to verify that the application is not just still running, but is
functioning properly. Since these liveness health checks are applicationspecific, you have to define them in your Pod manifest.

![image](https://github.com/kay1810/DevOpsVault/assets/29191813/81014259-28e9-4eaf-ac63-4a9b79e78f4f)

The preceding Pod manifest uses an httpGet probe to perform an HTTP
GET request against the /healthy endpoint on port 8080 of the kuard
container.



Kubernetes makes a distinction between liveness and readiness. Liveness
determines if an application is running properly. Containers that fail
liveness checks are restarted. Readiness describes when a container is ready
to serve user requests. Containers that fail readiness checks are removed
from service load balancers. Readiness probes are configured similarly to
liveness probes.


Kubernetes allows users to specify two different resource metrics. Resource
requests specify the minimum amount of a resource required to run the
application. Resource limits specify the maximum amount of a resource that
an application can consume

![image](https://github.com/kay1810/DevOpsVault/assets/29191813/b1d4d401-3cc0-4c50-af43-b981d8ca78c6)
