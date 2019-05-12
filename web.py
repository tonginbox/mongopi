from flask import Flask
from pymongo import MongoClient

# complient with uwsgi python
application = Flask(__name__)

def ObjectId(v):
    return v


data = [
{'_id': ObjectId('5ccff8dfb719d7fa2d05ad3e'), 'x': 1.0},
{'_id': ObjectId('5ccff8eab719d7fa2d05ad3f'), 'x': 2.0},
{'_id': ObjectId('5ccffabfb719d7fa2d05ad40'), 'name': 'Midhuna', 'age': 23.0, 'place': 'New York', 'hobbies': ['Singing', 'Reading Books'], 'spouse': {'name': 'Akash', 'age': 25.0}},
{'_id': ObjectId('5ccffae8b719d7fa2d05ad41'), 'name': 'Midhuna', 'age': 23.0, 'place': 'New York', 'hobbies': ['Singing', 'Reading Books']},
{'_id': ObjectId('5ccffbcab719d7fa2d05ad54'), 'name': 'Midhuna', 'age': 23.0, 'cars': ['BMW 320d', 'Audi R8'], 'place': 'Amaravati'},
{'_id': ObjectId('5ccffbcab719d7fa2d05ad55'), 'name': 'Akhil', 'age': 24.0, 'cars': ['Audo A7', 'Agera R'], 'place': 'New York'},
{'_id': ObjectId('5ccffbcab719d7fa2d05ad56'), 'name': 'Honey', 'age': 25.0, 'cars': ['Audi R8']},
{'_id': ObjectId('5ccffbcbb719d7fa2d05ad57'), 'name': 'Midhuna', 'age': 23.0, 'cars': ['BMW 320d', 'Audi R8'], 'place': 'Amaravati'},
{'_id': ObjectId('5ccffbcbb719d7fa2d05ad58'), 'name': 'Akhil', 'age': 24.0, 'cars': ['Audo A7', 'Agera R'], 'place': 'New York'},
{'_id': ObjectId('5ccffbcbb719d7fa2d05ad59'), 'name': 'Honey', 'age': 25.0, 'cars': ['Audi R8']},
{'_id': ObjectId('5ccffbcbb719d7fa2d05ad5a'), 'name': 'Midhuna', 'age': 23.0, 'cars': ['BMW 320d', 'Audi R8'], 'place': 'Amaravati'},
{'_id': ObjectId('5ccffbcbb719d7fa2d05ad5b'), 'name': 'Akhil', 'age': 24.0, 'cars': ['Audo A7', 'Agera R'], 'place': 'New York'},
{'_id': ObjectId('5ccffbcbb719d7fa2d05ad5c'), 'name': 'Honey', 'age': 25.0, 'cars': ['Audi R8']},
{'_id': ObjectId('5cd0028b2a488058e2adf098'), 'a': 1000},
{'_id': ObjectId('5cd002a22a488058e2adf099'), 'b': 32000},
{'_id': ObjectId('5cd6ae745f92b8a4c8279823'), 'a': 1000}
]


@application.route("/")
def hello():
    with fetch_data_from_mongo() as rows:
        return '<body><h1>hi</h1>%s</body>' % list_rows(rows)


def list_rows(rows):
    html_rows = []
    for row in rows:
        html_rows.append(
                show_row(row)
                )
    return '<table border=1>%s</table>' % ''.join(html_rows)


def show_row(row):
    html_row = []
    keys = row.keys()
    for key in keys:
        html_row.append(
                '<td>%s</td>' % row[key]
                )
    return '<tr>%s</tr>' % ''.join(html_row)

def fetch_data_from_mongo():
    client = MongoClient('mongodb://192.168.253.188:27017')
    db = client.data
    c = db.tonginbox
    recs = c.find()
    return recs


def main():
    print(list_rows(fetch_data_from_mongo()))
    #print(list_rows(data))


if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    main()
