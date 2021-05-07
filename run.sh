#!/usr/bin/env bash
# Script to set the configureation of the project

./scripts/init-rabbitmq.sh
# run the iot device
python3 pub/pub.py
