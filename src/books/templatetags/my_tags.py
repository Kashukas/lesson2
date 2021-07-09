from django import template
import requests
from json import JSONDecodeError


register = template.Library()

#USD_ENDPOINT = 'https://www.nbrb.by/api/exrates/rates/145'
USD_ENDPOINT = 'https://www.nbrb.by/api/exrates/rates/840?parammode=1'



@register.simple_tag
def currency_rate(): # {% currency_rate %}
    try: 
        res = requests.get(USD_ENDPOINT)
        return res.json().get('Cur_OfficialRate')
    except JSONDecodeError:
        pass
