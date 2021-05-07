FROM rabbitmq:3.8.16-alpine

# exit with 0 for build the container and not recive other exit command
RUN rabbitmq-plugins enable rabbitmq_mqtt; rabbitmq-server && \
    rabbitmqctl add_user test test && \
    rabbitmqctl set_user_tags test administrator && \
    rabbitmqctl set_permissions -p / test ".*" ".*" ".*"; exit 0
