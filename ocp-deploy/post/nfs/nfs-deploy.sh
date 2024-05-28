oc new-project nfs
oc create -f rbac.yaml
oc adm policy add-scc-to-user hostmount-anyuid system:serviceaccount:nfs:nfs-client-provisioner
oc apply -f deployment.yaml
oc apply -f class.yaml
oc apply -f test-claim.yaml
oc apply -f test-pod.yaml
