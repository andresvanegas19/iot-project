#!/bin/bash
set -e

/etc/init.d/postgresql start
psql -f set-up-db.sql
/etc/init.d/postgresql stop
