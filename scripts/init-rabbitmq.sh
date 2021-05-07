#!/usr/bin/env bash
# Script to create a admin user

docker exec -i broker rabbitmqctl add_user test test
docker exec -i broker rabbitmq rabbitmqctl set_user_tags test administrator
docker exec -i broker rabbitmqctl set_permissions -p / test ".*" ".*" ".*"
# docker exec -i broker rabbitmq-plugins enable rabbitmq_mqtt

# docker exec -i rabbitmq rabbitmq-plugins enable rabbitmq_mqtt && \
#     rabbitmqctl add_user test test && \
#     rabbitmqctl set_user_tags test administrator && \
#     rabbitmqctl set_permissions -p / test ".*" ".*" ".*"; exit 0
