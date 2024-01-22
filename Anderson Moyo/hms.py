from reportlab.pdfgen import canvas
class Patient:
    def __init__(self, name, age, address, medical_history, patient_id):
        self.name = name
        self.age = age
        self.address = address
        self.medical_history = medical_history
        self.patient_id = patient_id

    def register_patient(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.address = input("Enter address: ")
        self.patient_id = int(input("Enter your ID number: "))
        self.medical_history = input("Enter your medical history: ")

    def search_patient(self, patient_list):
        tpatient_id = int(input("Enter your ID number: "))
        for patient in patient_list:
            if tpatient_id == patient.patient_id:
                return f"{patient.name} {patient.age} {patient.address} {patient.medical_history}"
        return "Patient not found"
    def generate_patient_report(self, filename):
        patient_info = f"Name: {self.name}\nAge: {self.age}\nAddress: {self.address}\nMedical History: {self.medical_history}"

        pdf_filename = f"{filename}.pdf"
        c = canvas.Canvas(pdf_filename)
        c.drawString(100, 750, "Patient Information:")
        c.drawString(100, 730, patient_info)
        c.save()

        print(f"Patient report generated successfully: {pdf_filename}")

    def update_patient(self):
        self.name = input("Enter new name: ")
        self.age = int(input("Enter new age: "))
        self.address = input("Enter new address: ")
        self.medical_history = input("Enter new medical history: ")
        print("Patient information updated successfully.")

class Appointment:
    def __init__(self, patient, doctor, date_time):
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

    @staticmethod
    def schedule_appointment(patient, doctor, date_time):
        return Appointment(patient, doctor, date_time)

    @staticmethod
    def cancel_appointment(appointment_list, target_date_time, patient):
        for appointment in appointment_list:
            if target_date_time == appointment.date_time and patient == appointment.patient:
                appointment_list.remove(appointment)
                print("Appointment canceled successfully.")
                return
        print("Appointment not found.")

    # @staticmethod
    # def view_upcoming_appointments(appointment_list, patient):
    #     upcoming_appointments = [appointment for appointment in appointment_list if appointment.patient == patient]
    #     if upcoming_appointments:
    #         return [(appointment.doctor, appointment.date_time) for appointment in upcoming_appointments]
    #     else:
    #         return "No upcoming appointments."
        
    def view_upcoming_appointments(appointment_list, patient):
        upcoming_appointments = [(appointment.doctor, appointment.date_time) for appointment in appointment_list if appointment.patient == patient]
        if upcoming_appointments:
            return upcoming_appointments
        else:
            return []

class StaffManagement:
    def __init__(self):
        self.staff_list = []
        self.departments = {}

    def add_staff_member(self, name, role, department):
        staff_member = {'name': name, 'role': role, 'department': department}
        self.staff_list.append(staff_member)
        print(f"Staff member {name} added successfully.")

    def assign_doctor_to_department(self, doctor_name, department):
        if department not in self.departments:
            self.departments[department] = []
        self.departments[department].append(doctor_name)
        print(f"Doctor {doctor_name} assigned to {department} department.")

class MedicalRecordsManagement:
    def __init__(self):
        self.medical_records = {}

    def record_medical_history(self, patient, medical_history):
        self.medical_records[patient.patient_id] = medical_history
        print("Medical history recorded successfully.")

    def retrieve_medical_history(self, patient):
        patient_id = patient.patient_id
        if patient_id in self.medical_records:
            return self.medical_records[patient_id]
        else:
            return "Medical history not found."

    def manage_prescription(self, patient, prescription):
        patient_id = patient.patient_id
        if patient_id not in self.medical_records:
            self.medical_records[patient_id] = {'prescriptions': []}
        self.medical_records[patient_id]['prescriptions'].append(prescription)
        print("Prescription added successfully.")

class UserAuthentication:
    def __init__(self):
        self.credentials = {'admin': 'adminpass', 'Dr Nkosi': 'Khumalo98', 'nurse1': 'nursepass'}

    def authenticate_user(self, username, password):
        if username in self.credentials and self.credentials[username] == password:
            return True
        else:
            return False

    def get_user_role(self, username):
        if username.startswith('admin'):
            return 'admin'
        elif username.startswith('doctor'):
            return 'doctor'
        elif username.startswith('Dr'):
            return 'doctor'
        elif username.startswith('nurse'):
            return 'nurse'
        else:
            return 'unknown'


patient_list = []
appointment_list = []
staff_management = StaffManagement()
medical_records_management = MedicalRecordsManagement()
user_authentication = UserAuthentication()
current_user = None

while True:
    print("Select an action")
    if current_user:
        print(f"Logged in as {current_user}, Role: {user_authentication.get_user_role(current_user)}")

    print("1. Login")
    print("2. Logout/Exit")
    print("3. Register a patient")
    print("4. Search for a patient")
    print("5. Update patient information")
    print("6. Schedule a new appointment")
    print("7. Cancel an appointment")
    print("8. View upcoming appointments")
    print("9. Add new staff member (Admin only)")
    print("10. Assign doctor to department (Admin only)")
    print("11. Record medical history (Doctor only)")
    print("12. Retrieve medical history (Doctor only)")
    print("13. Manage prescription information (Doctor only)")

    action = input("Enter your choice: ")

    if action == "2":
        if current_user:
            current_user = None
            print("Logged out successfully.")
        else:
            break

    elif action == "1":
        if current_user:
            print("Already logged in.")
        else:
            username = input("Enter username: ")
            password = input("Enter password: ")
            if user_authentication.authenticate_user(username, password):
                current_user = username
                print("Login successful.")
            else:
                print("Invalid credentials. Please try again.")

    elif current_user:
        user_role = user_authentication.get_user_role(current_user)

        if action == "3":
            print("Welcome to our hospital, enter patient details!!")
            patient_object = Patient("", "", "", "", 0)
            patient_object.register_patient()
            patient_list.append(patient_object)

        elif action == "4":
            target_patient_id = int(input("Enter the ID of the patient you wish to search: "))
            result = Patient("", "", "", "", 0).search_patient(patient_list)
            print(result)

            if result != "Patient not found":
                generate_report = input("Do you want to generate a PDF report? (yes/no): ").lower()
                if generate_report == "yes":
                    patient_object.generate_patient_report(f"Patient_Report_{target_patient_id}")

        elif action == "5":
            target_patient_id = int(input("Enter the ID of the patient you wish to update: "))
            Patient("", "", "", "", 0).update_patient(patient_list, target_patient_id)

        elif action == "6":
            doctor = input("Enter the doctor's name: ")
            date_time = input("Enter the appointment date and time: ")
            new_appointment = Appointment(patient_list[0], doctor, date_time)
            appointment_list.append(new_appointment)
            f"Appointment for {patient_object} scheduled successfully with {doctor} at {date_time}"

        elif action == "7":
            target_date_time = input("Enter the date and time of the appointment you wish to cancel: ")
            Appointment(patient_object, "", "").cancel_appointment(appointment_list, target_date_time)

        elif action == "8":
            if not patient_list:
                print("Please register a patient first.")
            else:
                upcoming_appointments = Appointment.view_upcoming_appointments(appointment_list, patient_list[0])
                print("Upcoming Appointments:")
                for appointment in upcoming_appointments:
                    doctor, date_time = appointment  # Unpack the tuple
                    print(f"Doctor: {doctor}, Date and Time: {date_time}")

        elif user_role == 'admin':
            if action == "9":
                name = input("Enter staff member's name: ")
                role = input("Enter staff member's role: ")
                department = input("Enter staff member's department: ")
                staff_management.add_staff_member(name, role, department)

            elif action == "10":
                doctor_name = input("Enter doctor's name: ")
                department = input("Enter the department to assign the doctor: ")
                staff_management.assign_doctor_to_department(doctor_name, department)

        elif user_role == 'doctor':
            if action == "11":
                medical_history = input("Enter the medical history: ")
                medical_records_management.record_medical_history(patient_object, medical_history)

            elif action == "12":
                retrieved_history = medical_records_management.retrieve_medical_history(patient_object)
                print("Medical History:")
                print(retrieved_history)

            elif action == "13":
                prescription = input("Enter the prescription information: ")
                medical_records_management.manage_prescription(patient_object, prescription)

    else:
        print("Invalid choice. Please try again.")
