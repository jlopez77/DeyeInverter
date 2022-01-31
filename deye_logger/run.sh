#!/usr/bin/with-contenv bashio

#declare MQTT_HOST
#declare MQTT_USER
#declare MQTT_PASSWORD

#TODO: Read the mosquitto broker values directly avoinding the need to configure.
#MQTT_HOST=$(bashio::services mqtt "host")
#MQTT_USER=$(bashio::services mqtt "username")
#MQTT_PASSWORD=$(bashio::services mqtt "password")

#bashio::log.info "${MQTT_HOST}"
#bashio::log.info "${MQTT_USER}"
#bashio::log.info "${MQTT_PASSWORD}"

CONFIG_PATH=/data/options.json

mqtt_topic="$(bashio::config 'mqtt_topic')"

bashio::log.info "Starting InverterData.py"

# Run the script every 5 minutes
# TODO: make this value configurable through config.yaml
watch -n 300 'python3 InverterData.py'

#echo "$(bashio::config 'inverter_ip')"
#echo "$(bashio::config 'inverter_port')"
#echo "$(bashio::config 'inverter_sn')"
#echo "$(bashio::config 'mqtt')"
#echo "$(bashio::config 'mqtt_server')"
#echo "$(bashio::config 'mqtt_port')"
#echo "$(bashio::config 'mqtt_topic')"
#echo "$(bashio::config 'mqtt_username')"
#echo "$(bashio::config 'mqtt_passwd')"


bashio::log.info "Script terminated"
