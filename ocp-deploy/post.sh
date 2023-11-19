oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"storage":{"emptyDir":{}}}}'
oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"managementState":"Managed"}}'




oc login --insecure-skip-tls-verify=true --username kubeadmin $(cat $KUBECONFIG | grep https |  awk '{print $2}' | head -1) --password $(cat $(dirname $KUBECONFIG)/kubeadmin-password)

podman login --tls-verify=false -u kubeadmin -p $(oc whoami -t) https://$(oc get route default-route -n openshift-image-registry -o json | jq -r .spec.host)


podman push --tls-verify=false quay.io/calico/typha $(oc get route default-route -n openshift-image-registry -o json | jq -r .spec.host)/<ns>/<imgname>
podman pull --tls-verify=false $(oc get route default-route -n openshift-image-registry -o json | jq -r .spec.host)/<ns>/<imgname>




curl -X POST -k https://api.ocp.mylab.test:6443/apis/build.openshift.io/v1/namespaces/remus/buildconfigs/notification/webhooks/secretvalue1/generic
