# Run kubernetes cluster on GKE
## Setup a kubernetes cluster

All we want is a simple autoscalable cluster in a zone which is close to our location.

1. Go to http://console.cloud.google.com/
2. Log in on google cloud
3. Make sure the `Kubernetes Engine API` and the `Container Registry API` services are enabled
4. Open cloud shell
5. Enter the following command two commands:
```
export MY_ZONE=europe-north1-a
gcloud container clusters create apiservice --zone $MY_ZONE --enable-autoscaling --min-nodes=2 --max-nodes=5
```

This way we should have a kubernetes cluster called apiservice in google cloud which will have 1 master and 2 nodes at least. Whenever the workload increases GKE will increase the number of nodes to a maximum of 5.

## Startup a deployment
First of all add the deployment.yaml file to the cloud shell files by typing in:
```
nano deployment.yaml
```

Paste the contents of deployment.yaml in there and press `ctrl+o` and press enter. Than press `ctrl+x` to exit.

Now type the following to apply the deployment to the kubernetes
```
kubectl apply -f deployment.yaml
```

To check wether the deployment is successfull use 
```
kubectl get deployment
```
You should see something like this:
```
NAME                         READY   UP-TO-DATE   AVAILABLE   AGE
flaskversioning-deployment   1/1     1            1           89s
```

Change number of replicas with `nano deployment.yaml` and set to 4

Apply changes with
```
kubectl apply -f deployment.yaml
```
Check if it worked with 
```
kubectl get pods
```

Expose the container to public with
```
kubectl expose deployment flaskversioning-deployment --port 5000 --type LoadBalancer
```

Check wether it worked using 
```
kubectl get services
```

Use the public ip address and paste it in get_url.py. Run this script. It should say `version 1.0`.

Change the container image in de deployment script using `nano deployment.yaml` to tag v1.1

Apply the changes using
```
kubectl apply -f deployment.yaml
```

Check the running python script and see the version number getting updated