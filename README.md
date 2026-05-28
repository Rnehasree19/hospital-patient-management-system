# Hospital Patient Management System

### Live Application

https://hospital-management-jit.streamlit.app/

---

## Overview

The Hospital Patient Management System is a database-driven web application developed using Python, Streamlit, MongoDB Atlas, and PyMongo. The system is designed to efficiently manage patient records through complete CRUD (Create, Read, Update, Delete) operations integrated with a cloud-hosted MongoDB database.

The application provides a simple and interactive interface for storing, retrieving, updating, searching, and deleting patient information in real time.

---

## Key Features

* Patient Registration and Record Management
* Add New Patient Records
* View Existing Patient Records
* Search Patient Details using Patient ID
* Update Existing Patient Information
* Delete Individual Patient Records
* Delete All Records Functionality
* Patient Statistics Dashboard
* MongoDB Atlas Cloud Database Integration
* Real-Time Database Connectivity
* Interactive Streamlit User Interface

---

## Technologies Used

| Category        | Technologies      |
| --------------- | ----------------- |
| Frontend        | Streamlit         |
| Backend         | Python            |
| Database        | MongoDB Atlas     |
| Database Driver | PyMongo           |
| Libraries       | Pandas, dnspython |

---

## Project Structure

```txt id="msqj9p"
hospital-management/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation and Setup

### Step 1 — Clone Repository

```bash id="2cx75w"
git clone https://github.com/your-username/hospital-patient-management-system.git
```

### Step 2 — Open Project Folder

```bash id="bgjpdq"
cd hospital-patient-management-system
```

### Step 3 — Create Virtual Environment

```bash id="jlwmqq"
python -m venv venv
```

### Step 4 — Activate Virtual Environment

#### Windows

```bash id="jlwmww"
venv\Scripts\activate
```

#### Linux / Mac

```bash id="jlwmee"
source venv/bin/activate
```

### Step 5 — Install Dependencies

```bash id="jlwmrr"
pip install -r requirements.txt
```

### Step 6 — Run the Application

```bash id="jlwmtt"
streamlit run app.py
```

Application will run at:

```txt id="jlwmyy"
http://localhost:8501
```

---

## Requirements

```txt id="jlwmuu"
streamlit
pymongo
pandas
dnspython
```

---

## MongoDB Operations Implemented

The project implements the following MongoDB database operations:

* `insert_one()`
* `find()`
* `find_one()`
* `update_one()`
* `delete_one()`
* `delete_many()`
* `count_documents()`

---

## Functional Modules

### Add Patient

Stores patient information securely into MongoDB Atlas database.

### View Patients

Displays all patient records in a structured tabular format.

### Search Patient

Retrieves patient details using unique Patient ID.

### Update Patient

Allows modification of existing patient information.

### Delete Patient

Deletes selected patient records from the database.

### Delete All Records

Removes all patient records from the collection.

### Patient Statistics

Displays patient-related statistical information.

---

## MongoDB Atlas Integration

MongoDB Atlas is used as the cloud database service for storing and managing patient records. The application establishes secure real-time connectivity with MongoDB Atlas using the PyMongo driver.

---

## Developed as Part of DBMS (BCS403) Assignment

Under the Guidance of

#Dr. S. Prabhanjan

M.Tech, Ph.D  

Professor & Head  

Department of Computer Science and Engineering  

Jyothy Institute of Technology, Bangalore
---

## Team Members

* R Neha Sree (1JT24CS116)
* Pavithra K (1JT24CS102)
* Prathibha Y (1JT24CS113)

---

## License

This project is developed for academic and educational purposes.
