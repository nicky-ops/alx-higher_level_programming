#!/bin/bash
# this script takes in a URL and displays all HTTP methods the seerver will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-