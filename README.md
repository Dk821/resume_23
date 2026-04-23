# 💼 Django Resume Portfolio Web App

A dynamic and customizable **Resume + Portfolio Web Application** built using Django.
This project allows users to showcase their professional profile, skills, projects, and experience in a clean, web-based format.

---

## 🚀 Features

* 🧑 Personal profile section (Name, bio, contact)
* 📄 Resume display (Education, Experience, Skills)
* 📁 Project portfolio showcase
* 🖼️ Image/file upload support
* 🛠️ Admin panel for easy content management
* 🌐 Responsive UI using templates
* 🔐 Secure backend with Django

---

## 🏗️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, Django Templates
* **Database:** SQLite3
* **Other:** Django Admin, Static & Media Handling

---

## 📁 Project Structure

```
resume/
│
├── portfolio/        # Main app
│   ├── migrations/
│   ├── templates/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│
├── resume/           # Project settings
│   ├── settings.py
│   ├── urls.py
│
├── static/           # Static files (CSS, JS)
├── uploads/          # Media uploads
├── db.sqlite3        # Database
├── manage.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Dk821/resume_23.git
cd resume_23
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install django
```

### 4️⃣ Apply migrations

```bash
python manage.py migrate
```

### 5️⃣ Run server

```bash
python manage.py runserver
```

👉 Open: http://127.0.0.1:8000/

---

## 🔑 Admin Access

Create superuser:

```bash
python manage.py createsuperuser
```

Login at:
👉 http://127.0.0.1:8000/admin/

---

## 📸 Screenshots

*Add your project screenshots here*

---

## 🌟 Future Improvements

* User authentication system
* Resume PDF download
* REST API integration
* Deployment (AWS / Vercel / Render)
* UI enhancement with React

---

## 🤝 Contributing

Feel free to fork this repository and improve it.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👤 Author

**Dinesh Kumar**
GitHub: https://github.com/Dk821

---
