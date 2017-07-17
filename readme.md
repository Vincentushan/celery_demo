
## A Celery Demo to Fetch GEO Information from AMAP

To make this code work

1. install rabbitmq and redis
2. run `pip install -r requirments.txt`
3. set your amap key in app/celeryconfig.py
4. open 3 terminator windows and run code blow in different window
    
    celery -A app.tasks worker --loglevel=info --concurrency=10 -n worker0@%h

    celery -A app.tasks worker --loglevel=info --concurrency=10 -n worker1@%h

    celery -A app.tasks worker --loglevel=info --concurrency=10 -n worker2@%h
