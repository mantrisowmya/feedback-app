Online Feedback Collector with Admin Dashboard:-A Flask-based web application to collect feedback online, store it securely in SQLite, and provide an admin dashboard for viewing responses. Includes a REST API for JSON data retrieval.



🚀 Features:=


Online feedback form for users
Secure admin login
Dashboard view of collected feedback
REST API endpoint (/api/feedback)
SQLite database storage
Responsive HTML/CSS frontend





🛠 Technology Stack:=


Backend: Flask (Python)
Frontend: HTML, CSS, Jinja2 Templates, JavaScript
Database: SQLite (database.db)
API: REST API using Flask routes





📂 Project Structure:=



php
Copy code
feedback-app/
│── static/              # CSS, JS, Images  
│── templates/           # HTML Templates  
│── app.py               # Flask Application  
│── database.db          # SQLite Database  
│── requirements.txt     # Python Dependencies  
│── render.yaml          # Deployment Config (Render)  
│── runtime.txt          # Python Runtime Version  
│── README.md            # Project Documentation  





⚡ Setup Instructions:=




1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/mantrisowmya/feedback-app.git
cd feedback-app

2️⃣ Create Virtual Environment & Install Dependencies
bash
Copy code
python -m venv venv
# Activate virtual environment:
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
pip install -r requirements.txt

3️⃣ Run the Application
bash
Copy code
python app.py
Visit: http://127.0.0.1:5000 in your browser.





🔑 Default Admin Login:=
makefile
Copy code


Username: admin
Password: admin123
📡 API Endpoint
GET /api/feedback → Returns JSON list of feedback entries.



📌 Future Enhancements:=
Password hashing for better security
Search & filter in dashboard
Data visualization charts
Export feedback to CSV/Excel
Cloud deployment (Render, Railway)
