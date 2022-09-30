from calendar import HTMLCalendar
import requests

endpoint = "https://httpbin.org/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint) # Http Request
print(get_response.text)  # print raw text response


# Note:
# HTTP Request  ==> HTML
# REST API HTTP Request ==> JSON