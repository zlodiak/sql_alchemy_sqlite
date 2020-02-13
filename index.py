import random
from sqlalchemy import create_engine, Table, MetaData, select, Column, String, Integer
from sqlalchemy.sql import and_, or_, not_

engine = create_engine('sqlite:///db.sqlite3')
connection = engine.connect()
metadata = MetaData()

quotes = Table('quotes', metadata,
    Column('id', Integer, primary_key=True),
    Column('text', String, nullable=False),
    Column('weight', Integer, nullable=False)
)
metadata.create_all(engine)


quotes_json = []
with open("text.txt") as file_handler:
    for line in file_handler:
        quotes_json.append({
            'text': line,
            'weight': random.randint(1, 10),
        })
connection.execute(quotes.insert(), quotes_json)


s = select([quotes]).where(and_(quotes.c.weight > 3, quotes.c.weight < 8))
result = connection.execute(s)
for row in result:
    print(row['id'], row['text'][:20] + '...', row['weight'])






