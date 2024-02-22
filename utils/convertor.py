""" conver text to utf8-uri """

import urllib.parse


def text_converter():
    input_string = input("Text to code: ")
    text = urllib.parse.quote(input_string, safe='')
    return text

def new_request():
    input_due_date = input("(yyyy-mm-dd): ")
    input_blocked_by = input("blocked by: ")
    input_status = input("status: (true/false)")
    input_user_id = input("user id: ")
    new_cmnd = f"curl.exe -X 'PUT' 'http://127.0.0.1:8000/create/?todo_text={text_converter()}&todo_due_date={input_due_date}&todo_blocked_by={input_blocked_by}&todo_status={input_status}&todo_user_id={input_user_id}' -H 'accept: application/json'"
    return new_cmnd

print(new_request())

"""
TODO: write script for create valid curl-request like a:
curl.exe -X 'PUT' 'http://127.0.0.1:8000/create/?todo_text=1%83%D1%82%D0%B8%D0%BB%D0%B8%D1%82%D1%8B&todo_due_date=2024-12-30&todo_blocked_by=0&todo_status=false&todo_user_id=1000' -H 'accept: application/json'
with all fields!
return: curl requests command
"""