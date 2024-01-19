from datetime import datetime

# Base class for a person
class Person:
    def __init__(self, id_number, name, age, address):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.address = address

# Class for a patient, inheriting from Person
class Patient(Person):
    def __init__(self, id_number, name, age, address, medical_history=None):
        super().__init__(id_number, name, age, address)
        self.medical_history = medical_history or "No medical history available."

# Class for a doctor, inheriting from Person
class Doctor(Person):
    def __init__(self, id_number, name, age, address, role, department):
        super().__init__(id_number, name, age, address)
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

    def record_medical_history(self, patient, history):
        self.medical_history_records[patient.id_number] = history

    def retrieve_medical_history(self, patient):
        return self.medical_history_records.get(patient.id_number, "No medical history found.")

# Class for user authentication
class Authentication:
    def __init__(self):
        self.users = {"admin": "admin123", "doctor1": "pass123", "nurse1": "pass456"}

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        return False

# Class for reporting
class Reporting:
    def __init__(self):
        self.daily_appointments = {}
        self.monthly_billing = {}

    def generate_daily_appointments_report(self, date):
        # For future extension: Generate and display a report of daily appointments
        appointments = [f"Appointment {i + 1}" for i in range(5)]  # Sample data
        report = f"Daily Appointments Report - {date}\n"
        report += "\n".join(appointments)
        return report

    def generate_monthly_billing_summary(self, month, year):
        # For future extension: Generate and display a summary of monthly billing
        billing_summary = {
            "Patient1": 1500.00,
            "Patient2": 2000.00,
            "Patient3": 1200.00,
            "Patient4": 1800.00,
            "Patient5": 2500.00,
        }  # Sample data

        total_amount = sum(billing_summary.values())
        report = f"Monthly Billing Summary - {month} {year}\n"
        for patient, amount in billing_summary.items():
            report += f"{patient}: ZAR {amount:.2f}\n"

        report += f"Total Amount: ZAR {total_amount:.2f}"
        return report

# Class for billing
class Billing:
    def generate_bill(self, appointment):
        # Enhanced: Include amounts in ZAR
        amount_zar = 2000.00  # Sample billing amount in ZAR
        return f"Bill for {appointment.patient.name}'s appointment with Dr. {appointment.doctor.name}: ZAR {amount_zar:.2f}"

# Class for staff management
class StaffManagement:
    def __init__(self):
        self.staff_members = []

    def add_staff_member(self, id_number, name, role, department):
        new_staff_member = Person(id_number, name, 0, "")
        new_staff_member.role = role
        new_staff_member.department = department
        self.staff_members.append(new_staff_member)
        print(f"New staff member {name} added successfully.")

# Class for prescription management
class PrescriptionManagement:
    def __init__(self):
        self.prescriptions = {}

    def manage_prescription(self, doctor, patient, medication):
        prescription_key = (doctor.name, patient.id_number)
        if prescription_key not in self.prescriptions:
            self.prescriptions[prescription_key] = []

        self.prescriptions[prescription_key].append(medication)
        print(f"Prescription added for {patient.name} by Dr. {doctor.name}: {medication}")

