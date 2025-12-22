# 🎮 Backlog Tracker
A simple, clean Django web application for tracking your video game backlog. Add games, update their status, manage priorities, and keep your gaming life organised.

---

## 📌 Features
- Add, edit, and delete backlog entries  
- Track platform, status, and priority  
- User authentication (login/logout)  
- Secure POST-based logout  
- Bootstrap‑styled UI  
- Responsive layout  
- Status badges for quick visual scanning  

---

## 🚧 Upcoming Features
- Sorting (by name, platform, status, priority)  
- Filtering (e.g., show only “In Progress”)  
- Search bar  
- Pagination  
- User‑specific backlogs  
- Dashboard with stats and analytics  

---

## 🛠️ Tech Stack
- **Python 3**  
- **Django**  
- **SQLite** (default, can be swapped later)  
- **Bootstrap 5**  
- **HTML templates** (Django templating engine)

---

## 📂 Project Structure

project/
│
├── backlog/                # Main app
│   ├── templates/
│   │   ├── base.html
│   │   ├── library_list.html
│   │   ├── library_add.html
│   │   ├── library_edit.html
│   │   └── login.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── project_root/           # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md

