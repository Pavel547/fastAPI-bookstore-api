from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import SessionLocall, engine

models.Base.metadata.create_all(bind=engine)

mini_market = FastAPI()

def get_db():
    db = SessionLocall()
    try:
       yield db
    finally:
        db.close()
        
@mini_market.post("/book", response_model=schemas.BookCreate)
def add_book(create_book: schemas.BookCreate, db: Session = Depends(get_db)):
    get_book = crud.get_book_by_title(db=db, title=create_book.title)
    if get_book:
        raise HTTPException(status_code=400, detail="Book already exists")
    return crud.add_book(db=db, book=create_book)

@mini_market.get("/book/id/{book_id}", response_model=schemas.Book)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_id(db=db, id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
    
@mini_market.get("/book/title/{book_title}", response_model=schemas.Book)
def get_book_by_title(book_title: str, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_title(db=db, title=book_title)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@mini_market.get("/books/books_genre/{books_genre}", response_model=list[schemas.Book])
def get_books_by_genre(books_genre: str, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_ganre(db=db, genre=books_genre)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Books not found")
    return db_book

@mini_market.get("/books/above_price/{books_price}", response_model=list[schemas.Book])
def get_books_above_price(book_price: float, db: Session = Depends(get_db)):
    db_book = crud.get_books_above_price(db=db, price=book_price)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Books not found")
    return db_book

@mini_market.get("/books/cheaper_price/{books_price}", response_model=list[schemas.Book])
def get_books_cheaper_price(book_price: float, db: Session = Depends(get_db)):
    db_book = crud.get_books_cheaper_price(db=db, price=book_price)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Books not found")
    return db_book

@mini_market.get("/books/by_price/{price}", response_model=list[schemas.Book])
def get_book_by_price(order_price: str = Query("asc", enum=["asc", "desc"]), db: Session = Depends(get_db),):
    db_book = crud.get_books_by_price(order=order_price, db=db)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Books not found")
    return db_book

@mini_market.patch("/book_instock/{book_title}", response_model=schemas.BookUpdate)
def update_book_instock(in_stock: bool, book_title: str, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_title(db=db, title=book_title)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.update_book_instock(db=db, title=book_title, update_book=in_stock)

@mini_market.patch("/book_numerosity/{book_title}", response_model=schemas.BookUpdate)
def update_book_numerosity(numerosity: int, book_title: str, db: Session = Depends(get_db)):
    db_book = crud.get_book_by_title(db=db, title=book_title)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return crud.update_book_numerosity(db=db, title=book_title, update_book=numerosity)

@mini_market.delete("/delet_book/{book_title}")
def delet_book(book_title: str, db: Session = Depends(get_db)):
    get_book = db.query(models.Book).filter(models.Book.title == book_title).first()
    if get_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    crud.dell_book(db=db, book=get_book)
    return "Book was deleted succsessfully"
