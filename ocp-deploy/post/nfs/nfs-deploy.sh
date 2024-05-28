oc new-project nfs
oc create -f rbac.yaml
oc adm policy add-scc-to-user hostmount-anyuid system:serviceaccount:nfs:nfs-client-provisioner
