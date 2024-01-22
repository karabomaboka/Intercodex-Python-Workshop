from datetime import datetime
import random


class Person:
    def __init__(self, person_id, name, age, gender):
        self.person_id = person_id
        self.name = name
        self.age = age
        self.gender = gender


class Patient(Person):
    def __init__(self, person_id, name, age, gender, medical_aid=None):
        super().__init__(person_id, name, age, gender)
        self.medical_aid = medical_aid


class Doctor(Person):
    def __init__(self, person_id, name, age, gender, specialty):
        super().__init__(person_id, name, age, gender)
        self.specialty = specialty


class Staff(Person):
    def __init__(self, person_id, name, age, gender, role):
        super().__init__(person_id, name, age, gender)
        self.role = role


class Appointment:
    def __init__(self, doctor, patient, date):
        self.doctor = doctor
        self.patient = patient
        self.date = date


class Hospital:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.doctors = []
        self.staff = []
        self.appointments = []

    def admit_patient(self, patient):
        self.patients.append(patient)

    def discharge_patient(self, patient):
        if patient in self.patients:
            self.patients.remove(patient)

    def hire_staff(self, staff):
        self.staff.append(staff)

    def schedule_appointment(self, doctor, patient, date):
        appointment = Appointment(doctor, patient, date)
        self.appointments.append(appointment)

    def display_patient_info(self):
        print("Patients in the hospital:")
        for patient in self.patients:
            print(f"ID: {patient.person_id}, Name: {patient.name}, Age: {patient.age}, Gender: {patient.gender}, Medical Aid: {patient.medical_aid or 'None'}")

    def display_doctor_info(self):
        print("Doctors in the hospital:")
        for doctor in self.doctors:
            print(f"ID: {doctor.person_id}, Name: Dr. {doctor.name}, Age: {doctor.age}, Gender: {doctor.gender}, Specialty: {doctor.specialty}")

    def display_staff_info(self):
        print("Staff in the hospital:")
        for staff in self.staff:
            print(f"ID: {staff.person_id}, Name: {staff.name}, Age: {staff.age}, Gender: {staff.gender}, Role: {staff.role}")

    def display_appointment_info(self):
        print("Appointments in the hospital:")
        for appointment in self.appointments:
            print(f"Date: {appointment.date}, Doctor: Dr. {appointment.doctor.name}, Patient: {appointment.patient.name}")

    def assign_medical_aid(self, patient):
        if random.choice([True, False]):  # Randomly decide if the patient has medical aid
            medical_aids = ["SANTAM", "BONITAS", "GEMS"]
            patient.medical_aid = random.choice(medical_aids)


class InteractiveHospital:
    def __init__(self, hospital):
        self.hospital = hospital

    def display_menu(self):
        print("\nHospital Management System Menu:")
        print("1. Admit Patient")
        print("2. Discharge Patient")
        print("3. Hire Staff")
        print("4. Schedule Appointment")
        print("5. Display Patient Information")
        print("6. Display Doctor Information")
        print("7. Display Staff Information")
        print("8. Display Appointment Information")
        print("9. Exit")

    def run(self):
        print("Welcome to the Hospital Management System!")
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-9): ")

            if choice == '1':
                self.admit_patient()
            elif choice == '2':
                self.discharge_patient()
            elif choice == '3':
                self.hire_staff()
            elif choice == '4':
                self.schedule_appointment()
            elif choice == '5':
                self.hospital.display_patient_info()
            elif choice == '6':
                self.hospital.display_doctor_info()
            elif choice == '7':
                self.hospital.display_staff_info()
            elif choice == '8':
                self.hospital.display_appointment_info()
            elif choice == '9':
                print("Exiting the Hospital Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")

    def admit_patient(self):
        print("Admitting a patient:")

        existing_patient_choice = input("Is the patient a new patient or an existing patient? (new/existing): ").lower()

        if existing_patient_choice == 'existing':
            patient_id = int(input("Enter patient ID: "))
            existing_patient = self.find_patient_by_id(patient_id)

            if existing_patient:
                print(f"Existing patient found: {existing_patient.name}")
                send_to_doctor = input("Send patient details to Dr. (yes/no): ").lower()

                if send_to_doctor == 'yes':
                    self.send_patient_details_to_doctor(existing_patient)
                else:
                    print("Patient details not sent to the doctor.")
            else:
                print(f"No existing patient found with ID {patient_id}. Proceeding with new patient admission.")
        elif existing_patient_choice == 'new':
            # Proceed with capturing details for a new patient
            patient_id = int(input("Enter patient ID: "))
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender: ")
            medical_aid_choice = input("Does the patient have medical aid? (yes/no): ").lower()
            
            if medical_aid_choice == 'yes':
                new_patient = Patient(patient_id, name, age, gender)
                self.hospital.assign_medical_aid(new_patient)
            else:
                new_patient = Patient(patient_id, name, age, gender)
                
            self.hospital.admit_patient(new_patient)
            print(f"{name} has been admitted to {self.hospital.name}.")
        else:
            print("Invalid choice. Please enter 'new' or 'existing'.")

    def find_patient_by_id(self, patient_id):
        for patient in self.hospital.patients:
            if patient.person_id == patient_id:
                return patient
        return None

    def send_patient_details_to_doctor(self, patient):
        print(f"Sending patient details to Dr. {self.hospital.doctors[0].name}")

    def discharge_patient(self):
        patient_id = int(input("Enter patient ID to discharge: "))
        patient = self.find_patient_by_id(patient_id)

        if patient:
            self.hospital.discharge_patient(patient)
            print(f"{patient.name} has been discharged from {self.hospital.name}.")
        else:
            print(f"Patient with ID {patient_id} not found.")

    def hire_staff(self):
        staff_id = int(input("Enter staff ID: "))
        name = input("Enter staff name: ")
        age = int(input("Enter staff age: "))
        gender = input("Enter staff gender: ")
        role = input("Enter staff role: ")
        new_staff = Staff(staff_id, name, age, gender, role)
        self.hospital.hire_staff(new_staff)
        print(f"{name} has been hired as {role} in {self.hospital.name}.")

    def schedule_appointment(self):
        doctor_id = int(input("Enter doctor ID: "))
        patient_id = int(input("Enter patient ID: "))
        appointment_date_str = input("Enter appointment date (YYYY-MM-DD HH:MM): ")
        appointment_date = datetime.strptime(appointment_date_str, "%Y-%m-%d %H:%M")

        doctor = None
        patient = None

        for d in self.hospital.doctors:
            if d.person_id == doctor_id:
                doctor = d
                break

        for p in self.hospital.patients:
            if p.person_id == patient_id:
                patient = p
                break

        if doctor and patient:
            self.hospital.schedule_appointment(doctor, patient, appointment_date)
            print(f"Appointment scheduled between {patient.name} and Dr. {doctor.name} on {appointment_date}.")
        else:
            print("Doctor or patient not found. Please check IDs.")

# Example Usage:

# Create hospital
city_hospital = Hospital("City Hospital")

# Create doctor
dr_zulu = Doctor(101, "Dr. Zulu", 35, "Male", "Cardiologist")
city_hospital.doctors.append(dr_zulu)

# Create patient
patient_lungile = Patient(201, "Lungile", 28, "Female")
city_hospital.patients.append(patient_lungile)

# Create staff
nurse_susan = Staff(301, "Nurse Susan", 40, "Female", "Nurse")
city_hospital.staff.append(nurse_susan)

# Create interactive interface
interactive_hospital = InteractiveHospital(city_hospital)

# Run the interactive system
interactive_hospital.run()

