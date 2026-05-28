# Hospital Patient Management System

Live Link: https://your-streamlit-link.streamlit.app/

A database-driven Hospital Patient Management System developed using Python, Streamlit, MongoDB Atlas, and PyMongo. This project helps manage hospital patient records efficiently using complete CRUD operations integrated with MongoDB cloud database.

---

## Features

* Add Patient Records
* View Patient Records
* Search Patient Details
* Update Patient Information
* Delete Patient Records
* Delete All Records
* Patient Statistics
* MongoDB Atlas Integration
* Cloud Database Connectivity

---

## Technologies Used

### Frontend

* Streamlit

### Backend

* Python

### Database

* MongoDB Atlas
* PyMongo

### Libraries

* Pandas
* dnspython

---

## Project Structure

```txt
hospital-management/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### Step 1 — Clone Repository

```bash
git clone https://github.com/your-username/hospital-patient-management-system.git
```

### Step 2 — Open Project Folder

```bash
cd hospital-patient-management-system
```

### Step 3 — Create Virtual Environment

```bash
python -m venv venv
```

### Step 4 — Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Step 5 — Install Requirements

```bash
pip install -r requirements.txt
```

### Step 6 — Run Streamlit Application

```bash
streamlit run app.py
```

Application runs at:

```txt
http://localhost:8501
```

---

## Requirements

```txt
streamlit
pymongo
pandas
dnspython
```

---

## Database Operations Implemented

* insert_one()
* find()
* find_one()
* update_one()
* delete_one()
* delete_many()
* count_documents()

---

## Functionalities

### Add Patient

Stores patient information into MongoDB Atlas database.

### View Patients

Displays all patient records in tabular format.

### Search Patient

Searches patient details using Patient ID.

### Update Patient

Updates existing patient information.

### Delete Patient

Deletes selected patient record.

### Delete All Records

Deletes all patient records from database.

### Patient Statistics

Displays patient count statistics.

---

## MongoDB Atlas Integration

MongoDB Atlas cloud database is used for storing and managing patient records. The application connects to MongoDB Atlas using PyMongo driver.

---

## Developed as part of assignment of DBMS (BCS403)

Under the Guidance of

Dr. S. Prabhanjan
M.Tech, Ph.D
Professor & Head
Department of Computer Science and Engineering
Jyothy Institute of Technology, Bangalore

---

## Authors

* R Neha Sree (1JT24CS116)
* Pavithra K (1JT24CS102)
* Prathibha Y (1JT24CS113)
