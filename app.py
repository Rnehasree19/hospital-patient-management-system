from pymongo import MongoClient
from pymongo.server_api import ServerApi
import streamlit as st
import pandas as pd

# PAGE CONFIGURATION
st.set_page_config(
    page_title="Hospital Patient Management System",
    layout="centered"
)

st.title("Hospital Patient Management System")

# MONGODB CONNECTION
uri = "mongodb+srv://rnehasree_db_user:neha123@neha.dqc2txu.mongodb.net/?retryWrites=true&w=majority&appName=neha"

client = MongoClient(
    uri,
    server_api=ServerApi('1')
)

db = client["hospital_db"]
collection = db["patients"]

# CONNECTION TEST
try:
    client.admin.command('ping')
    st.success("MongoDB Connected Successfully")

except Exception as e:
    st.error(f"Connection Error: {e}")

# SIDEBAR MENU
menu = [
    "Add Patient",
    "View Patients",
    "Search Patient",
    "Update Patient",
    "Delete Patient",
    "Patient Statistics",
    "Delete All Records"
]

choice = st.sidebar.selectbox(
    "Select Operation",
    menu
)

# ADD PATIENT

if choice == "Add Patient":

    st.subheader("Add New Patient")

    patient_id = st.text_input("Patient ID")
    name = st.text_input("Patient Name")

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    disease = st.text_input("Disease")
    doctor = st.text_input("Doctor Name")
    phone = st.text_input("Phone Number")
    address = st.text_area("Address")

    if st.button("Add Patient"):

        existing_patient = collection.find_one(
            {"patient_id": patient_id}
        )

        if existing_patient:

            st.warning("Patient ID Already Exists")

        else:

            patient_data = {
                "patient_id": patient_id,
                "name": name,
                "age": age,
                "gender": gender,
                "disease": disease,
                "doctor": doctor,
                "phone": phone,
                "address": address
            }

            collection.insert_one(patient_data)

            st.success("Patient Added Successfully")

# VIEW PATIENTS

elif choice == "View Patients":

    st.subheader("Patient Records")

    patients = list(
        collection.find({}, {"_id": 0})
    )

    if patients:

        df = pd.DataFrame(patients)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:
        st.warning("No Records Found")

# SEARCH PATIENT

elif choice == "Search Patient":

    st.subheader("Search Patient")

    search_id = st.text_input(
        "Enter Patient ID"
    )

    if st.button("Search"):

        patient = collection.find_one(
            {"patient_id": search_id},
            {"_id": 0}
        )

        if patient:

            st.write(patient)

        else:
            st.error("Patient Not Found")

# UPDATE PATIENT

elif choice == "Update Patient":

    st.subheader("Update Patient")

    patient_ids = [
        patient["patient_id"]
        for patient in collection.find()
    ]

    if patient_ids:

        selected_id = st.selectbox(
            "Select Patient ID",
            patient_ids
        )

        patient = collection.find_one(
            {"patient_id": selected_id}
        )

        updated_name = st.text_input(
            "Patient Name",
            patient["name"]
        )

        updated_age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=patient["age"]
        )

        updated_gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

        updated_disease = st.text_input(
            "Disease",
            patient["disease"]
        )

        updated_doctor = st.text_input(
            "Doctor Name",
            patient["doctor"]
        )

        updated_phone = st.text_input(
            "Phone Number",
            patient["phone"]
        )

        updated_address = st.text_area(
            "Address",
            patient["address"]
        )

        if st.button("Update Patient"):

            collection.update_one(
                {"patient_id": selected_id},
                {
                    "$set": {
                        "name": updated_name,
                        "age": updated_age,
                        "gender": updated_gender,
                        "disease": updated_disease,
                        "doctor": updated_doctor,
                        "phone": updated_phone,
                        "address": updated_address
                    }
                }
            )

            st.success("Patient Updated Successfully")

    else:
        st.warning("No Patients Available")

# DELETE PATIENT

elif choice == "Delete Patient":

    st.subheader("Delete Patient")

    patient_ids = [
        patient["patient_id"]
        for patient in collection.find()
    ]

    if patient_ids:

        selected_id = st.selectbox(
            "Select Patient ID",
            patient_ids
        )

        if st.button("Delete Patient"):

            collection.delete_one(
                {"patient_id": selected_id}
            )

            st.success("Patient Deleted Successfully")

    else:
        st.warning("No Patients Available")

# PATIENT STATISTICS

elif choice == "Patient Statistics":

    st.subheader("Patient Statistics")

    total_patients = collection.count_documents({})

    male_count = collection.count_documents(
        {"gender": "Male"}
    )

    female_count = collection.count_documents(
        {"gender": "Female"}
    )

    st.write(f"Total Patients: {total_patients}")
    st.write(f"Male Patients: {male_count}")
    st.write(f"Female Patients: {female_count}")

# DELETE ALL RECORDS

elif choice == "Delete All Records":

    st.subheader("Delete All Patient Records")

    confirm = st.checkbox(
        "I confirm deletion of all records"
    )

    if confirm:

        if st.button("Delete All"):

            collection.delete_many({})

            st.success("All Patient Records Deleted")