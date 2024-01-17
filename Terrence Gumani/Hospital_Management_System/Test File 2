from datetime import datetime

# Single Responsibility Principle (SRP): Each class has a single responsibility.

# Base class for a person
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# Class for a patient, inheriting from Person
class Patient(Person):
    def __init__(self, name, age, address, medical_history=None):
        super().__init__(name, age, address)
        self.medical_history = medical_history or "No medical history available."

# Class for a doctor, inheriting from Person
class Doctor(Person):
    def __init__(self, name, age, address, role, department):
        super().__init__(name, age, address)
        self.role = role
        self.department = department

# Class for an appointment
class Appointment:
    def __init__(self, patient, doctor, date_time):
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

# Interface for Medical Records
class MedicalRecords:
    def __init__(self):
        self.medical_history_records = {}

    # Single Responsibility Principle (SRP): This class has a single responsibility - managing medical records.
    def record_medical_history(self, patient, history):
        self.medical_history_records[patient.name] = history

    def retrieve_medical_history(self, patient):
        return self.medical_history_records.get(patient.name, "No medical history found.")

# Class for user authentication
class Authentication:
    def __init__(self):
        self.users = {"admin": "admin123", "doctor1": "pass123", "nurse1": "pass456"}

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False

# Class for reporting - currently empty methods for future extension
class Reporting:
    def generate_daily_appointments_report(self, date):
        # This class can be extended to fulfill the Open/Closed Principle (OCP).
        pass

    def generate_monthly_billing_summary(self, month, year):
        # This class can be extended to fulfill the Open/Closed Principle (OCP).
        pass

# Class for billing
class Billing:
    def generate_bill(self, appointment):
        # Generate a bill for the appointment
        return f"Bill for {appointment.patient.name}'s appointment with Dr. {appointment.doctor.name}"

# Class for staff management
class StaffManagement:
    def __init__(self):
        self.staff_members = []

    def add_staff_member(self, name, role, department):
        new_staff_member = Person(name, 0, "")  # Age and address are placeholders
        new_staff_member.role = role
        new_staff_member.department = department
        self.staff_members.append(new_staff_member)
        print(f"New staff member {name} added successfully.")

# Class for prescription management
class PrescriptionManagement:
    def __init__(self):
        self.prescriptions = {}

    def manage_prescription(self, doctor, patient, medication):
        prescription_key = (doctor.name, patient.name)
        if prescription_key not in self.prescriptions:
            self.prescriptions[prescription_key] = []

        self.prescriptions[prescription_key].append(medication)
        print(f"Prescription added for {patient.name} by Dr. {doctor.name}: {medication}")

# Function to view upcoming appointments
def view_appointments(appointments):
    print("\nUpcoming Appointments:")
    for appointment in appointments:
        print(f"Patient: {appointment.patient.name}, Doctor: {appointment.doctor.name}, Date: {appointment.date_time}")

# Interactive usage

medical_records = MedicalRecords()
auth = Authentication()
appointments = []
billing_system = Billing()
staff_management = StaffManagement()
prescription_management = PrescriptionManagement()

while True:
    print("\nHospital Management System")
    print("1. Register Patient")
    print("2. Schedule Appointment")
    print("3. Record Medical History")
    print("4. View Medical History")
    print("5. View Appointments")
    print("6. Generate Bill")
    print("7. Add Staff Member")
    print("8. Assign Doctor to Department")
    print("9. Manage Prescription")
    print("10. Exit")

    choice = input("Enter your choice (1-10): ")

    if choice == "1":
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        address = input("Enter patient address: ")
        medical_history = input("Enter medical history: ")

        new_patient = Patient(name, age, address, medical_history)
        medical_records.record_medical_history(new_patient, medical_history)
        print(f"Patient {name} registered successfully.")

    elif choice == "2":
        # Assuming doctor and patient are already registered
        doctor_name = input("Enter doctor name: ")
        date_str = input("Enter appointment date and time (YYYY-MM-DD HH:MM): ")
        date_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

        doctor = Doctor(doctor_name, 0, "", "", "")
        patient = new_patient if 'new_patient' in locals() else None

        if patient:
            new_appointment = Appointment(patient, doctor, date_time)
            appointments.append(new_appointment)
            print(f"Appointment scheduled with {doctor_name} on {date_str} for {patient.name}.")

    elif choice == "3":
        if 'new_patient' in locals():
            # Single Responsibility Principle (SRP): MedicalRecords class is responsible for recording medical history.
            history = input("Enter additional medical history:")
            
            medical_records.record_medical_history(new_patient, history)
            print("Medical history recorded successfully.")
        else:
            print("Patient not registered. Please register a patient first.")

    elif choice == "4":
        if 'new_patient' in locals():
            print(medical_records.retrieve_medical_history(new_patient))
        else:
            print("Patient not registered. Please register a patient first.")

    elif choice == "5":
        view_appointments(appointments)

    elif choice == "6":
        if appointments:
            # Generate a bill for the latest appointment
            latest_appointment = appointments[-1]
            bill = billing_system.generate_bill(latest_appointment)
            print(bill)
        else:
            print("No appointments to generate a bill.")

    elif choice == "7":
        name = input("Enter staff member name: ")
        role = input("Enter staff member role: ")
        department = input("Enter staff member department: ")

        staff_management.add_staff_member(name, role, department)

    elif choice == "8":
        if staff_management.staff_members:
            doctor_name = input("Enter doctor name: ")
            department = input("Enter department to assign the doctor: ")

            for staff_member in staff_management.staff_members:
                if staff_member.name == doctor_name and staff_member.role == "Doctor":
                    staff_member.department = department
                    print(f"Doctor {doctor_name} assigned to {department}.")
                    break
            else:
                print(f"Doctor {doctor_name} not found or is not assigned as a Doctor.")
        else:
            print("No staff members available. Please add staff members first.")

    elif choice == "9":
        if staff_management.staff_members:
            doctor_name = input("Enter doctor name: ")
            patient_name = input("Enter patient name: ")
            medication = input("Enter prescribed medication: ")

            for staff_member in staff_management.staff_members:
                if staff_member.name == doctor_name and staff_member.role == "Doctor":
                    prescription_management.manage_prescription(staff_member, Patient(patient_name, 0, ""), medication)
                    break
            else:
                print(f"Doctor {doctor_name} not found or is not assigned as a Doctor.")
        else:
            print("No staff members available. Please add staff members first.")

    elif choice == "10":
        print("Exiting Hospital Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 10.")

