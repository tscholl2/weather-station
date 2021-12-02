#!/bin/bash

SOURCE_HOST="pi3"
SOURCE_FILE="/mnt/usb/weather.db"
TARGET_FILE="/mnt/usb/weather.db.backup"

ssh "${SOURCE_HOST}" "sqlite3 ${SOURCE_FILE} '.backup ${SOURCE_FILE}.backup'"
rsync "${SOURCE_HOST}:${SOURCE_FILE}.backup" "${TARGET_FILE}"
