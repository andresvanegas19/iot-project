FROM rabbitmq:3.6.6-management

RUN rabbitmq-plugins enable rabbitmq_mqtt; rabbitmq-server;

ADD rabbitmq.config /etc/rabbitmq/

ADD definitions.json /etc/rabbitmq/
RUN chown rabbitmq:rabbitmq /etc/rabbitmq/rabbitmq.config /etc/rabbitmq/definitions.json

CMD ["rabbitmq-server"]