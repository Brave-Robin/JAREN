# JAREN
Just Another REminder Notebook


# Developers run
```uvicorn main:app --reload```

# Notes

```sql
ALTER TABLE todos
ADD todo_status boolean NOT NULL DEFAULT False;
```

```commandline
curl.exe -X 'PUT' 'http://127.0.0.1:8000/create/?text=%D0%BA%D1%83%D0%BF%D0%B8%D1%82%D1%8C%20%D0%B6%D0%B8%D0%BB%D1%8C%D1%91&due_date=2024-12-30&blocked_by=0&status=false&user_id=1000' -H 'accept: application/json'
curl.exe -X 'PUT' 'http://127.0.0.1:8000/create/?text=%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C%20L3&due_date=2024-12-30&blocked_by=0&status=false&user_id=1000' -H 'accept: application/json'

curl.exe -X 'PUT' 'http://127.0.0.1:8000/create/?text=%D0%9F%D0%BE%D0%B4%D0%BD%D1%8F%D1%82%D1%8C%20%D0%B0%D0%BD%D0%B3%D0%BB%D0%B8%D0%B9%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B4%D0%BE%20B2%2FB2%2B&due_date=2024-12-30&blocked_by=0&status=false&user_id=1000' -H 'accept: application/json'
curl.exe -X 'PUT' 'http://127.0.0.1:8000/create/?text=%D0%A1%D0%B5%D1%80%D1%82%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%82%D1%8B&due_date=2024-12-30&blocked_by=0&status=false&user_id=1000' -H 'accept: application/json'
curl.exe -X 'PUT' 'http://127.0.0.1:8000/create/?text=%D0%98%D0%B7%D1%83%D1%87%D0%B8%D1%82%D1%8C%20%D0%93%D1%80%D1%83%D0%B7%D0%B8%D0%BD%D1%81%D0%BA%D0%B8%D0%B9%20%D0%B4%D0%BE%20A2&due_date=2024-12-30&blocked_by=0&status=false&user_id=1000' -H 'accept: application/json'
curl.exe -X 'PUT' 'http://127.0.0.1:8000/create/?text=%D0%9F%D0%BE%D0%BB%D1%83%D1%87%D0%B8%D1%82%D1%8C%20%D0%BF%D1%80%D0%B0%D0%B2%D0%B0%20A%2FB&due_date=2024-12-30&blocked_by=0&status=false&user_id=1000' -H 'accept: application/json'
curl.exe -X 'PUT' 'http://127.0.0.1:8000/create/?text=%D0%9A%D1%83%D0%BF%D0%B8%D1%82%D1%8C%20%D0%B2%D0%B5%D0%BB%D0%BE%D1%81%D0%B8%D0%BF%D0%B5%D0%B4&due_date=2024-12-30&blocked_by=0&status=false&user_id=1000' -H 'accept: application/json'
```
