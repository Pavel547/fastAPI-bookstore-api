from sqlalchemy.orm import Session
from sqlalchemy import asc, desc

from app import models, schemas

def add_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title = book.title,
        description = book.description,
        author = book.author,
        genre = book.genre,
        price = book.price,
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_book_by_id(db: Session, id: int):
    return db.query(models.Book).filter(models.Book.id == id).first()

def get_book_by_title(db: Session, title: str):
    return db.query(models.Book).filter(models.Book.title == title).first()

def get_book_by_genre(db: Session, genre: str):
    return db.query(models.Book).filter(models.Book.genre == genre).all()

def get_books_above_price(db: Session, price: float):
    return db.query(models.Book).filter(models.Book.price > price).all()

def get_books_cheaper_price(db: Session, price: float):
    return db.query(models.Book).filter(models.Book.price < price).all()

def get_books_by_price(order: str, db: Session):
    if order == "asc":
        return db.query(models.Book).order_by(asc(models.Book.price)).all()
    else:
        return db.query(models.Book).order_by(desc(models.Book.price)).all()
    
def update_book_instock(db: Session, title: str, update_book: schemas.BookUpdate):
    book = db.query(models.Book).filter(models.Book.title == title).first()
    book.in_stock = update_book
    db.commit()
    db.refresh(book)
    return book

def update_book_numerosity(db: Session, title: str, update_book: schemas.BookUpdate):
    book = db.query(models.Book).filter(models.Book.title == title).first()
    book.numerosity = update_book
    db.commit()
    db.refresh(book)
    return book
    

def dell_book(db: Session, book: schemas.Book):
    db.delete(book)
    db.commit()
