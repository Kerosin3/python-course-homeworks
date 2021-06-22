#!/bin/bash
#basi app initialiation
#use -dev or -prod flag
date0=$(date +'%d-%m-20%y')
echo current date is $date0
#app_flask="$PWD"/"$( basename "web_app/app.py" )"
flask_app="app.py"
flask_app=$PWD/$flask_app
#echo app is $flask_app
if [ -e $flask_app ]
then
  echo "file app exists"
  while [ -n "$1" ]
  do
    case "$1" in
    -dev) echo "Running in Developer mode"
        export FLASK_ENV=development;;
    -prod) echo "Running in Production mode";;
    *) echo "$1 is not an option, use either dev or prod"
      export FLASK_ENV=production;;
esac
shift
done
  echo flask_app is $flask_app
  export FLASK_APP=$flask_app
  #echo "Running Flask in Developer mode"
  #echo $FLASK_APP
  #echo $PWD
  flask run
else
  echo "file app does not exist, aborting"
  exit 1
fi
#docker-compose up database_local
# FLASK_ENV=development flask db upgrade
