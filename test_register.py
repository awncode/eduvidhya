from app import app, CSV_PATH, ensure_csv
import csv

ensure_csv()

with app.test_client() as client:
    resp = client.post('/register', json={
        'name': 'Test User',
        'email': 'test@example.com',
        'phone': '1234567890'
    })
    print('status', resp.status_code, resp.get_json())

    with open(CSV_PATH, newline='', encoding='utf-8') as f:
        rows = list(csv.reader(f))
        print('rows_count', len(rows))
        print('last_row', rows[-1])
