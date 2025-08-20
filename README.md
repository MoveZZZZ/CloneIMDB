# 🎬 CloneIMDB

A desktop application built with **Python (PyQt5)** that replicates core features of the IMDB platform.  
Users can register, log in, browse movies, search by genre, mark favorites, rate films, and manage their profile.  

---

## ✨ Features
- 👤 **User Authentication**
  - Sign up, log in, log out  
  - Password reset & change username/email  

- 🎥 **Movies**
  - Search films by **title** or **genre**  
  - Rate movies with stars ⭐  
  - Add to **Favorites**, **Later Watch**, or **Watched** lists  

- 📊 **Top 10 Section**
  - Displays the most popular or highest-rated films  

- 🖼️ **UI/UX**
  - Built with **PyQt5**  
  - Multiple pages (Login, Main Page, Profile, Forgot Password, etc.)  
  - Styled buttons and custom icons  

- 💾 **Database**
  - SQL database with preloaded movies  
  - Scripts available in `/DATABASE/`  

---

## 📂 Project Structure
```
CloneIMDB-master/
│── main.py                  # Entry point
│── Login_page.py            # Login page logic
│── main_page.py             # Main app page
│── forgotPassword.py        # Forgot password functionality
│── addFilmToFavoriteLaterWatched.py
│── ScoreFilmAndChangeIcon.py
│── SearchFilmByGenresNameIDT.py
│── StyleSheetForButtons.py
│── DATABASE/                # SQL scripts & DB data
│── Images_Films/            # Movie posters
│── *.ui                     # PyQt5 UI forms
│── icons / images           # Assets
```

---

## ⚙️ Requirements
- Python **3.8+**  
- **PyQt5**  
- **SQLite / MySQL** (depending on DB setup)  

Install dependencies:
```bash
pip install -r requirements.txt
```

*(If `requirements.txt` is missing, install manually:)*  
```bash
pip install pyqt5
```

---

## 🚀 Run the App
1. Make sure the database is set up. You can import one of the SQL dumps from `/DATABASE/`:
   ```bash
   mysql -u root -p < DATABASE/dataCloneIMDB.sql
   ```
   or use SQLite depending on configuration.
2. Start the application:
   ```bash
   python main.py
   ```

---

## 🛠️ Development
- Language: **Python**  
- Framework: **PyQt5**  
- Database: **SQL** (MySQL / SQLite)  

---
