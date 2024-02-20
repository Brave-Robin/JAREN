""" conver text to utf8-uri """

import urllib.parse


input_string = input("Text to code: ")

print(urllib.parse.quote(input_string, safe=''))

"""
TODO: write script for create valid curl-request like a:
curl.exe -X 'PUT' 'http://127.0.0.1:8000/create/?todo_text=%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9%20todo%20%D0%B8%D0%B7%20%D1%83%D1%82%D0%B8%D0%BB%D0%B8%D1%82%D1%8B&todo_due_date=2024-12-30&todo_blocked_by=0&todo_status=false&todo_user_id=1000' -H 'accept: application/json'
with all fields!
return: curl requests command
"""