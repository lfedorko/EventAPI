from django.forms import model_to_dict

from API.models import Events
from datetime import datetime
from API.search_logic.find_distance import searchDistance


def find_by_category(text):
    if not text in ['концерт','вечеринка','театр','стендап','лекция','мастер-класс']:
        return '()'
    day = datetime.now()
    day = day.strftime("%d.%m.%Y")
    res = Events.objects.filter(category=text).values()
    return res


def find_by_location(lat, long):
    day = datetime.now()
    day = day.strftime("%d.%m.%Y")
    res = list(Events.objects.filter(expire_date="20.12.2018").values())
    res = searchDistance(res, lat,long)
    return res[:3]




























































