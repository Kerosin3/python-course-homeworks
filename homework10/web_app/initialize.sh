#!/bin/bash
#basi app initialiation
#use -dev or -prod flags
##use -f (flask), -p(python)  ====not implemented====
date0=$(date +'%d-%m-20%y')
echo current date is $date0
flask_app="app.py"
flask_app=$PWD/$flask_app
if [ -e $flask_app ]
then
  echo "file app exists"
  if (( $# == 0 )); then
    echo "you must specify at either -dev or -prod flag, aborting..."
    exit 1
fi
  while [ -n "$1" ]
  do
    case "$1" in
    -dev) echo "Running in Developer mode"
        export FLASK_ENV=development;;
    -prod) echo "Running in Production mode";;
    *) echo "$1 is not an option, use either dev or prod"
      export FLASK_ENV=production
      exit 1;;
esac
shift
done
  echo flask_app is $flask_app
  export FLASK_APP=$flask_app
  flask run --host='0.0.0.0'
#  flask run #--host='0.0.0.0'
else
  echo "file app does not exist, aborting"
  exit 1
fi
