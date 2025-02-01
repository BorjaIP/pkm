---
title: Kubernetes
created: Monday 24th April 2023 19:04
aliases:
  - k8s
tags:
  - k8s
---
**Kubernetes** is a portable, extensible, open source platform for managing containerized workloads and services, that facilitates both declarative configuration and automation. It has a large, rapidly growing ecosystem. Kubernetes services, support, and tools are widely available.

| Tool                                                                                  | Description                                                                                   |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [Kubeshark](https://github.com/kubeshark/kubeshark)                                   | API traffic analyzer for Kubernetes (TCDump + Wireshark)                                      |
| [Vcluster](https://github.com/loft-sh/vcluster)                                       | Create fully functional virtual Kubernetes clusters                                           |
| [Openlens](https://github.com/MuhammedKalkan/OpenLens)                                | Lens - The way the world runs Kubernetes                                                      |
| [Cert-Manager](https://github.com/cert-manager/cert-manager)                          | Automatically provision and manage TLS certificates in Kubernetes                             |
| [Permissions-manager](https://github.com/sighupio/permission-manager)                 | Brings sanity to Kubernetes RBAC                                                              |
| [Kubectl-cost](https://github.com/kubecost/kubectl-cost)                              | CLI for determining the cost of Kubernetes workloads                                          |
| [Kubespray](https://github.com/kubernetes-sigs/kubespray)                             | Deploy a Production Ready Kubernetes Cluster                                                  |
| [MetalK8s](https://github.com/scality/metalk8s)                                       | Kubernetes distribution on-prem deployments                                                   |
| [K9s](https://k9scli.io/)                                                             | Kubernetes CLI To Manage Your Clusters In Style!                                              |
| [Kubectx](https://github.com/ahmetb/kubectx)                                          | Faster way to switch between clusters and namespaces in kubectl                               |
| [Opencost](https://github.com/opencost/opencost)                                      | Cross-cloud cost allocation models for Kubernetes workloads                                   |
| [Kubetap](https://github.com/soluble-ai/kubetap)                                      | Kubectl plugin to interactively proxy Kubernetes Services with ease                           |
| [Kubernetes-the-hard-way](https://github.com/kelseyhightower/kubernetes-the-hard-way) | Bootstrap Kubernetes the hard way                                                             |
| [CloudNativePG](https://github.com/cloudnative-pg/cloudnative-pg)                     | Kubernetes operator that covers the full lifecycle of a [[PostgreSQL]] database cluster       |
| [LongHorn](https://github.com/longhorn/longhorn)                                      | Longhorn is a distributed block storage system for Kubernetes                                 |
| [Keel](https://github.com/keel-hq/keel)                                               | Kubernetes Operator to automate Helm, DaemonSet, StatefulSet & Deployment updates             |
| [Kured](https://github.com/kubereboot/kured)                                          | Kubernetes Reboot Daemon                                                                      |
| [Kuma](https://github.com/kumahq/kuma)                                                | The multi-zone service mesh for containers, Kubernetes and VMs                                |
| [Pixie](https://github.com/pixie-io/pixie)                                            | Open-source observability tool for Kubernetes applications                                    |
| [Kueue](https://github.com/kubernetes-sigs/kueue)                                     | Kubernetes-native Job Queueing                                                                |
| [Flux](https://github.com/fluxcd/flux2)                                               | Open and extensible continuous delivery solution                                              |
| [Kuberhealthy](https://github.com/kuberhealthy/kuberhealthy)                          | Operator for running synthetic checks as pods                                                 |
| [Kubearmor](https://github.com/kubearmor/KubeArmor)                                   | Cloud-native runtime security enforcement system that restricts the behavior                  |
| [Popeye](https://github.com/derailed/popeye)                                          | Kubernetes cluster resource sanitizer                                                         |
| [Kube-linter](https://github.com/stackrox/kube-linter)                                | KubeLinter is a static analysis tool that checks Kubernetes YAML files and Helm charts        |
| [Karpenter](https://github.com/aws/karpenter-provider-aws)                            | Karpenter is a Kubernetes Node Autoscaler built for flexibility, performance, and simplicity. |
| [GlassKube](https://github.com/glasskube/glasskube)                                   | Package Manager for Kubernetes                                                                |
| [Devpod](https://github.com/loft-sh/devpod)                                           | Codespaces but open-source, client-only and unopinionated                                     |
| [Kubewall](https://github.com/kubewall/kubewall)                                      | A single binary kubernetes dashboard to manage your multiple clusters                         |
# Articles/Talks

- [Kubernetes Tools](https://github.com/AutomatingKubernetes/Kubernetes-Tools)
- [Kubernetes Security Checklist](https://reconshell.com/kubernetes-security-checklist/)
- [Kubernetes patterns ebook](https://blog.kubeify.com/ebooks/kubernetes-patterns-ebook.pdf)
- [Starting containers in order on Kubernetes with InitContainers](https://medium.com/@xcoulon/initializing-containers-in-order-with-kubernetes-18173b9cc222)
- [Securing kubernetes clusters with Istio and Keycloak](https://charnnarong.github.io/notes/kubernetes-istio-keycloak.html)
- [Hacking an AWS hosted Kubernetes backed product, and failing](https://blog.appsecco.com/hacking-an-aws-hosted-kubernetes-backed-product-and-failing-904cbe0b7c0d)
- [Adapting Docker and Kubernetes containers to run on Red Hat OpenShift Container Platform](https://developers.redhat.com/blog/2020/10/26/adapting-docker-and-kubernetes-containers-to-run-on-red-hat-openshift-container-platform#)
- [Kubernetes CKAD Example Exam Questions Practical Challenge Series](https://codeburst.io/kubernetes-ckad-weekly-challenges-overview-and-tips-7282b36a2681)
- [Practice Enough With These 150 Questions for the CKAD Exam](https://medium.com/bb-tutorials-and-thoughts/practice-enough-with-these-questions-for-the-ckad-exam-2f42d1228552)
- [CKAD Exercises](https://github.com/dgkanatsios/CKAD-exercises)
- [Kubernetes Network Policy Recipes](https://github.com/ahmetb/kubernetes-network-policy-recipes
- [KillerCoda - Killer Shell CKAD](https://killercoda.com/killer-shell-ckad)
- [Securing Kubernetes Cluster Networking](https://ahmet.im/blog/kubernetes-network-policy/)
# Packages

- [Find, install and publish Kubernetes packages](https://artifacthub.io/)
- [Operators for Kubernetes](https://operatorhub.io/)
# Components

- **Pod**: wrap one or more containers
- **Deploy**: scalability and application releases
- **Daemon Set** (ds): one pod per node (always have to be one running in each node)
- **Stateful Set** (sts): stateful app components
## Secrets

- Show secret in plain text

```bash
kubectl get secret -n name my-secret -o jsonpath="{.data.username}" | base64 --decode
```

- Duplicate an existing _Secret_ in the cluster in different NS

```bash
kubectl get secrets my-secret -n auth -o json \
 | jq 'del(.metadata["namespace","creationTimestamp","resourceVersion","selfLink","uid","annotations"])' \
 | kubectl apply -n other-ns -f 
```
## Volumes

- Create an empty volume for testing.

```yaml
apiVersion: v0
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - image: some-image-name
    name: my-container
    volumeMounts:
    - mountPath: /tempfiles
      name: temp-files-volume
  volumes:
  - name: temp-files-volume
    emptyDir: {}
```
## Ingress

### Nginx Controller

- [Ingress controller Annotations](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/)
### mTLS

- [mTLS setup using self-signed cert in Kubernetes and NGINX](https://stackoverflow.com/questions/63025817/mtls-setup-using-self-signed-cert-in-kubernetes-and-nginx)
- [Configuring Certificate-Based Mutual Authentication with Kubernetes Ingress-Nginx](https://awkwardferny.medium.com/configuring-certificate-based-mutual-authentication-with-kubernetes-ingress-nginx-20e7e38fdfca)
- [The magic of TLS, X509 and mutual authentication explained](https://medium.com/littlemanco/the-magic-of-tls-x509-and-mutual-authentication-explained-b2162dec4401)
- [mutual TLS based on specific IP](https://stackoverflow.com/questions/55690321/mutual-tls-based-on-specific-ip)

```bash
# Enable client certificate authentication
nginx.ingress.kubernetes.io/auth-tls-verify-client: "on"
# Create the secret containing the trusted ca certificates
nginx.ingress.kubernetes.io/auth-tls-secret: "namespace/secret"
# Specify if certificates are passed to upstream server
nginx.ingress.kubernetes.io/auth-tls-pass-certificate-to-upstream: "true" 

# Proxy
nginx.ingress.kubernetes.io/proxy-ssl-secret: "namespace/secret"
nginx.ingress.kubernetes.io/proxy-ssl-protocols: "TLSv1.3"
nginx.ingress.kubernetes.io/proxy-ssl-name: "example.com"

# HTTPS Backend
nginx.ingress.kubernetes.io/backend-protocol: HTTPS
nginx.ingress.kubernetes.io/secure-backends: "true"
nginx.ingress.kubernetes.io/ssl-redirect: "true"
nginx.ingress.kubernetes.io/force-ssl-redirect: "true"

# Pass https
nginx.ingress.kubernetes.io/ssl-passthrough: "true"

# Add TLSv3
nginx.ingress.kubernetes.io/configuration-snippet: |
    proxy_ssl_protocols             TLSv1.3;

# Snippets
nginx.org/server-snippets: |
  location / {
    proxy_set_header Host         $host;
    proxy_set_header Upgrade      $http_upgrade;
    proxy_set_header Connection   $connection_upgrade;
  }

nginx.org/server-snippets: |
  ssl_certificate /etc/nginx/secrets/namespace-secret-name; # namespace-name
  ssl_certificate_key /etc/nginx/secrets/namespace-secret-name; # namespace-name

# Timeout
nginx.ingress.kubernetes.io/proxy-read-timeout: "3600"
```

# Kubernetes API

All resources of API are managed under Special Interest Groups (SIGs) [here](https://github.com/kubernetes/community/blob/master/sig-list.md).
## Custom resources

Custom Resources (CRs) in Kubernetes allow you to extend the Kubernetes API and define your own API objects with custom schemas and behaviors. They provide a way to manage applications and resources that are not part of the core Kubernetes API.

The Kubernetes [declarative API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/) enforces a separation of responsibilities. You declare the desired state of your resource. The Kubernetes controller keeps the current state of Kubernetes objects in sync with your declared desired state. This is in contrast to an imperative API, where you _instruct_ a server what to do.

- Use [Metacontroller](https://github.com/metacontroller/metacontroller) is an add-on for Kubernetes that makes it easy to write and deploy CRs.

## Webhooks
### Admission webhook

An **admission controller** is a piece of code that intercepts requests to the Kubernetes API server prior to the persistence of the object, but after the request is authenticated and authorized

> Admission webhooks are HTTP callbacks that receive admission requests and do something with them. You can define two types of admission webhooks, validating admission webhook and mutating admission webhook. Mutating admission webhooks are invoked first, and can modify objects sent to the API server to enforce custom defaults

- `Mutating Admission Webhooks`: mutate the objects for resources, like Pods
- `Validating Admission Webhooks`: advanced validation for your resources
## Certificates

```bash
# conexion to API for see the certificate
openssl s_client -showcerts -connect localhost:6443 | openssl x509 -noout -text 
```

Check certs expiration with `kubeadm`

```bash
kubeadm certs check-expiration
```

Renew certificates

```bash
kubeadm certs renew all
# output
Done renewing certificates. You must restart the kube-apiserver, kube-controller-manager, kube-scheduler and etcd, so that they can use the new certificates.
```

Find `admin.conf` file for restart the Pods

```bash
find / -name admin.conf
kubectl --kubeconfig=/etc/kubernetes/admin.conf get nodes
```

Copy the new configuration

```bash
cp /etc/kubernetes/admin.conf /root/.kube/config
```

## Version

```bash
# display version
kubectl version
# display api version
kubectl api-versions | grep -i apps
```

# RBAC
## Role

 A Role always sets permissions within a particular namespace; when you create a Role, you have to specify the namespace it belongs in.

## Cluster Role

ClusterRole, by contrast, is a non-namespaced resource. The resources have different names (Role and ClusterRole) because a Kubernetes object always has to be either namespaced or not namespaced; it can’t be both.

- List all Cluster Role and Role

```bash
kubectl get rolebindings,clusterrolebindings \
--all-namespaces  \
-o custom-columns='KIND:kind,NAMESPACE:metadata.namespace,NAME:metadata.name,SERVICE_ACCOUNTS:subjects[?(@.kind=="ServiceAccount")].name'
```

- Use `can-i` for test pod creation

```bash
kubectl auth can-i create pods --context=user1-context
yes
```
## Users

```bash
kubectl get clusterrolebindings -o json | jq -r '.items[] | select(.subjects[0].kind=="Group") | select(.subjects[0].name=="system:masters")'
```

- Edit aws-auth for add new IAM roles.

```bash
kubectl edit -n kube-system configmap/aws-auth
# user example
arn:aws:iam::<userID>:user/<user-name>
```

```json
apiVersion: v1
data:
  mapAccounts: |
    []
  mapRoles: |
    - "groups":
      - "system:bootstrappers"
      - "system:nodes"
      "rolearn": "arn:aws:iam::<number>:role/<name>"
      "username": "system:node:{{EC2PrivateDNSName}}"
  mapUsers: |
    - "userarn": "arn:aws:iam::<number>:user/<user>"
      "username": "user"
      "groups":
      - "system:masters"
kind: ConfigMap
metadata:
  creationTimestamp: "2021-11-03T15:26:30Z"
  labels:
    app.kubernetes.io/managed-by: Terraform
    terraform.io/module: terraform-aws-modules.eks.aws
  name: aws-auth
  namespace: kube-system
  resourceVersion: "222342"
  uid: ce527f0b-e046-4b51-a853-b0abe675beeb
```

- Example of yaml

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: aws-auth
  namespace: kube-system
data:
  mapRoles: |
    - rolearn: <ARN of instance role (not instance profile)>
      username: system:node:{{EC2PrivateDNSName}}
      groups:
        - system:bootstrappers
        - system:nodes
```

## Auth

```bash
kubectl auth whoami  
ATTRIBUTE   VALUE  
Username    k8suser  
Groups      [k8s system:authenticated]
  
kubectl auth can-i get pods  
yes  
  
kubectl auth can-i get deployments.apps
```
# Plugins

[Krew](https://krew.sigs.k8s.io/)

```bash
# secret plugin
kubectl krew install whisper-secret
kubectl whisper-secret docker-registry my-secret --docker-password -- -n test --docker-username admin

# clean manifest
kubectl krew install neat
kubectl get pod mypod -o yaml | kubectl neat
kubectl neat get -- svc -n default myservice -o yaml

# permissions manager
https://github.com/sighupio/permission-manager

# Config files
kubectl krew install konfig
```

# Config

- Multiple context for different clusters. [kubeconfig](https://ahmet.im/blog/mastering-kubeconfig/)

```bash
kubectl config get-contexts
kubectl config use-context minikube
# extract config
kubectl config view --minify --flatten --context=minikube > minikube

# merge config
cd ~/.kube
kubectl konfig merge config <filename> > merged-config && mv -f merged-config config

# delete config
export node=node-name;(kubectl config unset clusters.$node && kubectl config unset users.$node && kubectl config unset contexts.$node)
kubectx -d dev-cluster-01
```

# Comands

- Create labels

```bash
# Crate a label
kubectl label nodes kworker-rj1 workload=production

# Display labels
kubectl get nodes --show-labels

# Grep pods by labels
kubectl label --list nodes kworker-rj1 | grep -i workload workload=production
```

- Clean replicaset

```bash
kubectl delete replicaset $(kubectl get replicaset -o jsonpath='{ .items[?(@.spec.replicas==0)].metadata.name }' -n minikube) -n minikube 
```

- Saber el Storage Class del cluster

```bash
kubectl describe sc
kubectl get storageclass
```

- Force delete Pod
  
```bash
kubectl delete pod --force=true --wait=false --grace-period=0 podname -n ns
```

- Kubelet
 
```bash
sudo netstat -tulpn | grep kubelet
curl 127.0.0.1:10248/healthz
```

- Healthz

```bash
curl -k https://localhost:6443/livez?verbose
kubectl get --raw='/readyz?verbose'
curl -k 'https://localhost:6443/readyz?verbose&exclude=etcd'
curl -k https://localhost:6443/livez/etcd
```


- Add nodes

```bash
# In Control Plane
kubeadm token create --print-join-command
# In worker node
kubeadm join url:6443 --token  --discovery-token-ca-cert-hash
# Enable kubelet
systemctl enable kubelet
# Ignoring Swap memory error
--ignore-preflight-errors=Swap
```

- Deploy busybox

```bash
kubectl run -n minikube busybox --image=busybox --restart=Never -- /bin/sh -c "sleep 3600;echo boo"
```

- Delete all

```bash
 kubectl delete all --all -n <namespace>
 kubectl delete namespace <namespace>
```

# Cloud
## AWS

- Configuration for [[AWS]] and K8s.

```bash
aws configure
aws sts get-caller-identity
# Download aws-iam-authenticator for get the token
curl -o aws-iam-authenticator https://amazon-eks.s3.us-west-2.amazonaws.com/1.21.2/2021-07-05/bin/linux/amd64/aws-iam-authenticator
```

# Third Party Tools

- [[Cert Manager]]
## Weave (Net connection)

```bash
# Test connection in Workers
curl 'http://127.0.0.1:6784/status'
kubectl exec -n kube-system weave-net-j8k27 -c weave -- /home/weave/weave --local status
# display errors
kubectl logs -n kube-system <a-weave-pod-id> weave | grep -i error
# remove database and reboot Worker Node
rm /var/lib/weave/weave-netdata.db
reboot
```

## Declarative Configuration

Kubernetes declarative configuration refers to the practice of declaring the desired state of applications and their resources in Kubernetes manifest files. This include [[IaC]], PaC or IaC.
### Structured Key-Value Pair

Structured key-value pair meets the minimum data declaration requirements (int, string, list, dict, etc.)

- JSON/YAML: It is very convenient for reading and automation, and has different languages API support.
- [[Kustomize]]
### Templated Key-Value Pair

The Templated KV has the capability of static configuration data and dynamic parameters, and can output different static configuration data with one template+dynamic parameters.

- [[Helm]]
### Programmable Key-Value Pair

`Configuration as Code (CaC)` uses code to generate configuration, just like engineers only need to write advanced GPL code, rather than manually writing error-prone and difficult-to-understand server binary code.

- [OPA](https://github.com/open-policy-agent/opa) --> Open Policy Agent (OPA) is an open source, general-purpose policy engine.
- [CEL](https://kubernetes.io/docs/reference/using-api/cel/) --> The [Common Expression Language (CEL)](https://github.com/google/cel-go) is used in the Kubernetes API to declare validation rules, policy rules, and other constraints or conditions.
### Typed Key-Value Pair

Based on programmable K-V, typed K-V has more capabilities of type constraints.

- [CUE](https://github.com/cue-lang/cue)--> Validate and define text-based and dynamic configuration
### Modeled Key-Value Pair

High-level language modeling capability as the core description

- [[KCL]]
### General-Purpose Languages and CDKs

Kubernetes resources using DSLs, we can also employ general-purpose languages for definition.

- [Pulumi](https://github.com/pulumi/pulumi)
### Hybrid Structured and Programmable KV

Some tools primarily employ structured KV for configuration management but also provide additional extensions to handle complex scenarios, eliminating the need for extensive YAML templating

- [Crossplane](https://github.com/crossplane/crossplane)
- [KPT](https://github.com/kptdev/kpt/tree/main) --> Automate Kubernetes Configuration Editing
# Bugs/Errors

- Broken connection between services with Names or IPs.

1. I would check my coreDNS pod under kube-system if there is an issue.
2. You could also try using the FQDN (fully qualified domain name) postgres-postgresql.[YOURNAMESPACE].svc.cluster.local
3. the postgres-postgresql service IP
4. postgres-postgresql-0 incase there is a problem with your svc networking
# Scalling

HorizontalPodAutoscaler

- Increase load deploying more Pods.

PodDisruptionBudget

- For HA you neeed to define Disruptions if a Node of the Cluster is down or upgraded. Stablish the minimum and maximum Pods are needed mandatory for your App.

# References

[1]: [Declarative Configuration Management](https://dev.to/peefy/10-ways-for-kubernetes-declarative-configuration-management-5pb)

