#!/usr/bin/env python

import json
import sys
import os
import argparse

CONFIG_PATH = "/etc/ssh-selector/config.json"

def load_configuration():
    print("Loading configuration {}".format(CONFIG_PATH))
    if os.path.isfile(CONFIG_PATH) == False:
        print("Configuration file in path {} is missing.".format(CONFIG_PATH))
        print("Please provide configuration with hosts.")
        exit(-1)

    with open(CONFIG_PATH) as config_file:
        return json.load(config_file)


def search(configuration, search_param):
    suggested_connections = list()

    for connection in configuration:
        host = str(connection["host"])
        if host.find(search_param) != -1:
            suggested_connections.append(connection)

    return suggested_connections


def connect(host_config):
    command = "ssh {} -l {}".format(host_config["host"], host_config["user"])

    if "key" in host_config:
        command += " -i {}".format(host_config["key"])

    print("Running '{}'".format(command))
    os.system(command)

def list_hosts(hosts) :
    print("Hosts in {} file:".format(CONFIG_PATH))
    for host in hosts:
        print(host["host"])


def run(search_host):
    connections_configuration = load_configuration()

    if search_host == None or search_host == '':
        search_host = input("Server name: ")

    if search_host == "list":
        list_hosts(connections_configuration)
        return


    suggestions = search(connections_configuration, search_host)

    number_suggestions = len(suggestions)

    # No match found
    if number_suggestions == 0:
        print("No matching servers found")
        return

    # One match found, use it.
    if number_suggestions == 1:
        connect(suggestions[0])
        return

    # Multiple matches found, select one
    print("Multiple hosts found:")
    index = 0
    for suggestion in suggestions:
        print("[{}] \t {}".format(index, suggestion["host"]))
        index += 1

    selected_index = int(input("Select host: "))

    if selected_index < 0 or selected_index >= number_suggestions:
        print("Invalid index number.")
        return

    connect(suggestions[selected_index])

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="name of host or substring contained in hostname.", type=str)
    args = parser.parse_args()

    run(args.host)
