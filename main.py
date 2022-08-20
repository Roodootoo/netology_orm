import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import create_tables, Publisher, Book, Sale, Shop, Stock

DSN = 'sqlite:///:memory:'
# engine = sq.create_engine(DSN, echo=True)
engine = sq.create_engine(DSN)

create_tables(engine)

p1 = Publisher(name='Альпина', books = [
    Book(title="6 минут: Ежедневник, который изменит вашу жизнь"),
    Book(title="Тонкое искусство пофигизма: Парадоксальный способ жить счастливо"),
    Book(title="Думай как математик: Как решать любые проблемы быстрее и эффективнее")])
p2 = Publisher(name='Питер', books = [
    Book(title="Python. Лучшие практики и инструменты"),
    Book(title="Python. Чистый код для продолжающих"),
    Book(title="Основы Data Science и Big Data. Python и наука о данных")])
b1 = Book(title="Паттерны разработки на Python: TDD, DDD и событийно-ориентированная архитектура", publisher=p2)
shop1 = Shop(name="Лабиринт")
stock1 = Stock(book=b1, shop=shop1, count=50)
sale1 = Sale(price=250, stock=stock1, count=25)

Session = sessionmaker(bind=engine)
s = Session()
s.add_all([p1, p2, b1, shop1, stock1, sale1])
s.commit()

# x = input()
x = 'Питер'
print(s.query(Publisher).filter(sq.or_(Publisher.id==x, Publisher.name==x)).all()[0])

s.close()