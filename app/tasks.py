
import requests
from celery import Celery

from . import celery_config

cel = Celery()
cel.config_from_object(celery_config)


@cel.task
def add(x, y):
    return x + y


@cel.task
def get_road(twenty_pionts):
    key = celery_config.AMAP_KEY

    kws = '|'.join('{},{}'.format(lat, lng) for lat, lng in twenty_pionts)

    params = {
        'key': key,
        'location': kws
    }
    url = 'http://restapi.amap.com/v3/geocode/regeo'
    resp = requests.get(url, params=params)
    return resp.json()
