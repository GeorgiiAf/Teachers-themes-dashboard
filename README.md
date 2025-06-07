# 📦 My Flask App

A multi-page Flask web application designed to facilitate interaction between **teachers** and **students**. Includes user authentication, task assignment, deadline tracking, commenting, file submission, and more. Deployed with Docker using **uWSGI** and **Nginx**.


<div align="center">
  <img src="./screenshots/pic3.png.png" alt="Main Interface" width="45%">
  <img src="./screenshots/pic2.png" alt="Adding theme as teacher" width="45%">
  <img src="./screenshots/pic4.png" alt="Student View" width="90%">
</div>


---

## 🔧 Tech Stack

- Flask  
- PostgreSQL  
- SQLAlchemy + Alembic  
- Flask-Login  
- Docker + Docker Compose  
- uWSGI + Nginx  
- WTForms  
- Jinja2  

---

## ✨ Features

- User registration and login  
- Two user roles:

  ### 👨‍🏫 Teacher:
  - Create/delete topics  
  - Assign students to topics  
  - Set task deadlines  
  - Review student submissions  
  - Add comments on submitted work  

  ### 👨‍🎓 Student:
  - View assigned topics  
  - Submit files for review  
  - Leave comments on tasks  

- Secure login system using Flask-Login  
- File upload support  
- Modular and extendable codebase  

---

## 🚀 Deployment

🟢 This project is deployed on **Microsoft Azure**  
Accessible at: [http://20.224.17.174:8080/](http://20.224.17.174:8080/)

You can also deploy the project to any cloud provider (Azure, AWS, Heroku, Render, etc.)

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone <repo-url>
cd myproject
```


###  2. Create .env file

.env
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://postgres:yourpassword@postgres:5432/mydatabase
### 3. Build and start the containers

```bash

docker-compose up --build
```
### 4. Open in browser

```
bash

http://<your-public-ip>:8080/
```

For local development:

```bash

http://localhost:8080/
```

##  📁 Project Structure

```csharp

.
├── app/
│   ├── routes/           # Blueprints
│   ├── templates/        # HTML templates
│   ├── static/           # Static assets (CSS, JS)
│   ├── models/           # SQLAlchemy models
│   └── ...
├── run.py                # uWSGI entrypoint
├── app.ini               # uWSGI config
├── Dockerfile
├── docker-compose.yml
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
└── requirements.txt
```

##  🐘 Working with Database


```bash
docker exec -it flask bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

## 🔄 Common Docker Commands

Command	Description
flask db init	Initialize new migration repository
flask db migrate -m "message"	Create new migration
flask db upgrade	Apply migrations
flask db downgrade	Revert migration

## 🌱 Future Development
This project is under active development and has strong potential for further expansion. Planned features include:

✅ Email or in-app notifications

✅ Multi-teacher collaboration

✅ Enhanced role-based access control

✅ File version history

✅ Dashboard with statistics and analytics



