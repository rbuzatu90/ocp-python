

delete(){
  for i in auth converter gateway notification rabbitmq; do
    oc delete -f /root/microservices/$i/manifests/
  done
  oc delete -f /root/microservices/mysql/
  oc delete -f /root/microservices/mongo/
  for i in $(oc get nodes | awk '{print $1}' | grep worker); do sssh $i "sudo rm -rf /mnt/*";done
}

create(){
  oc apply -f /root/microservices/mysql/
  oc apply -f /root/microservices/mongo/
  for i in rabbitmq auth converter gateway notification; do
    oc apply -f /root/microservices/$i/manifests/
  done
}

init(){
  oc exec rabbitmq-0 -- bash -c '/usr/local/bin/rabbitmqadmin declare queue --vhost=/ name=video durable=true'
  oc exec rabbitmq-0 -- bash -c '/usr/local/bin/rabbitmqadmin declare queue --vhost=/ name=mp3 durable=true'
  oc exec mongodb-test-0 -- bash -c 'mongo -u admin -p password << EOF
use videos
db.createUser( { user: "admin", pwd: "password",roles: [ "readWrite", "dbAdmin" ] } )
use mp3s
db.createUser( { user: "admin", pwd: "password",roles: [ "readWrite", "dbAdmin" ] } )
EOF'
}


#oc adm policy add-scc-to-user privileged -z default -n remus
#oc adm policy add-scc-to-user anyuid -z default -n remus



mp3(){
  gateway_url=$(oc get route gateway -o json | jq -r .spec.host)
  token=$(curl -X POST http://$gateway_url/login -u test@email.com:Admin123)
  echo "Token is $token"
  curl -vX POST -F 'file=@/root/microservices/StarWars.mkv' -H "Authorization: Bearer $token" http://$gateway_url/upload
}

get(){
  fid=$1
  echo Token is $token
  curl -vX GET --output test.mp3 -H "Authorization: Bearer $token" http://$gateway_url/download?fid=$fid
}


build(){
  repo=$1
  if [ ! -z $repo ] ; then
    echo Buildiing $repo
    cd /root/microservices/$repo/
    podman build -t rbuzatu/$(basename "$PWD"):latest . #; podman push rbuzatu/$(basename "$PWD"); oc delete $(oc get pods -l app=$(basename "$PWD") -o name)
    podman push --tls-verify=false rbuzatu/$(basename "$PWD") $(oc get route default-route -n openshift-image-registry -o json | jq -r .spec.host)/remus/$(basename "$PWD")

    cd -
  else
    echo rabbitmq auth converter gateway notification mongo mysql
  fi
}

notification(){
  watch -tn1 'oc logs  $(oc get pods -l app=notification -o name) | tail -50'
}
rabbit(){
  watch -tn1 'oc logs  $(oc get pods -l app=rabbitmq -o name) | tail -50'
}
gateway(){
  watch -tn1 'oc logs  $(oc get pods -l app=gateway -o name) | tail -50'
}
converter(){
  watch -tn1 'oc logs  $(oc get pods -l app=converter -o name) | tail -50'
}
mongo(){
  watch -tn1 'oc logs  $(oc get pods -l app=database -o name) | tail -50'
}
