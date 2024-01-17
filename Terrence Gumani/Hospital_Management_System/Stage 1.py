# Base class for Person [Receptionist]
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# Class for Patient, inheriting from Person
class Patient(Person):
    def __init__(self, name, age, address, medical_history):
        super().__init__(name, age, address)
        self.medical_history = medical_history

# Class for Doctor, inheriting from Person
class Doctor(Person):
    def __init__(self, name, age, address, role, department):
        super().__init__(name, age, address)
        self.role = role
        self.department = department

# Class for Appointment
class Appointment:
    def __init__(self, patient, doctor, date_time):
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time

# Interface for Medical Records
class MedicalRecords:
    def record_medical_history(self, patient, history):
        pass

    def retrieve_medical_history(self, patient):
        pass

# Class for Authentication
class Authentication:
    def login(self, username, password):
        pass

# Class for Reporting
class Reporting:
    def generate_daily_appointments_report(self, date):
        pass

    def generate_monthly_billing_summary(self, month, year):
        pass
