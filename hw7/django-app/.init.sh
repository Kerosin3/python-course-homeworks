#!/usr/bin/zsh
#use clean flag to clean up the project
#use fresh flag to recreate DB
#just launch the scrip to run reserver

#echo current directory is $(pwd)
main_dir=$(pwd)

while [ -n "$1" ]
do
  case "$1" in
  -clean) echo "Cleaning up..."
    cel_dir=django_app/stocks_app
    new_dir="$main_dir/$cel_dir"
    cd $new_dir
    messages_file=data_tickers.txt
    emails_db=tmp
    if [ -f $messages_file ]; then
      echo deleting messsages
      rm data_tickers.txt
    fi
    db_file=db.sqlite3
    if [ -f $db_file ]; then
      echo deleting database
      rm db.sqlite3
    fi
    if [ -d $emails_db ]; then
      echo deleting messsages db
      rm -r $emails_db
    fi
    migrations_name=migrations
    migrations_dir=stocks/migrations
    new_dir2="$new_dir/$migrations_dir"
#    echo $new_dir2
    if [ -d $new_dir2 ]; then
      echo deleting migrations
      rm -r $new_dir2/*
      touch $new_dir2/__init__.py
    fi
    if [ "$( docker inspect -f '{{.State.Running}}' rabbitmq )" = "true" ]; then
      image=$(docker ps -aqf "name=rabbitmq")
      echo 'stopping running container'
      docker stop $image
    fi
    echo finishing cleaning
    exit 1;;
  -fresh) echo recreating DB
    # shellcheck disable=SC2164
    cd django_app/stocks_app
    ls
    python manage.py makemigrations
    python manage.py migrate
    echo Migrations creationg has been finished
    exit 1;;

esac
shift
done
echo Preforming poetry update
python -m pip install --upgrade pip
pip install poetry
poetry update
if [ "$( docker inspect -f '{{.State.Running}}' rabbitmq )" = "true" ]; then
  image=$(docker ps -aqf "name=rabbitmq")
  echo 'stopping running container'
  docker stop $image
  fi
echo 'running RabbitMQ'
(docker run -dt --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management) # not interactive
cel_dir=django_app/stocks_app
new_dir="$main_dir/$cel_dir"
echo starting Celery
cl()(
  #shellcheck disable=SC2164
  cd $new_dir
  (celery -A stocks_app worker -l info --detach)
)
cl
#shellcheck disable=SC2164
#cd django_app/stocks_app
cd $new_dir
varPrint=$'=================== Deleting all saved data ==================='
printf %q "$varPrint"
messages_file=data_tickers.txt
emails_db=tmp
if [ -f $messages_file ]; then
  echo deleting messsages
  rm data_tickers.txt
fi
if [ -d $emails_db ]; then
  echo deleting messsages db
  ls
  rm -r $emails_db
fi
echo starting App
python manage.py runserver

