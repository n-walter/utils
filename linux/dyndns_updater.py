#!/usr/bin/python3

import requests
import datetime

dyndns_url = 'https://{}:{}@dyndns.strato.com/nic/update?hostname={}'
my_url = ''
username = ''
pw = ''

effective_url = dyndns_url.format(username, pw, my_url)

r = requests.get(effective_url)
text = r.text

iso_date = datetime.datetime.now().isoformat()

log_text = "{} - {}".format(iso_date, text)

with open("log.txt", "a") as target:
        target.write(log_text)
