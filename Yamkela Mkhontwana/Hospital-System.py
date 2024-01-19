from datetime import datetime

# Base class for Person
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# Class for Patients
class Patient(Person):
    def __init__(self, name, age, address, medical_history, file_number, id_number):
        super().__init__(name, age, address)
        self.medical_history = medical_history
        self.file_number = file_number
        self.id_number = id_number

# Class for Appointments
class Appointment:
    def __init__(self, patient, doctor, appointment_date):
        self.patient = patient
        self.doctor = doctor
        self.appointment_date = appointment_date

# Class for Staff
class Staff(Person):
    def __init__(self, name, age, address, role, department):
        super().__init__(name, age, address)
        self.role = role
        self.department = department

# Class for Medical Records
class MedicalRecord:
    def __init__(self, patient, prescriptions):
        self.patient = patient
        self.prescriptions = prescriptions

# Class for User Authentication
class Authentication:
    def __init__(self):
        self.users = {"admin": {"password": "admin_pass", "role": "admin"},
                      "doctor": {"password": "doctor_pass", "role": "doctor"},
                      "nurse": {"password": "nurse_pass", "role": "nurse"}}

    def login(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            return self.users[username]["role"]
        return None

# Class for Reporting
class Reporting:
    def generate_daily_appointment_report(self, appointments):
        for appointment in appointments:
            print(f"Date: {appointment.appointment_date}, Patient: {appointment.patient.name}, Doctor: {appointment.doctor.name}")

    def generate_monthly_billing_summary(self, billing_data):
        for item in billing_data:
            print(f"Month: {item['month']}, Total Revenue: R{item['total']}")

    def generate_medical_records_report(self, medical_records):
        for record in medical_records:
            print(f"Patient: {record.patient.name}, Medical History: {record.patient.medical_history}")
            print("Prescriptions:")
            for prescription in record.prescriptions:
                print(f"  - {prescription}")

# Class for HMS (Main Class to Integrate Modules)
class HospitalManagementSystem:
    def __init__(self):
        self.patients = []
        self.appointments = []
        self.staff_members = []
        self.medical_records = []
        self.authenticator = Authentication()
        self.reporter = Reporting()

        # Add sample data
        self.add_sample_data()

    def add_sample_data(self):
        # Sample Doctors
        self.add_staff_member("Dr. Mkhontwana", 40, "456 Oak St", "Doctor", "Cardiology")
        self.add_staff_member("Dr. Johnson", 35, "789 Maple St", "Doctor", "Pediatrics")
        self.add_staff_member("Dr. Mokoena", 45, "123 Pine St", "Doctor", "Orthopedics")
        self.add_staff_member("Dr. Williams", 50, "987 Cedar St", "Doctor", "Oncology")

        # Sample Patients
        self.register_patient("Siyanda Xulu", 35, "123 Main St", "None", "FN001", "8704068766554")
        self.register_patient("Mandisa Bolofo", 28, "456 Elm St", "Allergies", "FN002", "9604087665083")
        self.register_patient("Bob Smith", 50, "789 Birch St", "Hypertension", "FN003", "ID003")
        self.register_patient("Alice Johnson", 42, "987 Spruce St", "Diabetes", "FN004", "ID004")

    def register_patient(self, name, age, address, medical_history, file_number=None, id_number=None):
        if file_number is None:
            file_number = self.generate_file_number()

        if id_number is None:
            id_number = self.generate_id_number()

        patient = Patient(name, age, address, medical_history, file_number, id_number)
        self.patients.append(patient)

    def add_staff_member(self, name, age, address, role, department):
        staff_member = Staff(name, age, address, role, department)
        self.staff_members.append(staff_member)

    def search_patient(self, patient_id):
        for patient in self.patients:
            if patient_id.lower() in [patient.name.lower(), patient.file_number.lower(), patient.id_number.lower()]:
                return patient
        return None

    def generate_file_number(self):
        return "FN" + str(len(self.patients) + 1).zfill(3)

    def generate_id_number(self):
        return "ID" + str(len(self.patients) + 1).zfill(3)

    def update_patient_information(self, patient_id, new_info):
        patient = self.search_patient(patient_id)
        if patient:
            patient.name = new_info.get("name", patient.name)
            patient.age = new_info.get("age", patient.age)
            patient.address = new_info.get("address", patient.address)
            patient.medical_history = new_info.get("medical_history", patient.medical_history)

    def schedule_appointment(self, patient, doctor, appointment_date):
        appointment = Appointment(patient, doctor, appointment_date)
        self.appointments.append(appointment)
        print(f"\nAppointment scheduled successfully with {doctor.name} on {appointment_date}.")

    def cancel_or_reschedule_appointment(self, patient):
        print("\nYour Upcoming Appointments:")
        upcoming_appointments = [appointment for appointment in self.appointments if appointment.patient == patient]

        if not upcoming_appointments:
            print("No upcoming appointments found.")
            return

        for i, appointment in enumerate(upcoming_appointments, start=1):
            print(f"{i}. Doctor: {appointment.doctor.name}, Date: {appointment.appointment_date}")

        choice = input("\nEnter the number of the appointment you want to cancel or reschedule (0 to go back): ")
        if choice == "0":
            return

        try:
            selected_appointment = upcoming_appointments[int(choice) - 1]
            new_date = input("Enter the new date for the appointment (e.g., YYYY-MM-DD): ")
            if not self.is_valid_date(new_date):
                print("Invalid date. Enter a valid date (YYYY-MM-DD) with month between 1 and 12, day between 1 and 31, and year 2024.")
                return

            selected_appointment.appointment_date = new_date
            print("Appointment rescheduled successfully.")

        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid appointment number.")

    def view_upcoming_appointments(self, patient):
        print("\nYour Upcoming Appointments:")
        upcoming_appointments = [appointment for appointment in self.appointments if appointment.patient == patient]

        if not upcoming_appointments:
            print("No upcoming appointments found.")
        else:
            for i, appointment in enumerate(upcoming_appointments, start=1):
                print(f"{i}. Doctor: {appointment.doctor.name}, Date: {appointment.appointment_date}")

    def is_valid_date(self, date_str):
        try:
            appointment_date = datetime.strptime(date_str, "%Y-%m-%d")
            # Validate month, day, and year as per your requirements
            if not 1 <= appointment_date.month <= 12 or not 1 <= appointment_date.day <= 31 or appointment_date.year != 2024:
                return False
            return True
        except ValueError:
            return False


class Reception:
    def __init__(self, hospital_system):
        self.hospital_system = hospital_system
        self.current_user_role = None

    def start_reception(self):
        print("Welcome to the Hospital Management System")

        # Secure login for hospital staff
        while not self.current_user_role:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            self.current_user_role = self.hospital_system.authenticator.login(username, password)

            if not self.current_user_role:
                print("Invalid login credentials. Please try again.")

        print(f"Login successful. Role: {self.current_user_role}")

        while True:
            print("\nOptions:")
            print("1. Search Patient")
            print("2. Register New Patient")
            print("3. Generate Medical Records Report")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.search_patient()

            elif choice == "2":
                self.register_patient()

            elif choice == "3":
                self.generate_medical_records_report()

            elif choice == "4":
                print("Exiting Reception. Have a great day!")
                break

            else:
                print("Invalid choice. Please try again.")

    def search_patient(self):
        patient_id = input("Enter patient ID or file number: ")
        patient = self.hospital_system.search_patient(patient_id)

        if patient:
            print("Patient found!")
            self.display_patient_information(patient)
            self.patient_menu(patient)
        else:
            print("Patient not found. Please register.")

    def display_patient_information(self, patient):
        print(f"Patient Information:\nName: {patient.name}\nAge: {patient.age}\nAddress: {patient.address}")
        print(f"File Number: {patient.file_number}\nID Number: {patient.id_number}")

    def register_patient(self):
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        address = input("Enter patient address: ")
        medical_history = input("Enter patient medical history: ")
        ID = int(input("Enter ID number: "))
        file_number = int(input("Enter file number: "))

        self.hospital_system.register_patient(name, age, address, medical_history, file_number, ID)
        print("Patient registered successfully!")

    def patient_menu(self, patient):
        while True:
            print("\nPatient Menu:")
            print("1. Schedule Appointment")
            print("2. View Upcoming Appointments")
            print("3. Cancel or Reschedule Appointment")
            print("4. View Medical Records")
            print("5. Update Information")
            print("6. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.schedule_appointment(patient)

            elif choice == "2":
                self.view_upcoming_appointments(patient)

            elif choice == "3":
                self.cancel_or_reschedule_appointment(patient)

            elif choice == "4":
                self.view_medical_records(patient)

            elif choice == "5":
                self.update_patient_information(patient)

            elif choice == "6":
                print("Returning to Main Menu.")
                break

            else:
                print("Invalid choice. Please try again.")

    def schedule_appointment(self, patient):
        print("\nAvailable Doctors:")
        for i, doctor in enumerate(self.hospital_system.staff_members):
            print(f"{i + 1}. {doctor.name}, {doctor.department}")

        doctor_choice = int(input("\nEnter the number of the doctor you want to schedule with: ")) - 1
        selected_doctor = self.hospital_system.staff_members[doctor_choice]

        print(f"\nAvailable Appointment Times for {selected_doctor.name}:")
        # We can add logic here to display available appointment times

        # For now, let's assume some sample times
        available_times = ["10:00 AM", "02:30 PM", "04:15 PM"]
        for i, time in enumerate(available_times):
            print(f"{i + 1}. {time}")

        # Validate the appointment date
        appointment_date = input("\nEnter the date for the appointment (e.g., YYYY-MM-DD): ")
        if not self.hospital_system.is_valid_date(appointment_date):
            print("Invalid date. Enter a valid date (YYYY-MM-DD) with month between 1 and 12, day between 1 and 31, and year 2024.")
            return

        time_choice = int(input("\nEnter the number of the preferred appointment time: ")) - 1
        selected_time = available_times[time_choice]

        self.hospital_system.schedule_appointment(patient, selected_doctor, f"{appointment_date} {selected_time}")

    def cancel_or_reschedule_appointment(self, patient):
        self.hospital_system.cancel_or_reschedule_appointment(patient)

    def view_upcoming_appointments(self, patient):
        self.hospital_system.view_upcoming_appointments(patient)

    def view_medical_records(self, patient):
        print(f"\nMedical Records for {patient.name}:")
        # Assume some sample medical records for demonstration
        for record in self.hospital_system.medical_records:
            if record.patient == patient:
                print(f"Prescriptions: {record.prescriptions}")

    def update_patient_information(self, patient):
        print("\nUpdate Patient Information:")
        new_name = input("Enter new name (leave blank to keep current): ")
        new_age = input("Enter new age (leave blank to keep current): ")
        new_address = input("Enter new address (leave blank to keep current): ")
        new_medical_history = input("Enter new medical history (leave blank to keep current): ")

        new_info = {"name": new_name, "age": new_age, "address": new_address, "medical_history": new_medical_history}
        self.hospital_system.update_patient_information(patient.id_number, new_info)
        print("Patient information updated successfully!")


if __name__ == "__main__":
    hms = HospitalManagementSystem()
    reception = Reception(hms)
    reception.start_reception()

