import re

from requests import get
from simplepush import send

recipients = ['cvTRWj', 'Jd7BvU']
pattern = r"<td data-label='Availability'.+><button.+>(.+)<\/button><\/td>"

try:
    page_contents = get('https://www.talonhill.com/floorplans.aspx').content.decode('utf-8')

    groups = re.findall(pattern, page_contents)
    for group in groups[3:6]:
        if group != 'Contact':
            for recipient in recipients:
                send(recipient, '2-Bed Available!', group)
            break

except Exception as e:
    for recipient in recipients:
        send(recipient, 'i broke :(', e)

    raise e
