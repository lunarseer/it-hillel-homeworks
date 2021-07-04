#!bin/bash
clear
curl -X POST -d "count=$1" http://127.0.0.1:8000/generate-teachers/