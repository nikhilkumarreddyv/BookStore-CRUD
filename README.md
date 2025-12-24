# 📚 BookStore-CRUD (Django)

## 📖 Project Overview
**BookStore-CRUD** is a Django-based web application that performs **CRUD operations** on books.

CRUD stands for:
- **Create** – Add new books
- **Read** – View book details
- **Update** – Edit existing books
- **Delete** – Remove books

This project is designed to help understand Django fundamentals such as models, views, templates, forms, and database interactions.

---

## 🚀 Features
- Add new books
- View all books
- Update book details
- Delete books
- Simple and clean UI
- Uses Django ORM for database operations

---

## 🛠️ Technologies Used
- **Python**
- **Django**
- **HTML, CSS, Bootstrap**
- **SQLite (default Django database)**
- **Git & GitHub**

---

## 📂 Project Structure
BookStore-CRUD/  
│── manage.py  
│── .env  
│── bookstore/  
│── books/  
     │── templates/  
        │── static/  
│── db.sqlite3  
│── requirements.txt


---

## ⚙️ Installation and Setup

Follow these steps to run the project locally.



### 1️⃣ Clone the Repository
```bash
git clone https://github.com/nikhilkumarreddyv/BookStore-CRUD.git

cd BookStore-CRUD
```

### 2️⃣ Create a Virtual Environment
Windows  
```bash
python -m venv env
env\Scripts\activate
```
Linux / macOS
```bash
python3 -m venv env
source env/bin/activate
```

### 3️⃣ Install Django
```bash
pip install django
```
Or install all dependencies:
```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a .env file in the project root:
```bash
SECRET_KEY=your-secret-key  
DEBUG=True
```
Generate a key using:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

```

### 5️⃣ Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ Run the Development Server
```bash
python manage.py runserver
```
Open your browser and go to:
```bash
http://127.0.0.1:8000/
```


## 🔄 CRUD Operations Explanation
#### ➕ Create

- Add new books using Django forms.

#### 📖 Read

- View the list of books stored in the database.

#### ✏️ Update

- Edit existing book details.

#### 🗑️ Delete

- Remove books from the database.
---

## 👨‍💻 Author 

**Nikhil Kumar Reddy**  
**GitHub:** https://github.com/nikhilkumarreddyv


### ⭐ Support

- If you like this project, consider giving it a ⭐ on GitHub!