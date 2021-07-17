#!/usr/bin/zsh
#use clean flag to clean up the project

echo current directory is $(pwd)
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
    if [ -d $emails_db ]; then
      echo deleting messsages db
      rm -r $emails_db
    fi
    if [ "$( docker inspect -f '{{.State.Running}}' rabbitmq )" = "true" ]; then
      image=$(docker ps -aqf "name=rabbitmq")
      echo 'stopping running container'
      docker stop $image
    fi
    echo finishing cleaning
    exit 1;;
esac
shift
done

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

