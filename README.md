Django Assessment Project
This project is a Django-based web application that visualizes the data from several tables (School, Class, Student, Assessment Areas, Answers, Awards, Subject, and Summary) based on the provided dataset.

Table of Contents
Project Overview
Folder Structure
Prerequisites
Getting Started
1. Clone the repository
2. Build and run the Docker container
3. Access the application
Available Endpoints
Notes
Project Overview
This project is built with Django and uses Docker for containerization. It reads data from CSV files, populates the database, and visualizes various tables without explicit relationships. The application serves as a visual interface for inspecting the table structure and data points.

Folder Structure
php
Copy code
django_project/
│
├── docker-compose.yml       # Docker Compose file
├── Dockerfile               # Dockerfile to build the project
├── manage.py                # Django's management script
├── requirements.txt         # Python dependencies
├── README.md                # This instructions file
├── assessment/                     # Django application folder
│   ├── models.py            # Models representing database tables
│   ├── views.py             # Views for handling requests
│   ├── templates/           # HTML templates for rendering data
│   └── static/              # Static files (CSS, JS, etc.)
├── django_project/          # Main project folder
│   └── settings.py          # Django settings
└── data/                    # Folder with CSV files
    └── load_csv.csv
Prerequisites
Before starting, ensure you have the following installed on your machine:

Docker
Docker Compose
Getting Started
1. Clone the repository
bash
Copy code
git clone  https://github.com/Usamafuward/django-assessment.git
cd django_project
2. Build and run the Docker container
The project is dockerized, making it easy to set up. Simply use Docker Compose to build and run the application.

Step 1: Build the Docker image
bash
Copy code
docker-compose build
Step 2: Start the containers
bash
Copy code
docker-compose up
This will start both the Django application and the PostgreSQL database in containers. The database will be accessible via localhost:5432, and the web application will be served on port 8000.

3. Access the application
After the container has started, you can access the web application in your browser:

arduino
Copy code
http://localhost:8000
The homepage will display links to different data tables, such as:

Schools
Classes
Students
Assessment Areas
Answers
Awards
Subjects
Summary
Available Endpoints
The following endpoints are available to view the data:

/schools/ - List all schools
/classes/ - List all classes
/students/ - List all students
/assessment-areas/ - List all assessment areas
/answers/ - List all answers
/awards/ - List all awards
/subjects/ - List all subjects
/summary/ - View the summary data
Notes
You can customize the docker-compose.yml file if necessary, such as changing database credentials or ports.
Make sure you place all the provided CSV files in the data/ directory before running the application. These will be loaded into the database for visualization.
The data will be stored in a PostgreSQL database managed by Docker, and the Django models will be used to fetch the data and render it on the HTML pages.
Feel free to modify the HTML templates or CSS files in the static/ directory to customize the look and feel of the web interface.
