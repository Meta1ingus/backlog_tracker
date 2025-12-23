# 🎮 Backlog Tracker

A personal game backlog management system built with **Django**, designed to help users track, organize, and prioritize their gaming library across platforms, editions, mediums, and subscription services.

---

## 📑 Table of Contents
- [Live Demo](#live-demo)
- [Overview](#-overview)
- [Design Decisions](#-design-decisions)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Database Structure](#-database-structure)
- [Model Relationship Diagram](#model-relationship-diagram)
- [System Architecture](#system-architecture)
- [Why SQLite Is Appropriate for This Project](#-why-sqlite-is-appropriate-for-this-project)
- [Project Structure](#-project-structure)
- [Template Inheritance Diagram](#template-inheritance-diagram)
- [Installation](#-installation-local-development)
- [Upcoming Features](#-upcoming-features)
- [Known Limitations](#-known-limitations)
- [Future Architecture Considerations](#-future-architecture-considerations)
- [Attribution & License](#-attribution--license)

---
## 🔗 Live Demo
[Backlog Tracker](https://backlogged.uk)
---

## 📌 Overview  
**Backlog Tracker** is a full-stack web application that allows users to maintain a structured, searchable, and filterable library of games. Whether it is a physical collector's edition or a digital title on a subscription service, this tool helps gamers manage "analysis paralysis" by providing a clean, intuitive interface for their collection.

The project demonstrates strong backend design, relational modeling, and modern web development practices using the Django framework.

---

## 🧠 Design Decisions

### Django as the Framework
Django was chosen for its strong built‑in features: authentication, ORM, admin interface, and clear project structure. These tools reduce boilerplate and allow the project to focus on modelling and user experience rather than infrastructure.

### Normalised Relational Schema
The database is designed around clear relationships (Game → Edition → Library) to avoid duplication and ensure data integrity. Many‑to‑Many fields are used for mediums and subscription services to allow flexible combinations without cluttering the Library model.

### Template Inheritance
A single `base.html` layout ensures consistent styling and navigation across all pages. Child templates only define their unique content, reducing duplication and improving maintainability.

### Minimal JavaScript
The UI relies primarily on Django templates and Bootstrap. JavaScript is only used where necessary, keeping the project simple, accessible, and easy to maintain.

### Cloudflare Tunnel for Deployment
Cloudflare Tunnel provides a secure, zero‑configuration way to expose the local server for demonstration without needing a public IP or complex hosting setup.

---

## ✨ Features  

### 🔐 User Management
* **Secure Accounts:** Register, login, and logout functionality.
* **Private Libraries:** Each user's data is isolated; you only see the games you've added.
* **Staff Control:** Integrated Django Admin panel for administrative tasks.

### 📚 Library Management (CRUD)
* **Full Lifecycle:** Add new game entries, edit metadata, or remove games from your list.
* **Detailed Metadata:** Track platform, edition, release year, and personal notes.
* **Status Badges:** Visual indicators for "Backlog," "Playing," "Completed," and "Dropped."

### 🔎 Search, Filter & Sort
* **Dynamic Search:** Find titles instantly by keyword.
* **Advanced Filtering:** Narrow down your list by platform, status, priority, or medium.
* **Smart Sorting:** Multi-column default sorting (e.g., Priority > Title) for consistent organization.

### 📱 Responsive UI
* **Mobile-First Design:** Built with **Bootstrap 5** to ensure the library looks great on phones, tablets, and desktops.
* **Accessible Navigation:** Clean headers and intuitive form layouts.

---

## 🛠️ Tech Stack

| Layer        | Technologies                                  |
|--------------|-----------------------------------------------|
| **Backend**  | Python 3, Django, Django ORM                  |
| **Database** | SQLite (Local & Deployment)                   |
| **Frontend** | HTML5, CSS3, Bootstrap 5, JavaScript (minimal)          |
| **Deployment** | Local server + Cloudflare Tunnel            |
| **Tools**    | Git, GitHub                                   |

---

## 🗄️ Database Structure  

The application uses a normalised relational schema to ensure data integrity and scalability.

### Key Models
* **Game:** The core title (base game info).
* **Edition:** Specific versions (e.g., "Game of the Year Edition").
* **Library:** The user-specific entry linking to an edition, containing personal stats like priority and status.
* **Platform:** The hardware or service (PC, PS5, Switch).
* **ManyToMany Relations:** Used for **Mediums** (Physical, Digital) and **Subscription Services** (Game Pass, PS Plus) to allow multiple selections per game.

## Model Relationship Diagram

```
User
 │
 └── Library
      ├── edition_id ───────────────→ Edition
      │                                 │
      │                                 └── game_id → Game
      │
      ├── status (Backlog/Playing/Completed/Dropped)
      ├── priority (1–5)
      ├── notes
      │
      ├── mediums (M2M) ─────────────→ Medium
      └── subscription_services (M2M) → SubscriptionService
```

## System Architecture

**Client (Browser)**  
     ▼  

**Cloudflare Tunnel**  
     ▼  

**Django Application (tracker/)**  
     ▼  

**SQLite Database (db.sqlite3)**  

### How It Works  

*   **Client (Browser):** Users interact with the interface through standard HTTP requests.  
    
*   **Cloudflare Tunnel:** Securely exposes the local Django server to the internet without port forwarding or a public IP.  
    
*   **Django Application:** Handles routing, authentication, business logic, and template rendering.  
    
*   **SQLite Database:** Stores all persistent data, including users, games, editions, and library entries.  
    

This architecture is lightweight, secure, and perfectly suited to a single‑developer academic project.  

---

## 🗃️ Why SQLite Is Appropriate for This Project

SQLite is an ideal choice for this assignment because:

• Zero configuration: No server setup or external dependencies.

• Lightweight and fast: Perfect for a personal game library with modest data volume.

• Fully supported by Django: Works seamlessly with migrations, the ORM, and the admin interface.

• Identical across environments: Using SQLite for both development and deployment avoids environment drift.

• Meets project requirements: The assignment does not require high concurrency, large-scale writes, or multi-user database scaling.

In short, SQLite provides simplicity, reliability, and portability — making it the most practical database choice for a project of this scope.

---

## 📂 Project Structure

```text
backlog-tracker/
│
├── backlog_tracker/                 # Project config
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tracker/                         # Main application
│   ├── management/commands/         # Custom commands (seed.py)
│   ├── migrations/                  # Database migrations
│   ├── static/css/                  # Stylesheets
│   ├── templates/
│   │   ├── registration/login.html
│   │   ├── base.html
│   │   ├── library_list.html
│   │   ├── library_form.html
│   │   └── library_confirm_delete.html
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── db.sqlite3
├── manage.py
├── README.md
└── requirements.txt
```

## Template Inheritance Diagram

```
base.html
 ├── library_list.html
 ├── library_form.html
 ├── library_confirm_delete.html
 └── registration/login.html
```

## 🚀 Installation (Local Development)

### 1. Clone the repository

```
git clone <your-repo-url>
cd backlog-tracker
```

### 2. Setup Virtual Environment

```
python -m venv venv

source venv/bin/activate  # macOS/Linux

venv\Scripts\activate     # Windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Initialize Database

```
python manage.py migrate

python manage.py createsuperuser  # Create an admin account
```

### 5. Run Server

```
python manage.py runserver
```

Visit http://127.0.0.1:8000 in your browser.

## 🚧 Upcoming Features

**Dashboard**: Analytics showing "Percentage Completed" and genre breakdowns.  
**IGDB Integration**: Automatically fetch game covers and metadata via API.  
**Social Sharing**: Option to make libraries public for friends to view.

## ⚠️ Known Limitations

- **Single‑User Database:** SQLite is ideal for this project, but not suited for high‑concurrency production environments.
- **Manual Data Entry:** Games, editions, and metadata must be entered manually. Future API integration (e.g., IGDB) would automate this.
- **No Image Uploads:** The project intentionally avoids handling media files to keep the scope focused on core functionality.
- **Basic Analytics:** The current version does not include dashboards or progress statistics, though the data model supports them.

## 🚀 Future Architecture Considerations

- **PostgreSQL Migration:** If the application were to support many users or heavy write activity, migrating from SQLite to PostgreSQL would provide better concurrency and reliability.
- **Containerisation:** Packaging the app with Docker would simplify deployment and ensure consistent environments.
- **API Integration Layer:** Introducing a service layer for IGDB or other metadata sources would reduce manual data entry and enrich the library.
- **Background Tasks:** Tools like Celery could handle scheduled updates, data imports, or long‑running operations.
- **User‑Shared Libraries:** A permission system could allow users to make their libraries public or share them with friends.

## 📝 Attribution & License

**Frameworks**: [Django Documentation](https://docs.djangoproject.com) & [Bootstrap 5](https://getbootstrap.com)  
**Resources**: [StackOverflow](https://stackoverflow.com/questions) for pagination logic and query preservation.  
**License**: This project is for educational purposes as part of a college project.  