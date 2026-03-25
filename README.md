# Bookstore API (FastAPI)

REST API for managing books built with FastAPI.

---

## 🚀 Features
- CRUD operations for books
- RESTful endpoints
- Data validation
- JSON responses

---

## 🛠 Tech Stack
- Python
- FastAPI

---

## 📡 Endpoints

### Get book
GET /book

### Get book by ID
GET /books/{id}

### Create book
POST /add_book

### Update book_instock
PATCH /book_in_stock/{book_title}

### Update book_numerosity
PATCH /book_numerosity/{book_title}

### Delete book
DELETE /delete_book/{id}

---

## ▶️ Run locally

```bash
uvicorn main:app --reload
