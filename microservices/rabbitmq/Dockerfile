FROM library/rabbitmq:3-management

ADD rabbitmq.conf /etc/rabbitmq/
ADD definitions.json /etc/rabbitmq/

RUN chown rabbitmq:rabbitmq /etc/rabbitmq/rabbitmq.conf /etc/rabbitmq/definitions.json

