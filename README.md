# Openshift UDP

Resources for testing UDP connection in OpenShift

## Deploy consumer and configure UDP nodeport

```sh
# Create a namespace
oc new-project test-udp

# Create application in OpenShift
oc new-app  --strategy=docker --name udp-consumer --context-dir=consumer https://github.com/clbartolome/openshift-udp

# Update deployment to use port 5000 and UDP
oc patch deployment/udp-consumer -p '{"spec":{"template":{"spec":{"containers":[{"name":"udp-consumer","ports":[{"containerPort":5000,"protocol":"UDP"}]}]}}}}'

# Update service to redirect traffic to port 5000 and UDP
oc patch service udp-consumer -n udp-test --type='json' -p='[{"op": "replace", "path": "/spec/type", "value":"NodePort"},{"op": "replace", "path": "/spec/ports", "value":[{"port": 5000, "protocol": "UDP", "targetPort": 5000}]}]'

# Validate service is configured properly and get assigned port (in this example is 31552)
oc get svc udp-consumer
# NAME           TYPE       CLUSTER-IP     EXTERNAL-IP   PORT(S)          AGE
# udp-consumer   NodePort   172.30.40.32   <none>        5000:31552/UDP   48m

# Validate application pods are running
oc get pods
# NAME                            READY   STATUS      RESTARTS   AGE
# udp-consumer-7749bfc8c7-q4gjp   1/1     Running     0          47m
```

## Test UDP connection

```sh
# Get worker node IP (in this example we're going to use compute-0)
# IMPORTANT: admin rights needed to get the IP using oc CLI
# NOTE: the node where the app pod is running does not matter, OCP will redirect to the right node
oc get nodes -o wide
# NAME        STATUS   ROLES                  AGE   VERSION           INTERNAL-IP ...
# compute-0   Ready    worker                 20d   v1.28.7+f1b5f6c   192.xxx.xx.13 ...
# compute-1   Ready    worker                 20d   v1.28.7+f1b5f6c   192.xxx.xx.14 ...
# compute-2   Ready    worker                 20d   v1.28.7+f1b5f6c   192.xxx.xx.15 ...
# master-0    Ready    control-plane,master   20d   v1.28.7+f1b5f6c   192.xxx.xx.10 ...
# master-1    Ready    control-plane,master   20d   v1.28.7+f1b5f6c   192.xxx.xx.11 ...
# master-2    Ready    control-plane,master   20d   v1.28.7+f1b5f6c   192.xxx.xx.12 ...

# Test connection to the node
ping 192.xxx.xx.13

# Send a message using UDP
echo -n "Hello, UDP consumer!" | nc -uv 192.xxx.xx.13 31552

# Validate pod is getting the message
oc logs udp-consumer-7749bfc8c7-q4gjp
# UDP server listening on port 5000
# Received message: Hello, UDP consumer!
```




