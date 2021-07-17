#!/usr/bin/zsh
echo current directory is $(pwd)
main_dir=$(pwd)
if [ "$( docker inspect -f '{{.State.Running}}' rabbitmq )" = "true" ]; then
  image=$(docker ps -aqf "name=rabbitmq")
  echo 'stopping running container'
  docker stop $image
  fi
echo 'running RabbitMQ'
(docker run -dt --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management) # not interactive


#shellcheck disable=SC2164
#cd django_app/stocks_app
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
rm data_tickers.txt
echo starting App
python manage.py runserver

