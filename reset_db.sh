#!/bin/sh
sudo mysql -e "DROP DATABASE bluerate"
sudo mysql -e "CREATE DATABASE bluerate"
sudo mysql bluerate < officer.sql