# Class for Hospital Management System
class HospitalManagementSystem:
    def __init__(self):
        self.medical_records = MedicalRecords()
        self.auth = Authentication()
        self.appointments = []
        self.billing_system = Billing()
        self.staff_management = StaffManagement()
        self.prescription_management = PrescriptionManagement()
        self.reporting = Reporting()

    def view_appointments(self):
        print("\nUpcoming Appointments:")
        for appointment in self.appointments:
            print(f"Patient: {appointment.patient.name}, Doctor: {appointment.doctor.name}, Date: {appointment.date_time}")

    def search_patient_by_id(self):
        patient_id = input("Enter patient ID: ")
        found_patient = None

        for appointment in self.appointments:
            if appointment.patient.id_number == patient_id:
                found_patient = appointment.patient
                break

        if found_patient:
            print(f"Patient found: {found_patient.name}, ID: {found_patient.id_number}")
            # You can add additional information display here
        else:
            print("Patient not found.")

    def start_system(self):
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
            print("10. Generate Daily Appointments Report")
            print("11. Generate Monthly Billing Summary")
            print("12. Search for Patient by ID")
            print("13. Exit")

            choice = input("Enter your choice (1-13): ")

            if choice == "1":
                id_number = input("Enter patient ID: ")
                name = input("Enter patient name: ")
                age = int(input("Enter patient age: "))
                address = input("Enter patient address: ")
                medical_history = input("Enter medical history: ")

                new_patient = Patient(id_number, name, age, address, medical_history)
                self.medical_records.record_medical_history(new_patient, medical_history)
                print(f"Patient {name} registered successfully with ID: {id_number}.")

            elif choice == "2":
                doctor_name = input("Enter doctor name: ")
                date_str = input("Enter appointment date and time (YYYY-MM-DD HH:MM): ")
                date_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

                doctor = Doctor(doctor_name, 0, "", "", "")
                patient = new_patient if 'new_patient' in locals() else None

                if patient:
                    new_appointment = Appointment(patient, doctor, date_time)
                    self.appointments.append(new_appointment)
                    print(f"Appointment scheduled with {doctor_name} on {date_str} for {patient.name}.")

            elif choice == "3":
                if 'new_patient' in locals():
                    history = input("Enter additional medical history: ")
                    self.medical_records.record_medical_history(new_patient, history)
                    print("Medical history recorded successfully.")
                else:
                    print("Patient not registered. Please register a patient first.")

            elif choice == "4":
                if 'new_patient' in locals():
                    print(self.medical_records.retrieve_medical_history(new_patient))
                else:
                    print("Patient not registered. Please register a patient first.")

            elif choice == "5":
                self.view_appointments()

            elif choice == "6":
                if self.appointments:
                    latest_appointment = self.appointments[-1]
                    bill = self.billing_system.generate_bill(latest_appointment)
                    print(bill)
                else:
                    print("No appointments to generate a bill.")

            elif choice == "7":
                id_number = input("Enter staff member ID: ")
                name = input("Enter staff member name: ")
                role = input("Enter staff member role: ")
                department = input("Enter staff member department: ")

                self.staff_management.add_staff_member(id_number, name, role, department)

            elif choice == "8":
                if self.staff_management.staff_members:
                    doctor_name = input("Enter doctor name: ")
                    department = input("Enter department to assign the doctor: ")

                    for staff_member in self.staff_management.staff_members:
                        if staff_member.name == doctor_name and staff_member.role == "Doctor":
                            staff_member.department = department
                            print(f"Doctor {doctor_name} assigned to {department}.")
                            break
                    else:
                        print(f"Doctor {doctor_name} not found or is not assigned as a Doctor.")
                else:
                    print("No staff members available. Please add staff members first.")

            elif choice == "9":
                if self.staff_management.staff_members:
                    doctor_name = input("Enter doctor name: ")
                    patient_id = input("Enter patient ID: ")
                    medication = input("Enter prescribed medication: ")

                    for staff_member in self.staff_management.staff_members:
                        if staff_member.name == doctor_name and staff_member.role == "Doctor":
                            # You might want to perform additional checks here
                            patient = next((app.patient for app in self.appointments if app.patient.id_number == patient_id), None)
                            if patient:
                                self.prescription_management.manage_prescription(staff_member, patient, medication)
                                break
                            else:
                                print(f"Patient with ID {patient_id} not found.")
                        else:
                            print(f"Doctor {doctor_name} not found or is not assigned as a Doctor.")
                else:
                    print("No staff members available. Please add staff members first.")

            elif choice == "10":
                date = input("Enter the date (YYYY-MM-DD) for the report: ")
                print(self.reporting.generate_daily_appointments_report(date))

            elif choice == "11":
                month = input("Enter the month for the report: ")
                year = input("Enter the year for the report: ")
                print(self.reporting.generate_monthly_billing_summary(month, year))

            elif choice == "12":
                self.search_patient_by_id()

            elif choice == "13":
                print("Exiting Hospital Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 13.")

# Main entry point
if __name__ == "__main__":
    hms = HospitalManagementSystem()
    hms.start_system()
