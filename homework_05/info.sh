#!/bin/bash
info=$(whoami)
date=$
os_name=$(head -1 /etc/os-release)
python_version=$(python --version)
say="We are running $os_name on hostname:$(hostname) and $python_version on $(date)"
echo $say
echo "=========================Running Flask========================="
#eval $"flask run --host=0.0.0.0"
exec "$@"
