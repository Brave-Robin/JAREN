""" conver text to utf8-uri """

import urllib.parse


def input_convert():
    input_data = []
    command_fields = {
        'input_text':"Введите текст",
        'input_date':"Введите дату",
        'input_blocked_by':"С какой связан",
        'input_status':"Статус",
        'input_user_id':"ID пользователя"
    }
    for k,v in command_fields.items():
        raw_data = input(v+": ")
        if k == "input_text":
            raw_data = urllib.parse.quote(raw_data, safe='')
        input_data.append(raw_data)

    return (f"curl.exe -X 'PUT' 'http://127.0.0.1:8000/create/?"
            f"todo_text={input_data[0]}&"
            f"todo_due_date={input_data[1]}&"
            f"todo_blocked_by={input_data[2]}&"
            f"todo_status={input_data[3]}&"
            f"todo_user_id={input_data[4]}' "
            f"-H 'accept: application/json'")


print(input_convert())





"""
TODO: write script for create valid curl-request like a:
curl.exe -X 'PUT' 'http://127.0.0.1:8000/create/?todo_text=%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9%20todo%20%D0%B8%D0%B7%20%D1%83%D1%82%D0%B8%D0%BB%D0%B8%D1%82%D1%8B&todo_due_date=2024-12-30&todo_blocked_by=0&todo_status=false&todo_user_id=1000' -H 'accept: application/json'
with all fields!
return: curl requests command
"""
# input_text = input("Text to code: ")
# input_date = input("Date to code: ")
# input_blocked_by = input("Text to code: ")
# input_status = input("Text to code: ")
# input_user_id = input("Text to code: ")
# input_text: str
# input_date: str | None = 'NULL'
# input_blocked_by: int | None = 0
# input_status: bool | None = False
# input_user_id: int
