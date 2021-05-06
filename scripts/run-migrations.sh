#!/usr/bin/env bash
# script that make a migration

flask db init
flask db migrate
flask db upgrade
