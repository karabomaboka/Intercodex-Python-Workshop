from datetime import datetime, timedelta
import pprint
import pwinput
import random
      
#====================================================================================================================================================          
class StaffManagement:
    def __init__(self):
        self.staff_database = {}

    def register_user(self):
        print(f"{self.staff_database}")
        # self.id_number = id_number
        # self.name = name
        # self.role = role
        # self.department = department 
        # self.password = password
        # self.database = database
        
        id_number = int(input("Please enter your ID number: "))
        name = input("Please enter your name: ")
        role = input("Please enter your role: ")
        department = input("Please enter your department: ")
        password = input("Create a new password: ")

        #self.staff_database[id_number] = {"Name":name,"Role":role,"Department":department,"Password":password}
        
        self.staff_database.update({id_number:{"Name":self.name,"Role":self.role,"Department":self.department,"Password":self.password}})
        #print(f"{self.staff_database}")
        
    
    def assign_doctor_to_department(self):
        dr = input("Select doctor to re-assign: ")
        for k, v in self.staff_database.items():
            if k == dr:
                dept = input("Select department to assign doctor to: ")
                self.staff_database["Department"] = dept

#======================================================================================
class UserAuthentication(StaffManagement):
    
    def __init__(self):
        super().__init__()

    def login(self):
        username = int(input("Enter your username: "))
        password = pwinput.pwinput(prompt="Enter your password",mask="*")
        attempts = 0
        
        while (password != StaffManagement().staff_database[username]["Password"]):
            if attempts < 3:
                attempts += 1
                print(f"Incorrect password. You have {3 - attempts} attempt(s) left")
                password = pwinput.pwinput(prompt="Re-enter your password",mask="*")
                break
                return True
                    
            else: 
                print("Your account is locked. Contact IT admin")
                StaffManagement().staff_database[username]["Password"] = random.randint(1000000,9999999)
                break
                return False
                
#=======================================================================================================
class Appointments:
   
    def __init__(self):
        self.appointment_count = 1
        self.appointment_list = {self.appointment_count:{"Date time":None,"Duration": None,"Patient ID":None,"Assigned doctor":None}}
    
    def schedule_appointment(self):
        year = int(input("Please enter the year: "))
        month = int(input("Please enter the month: "))
        day = int(input("Please enter the day: "))
        hour = int(input("Please enter the hour: "))
        minutes = int(input("Please enter the minutes: "))
        seconds = 0
        duration = int(input("Please enter the duration: "))

        check_date_time = datetime(year,month,day,hour,minutes,seconds)

        for i in self.appointment_list[self.appointment_count]:
            if self.appointment_count > 1:
                if (self.appointment_list[self.appointment_count]["Date time"]<=check_date_time<=self.appointment_list[self.appointment_count]["Date time"]+timedelta(self.appointment_list[self.appointment_count]["Duration"])) and (self.appointment_list[self.appointment_count]["Date time"]<=check_date_time + timedelta(minutes=duration)<=self.appointment_list[self.appointment_count]["Date time"]+timedelta(self.appointment_list[self.appointment_count]["Duration"])):
                    print("This slot is unavailable")
                
                else:
                    self.appointment_count += 1
                    patient_id = int(input("Please enter the patient ID: "))
                    assigned_dr = int(input("Please select the doctor: "))
                    self.appointment_list[self.appointment_count]={"Date time":check_date_time,"Duration":duration ,"Patient ID":patient_id, "Assigned doctor":assigned_dr}
                    break
            else:
                self.appointment_count += 1
                patient_id = int(input("Please enter the patient ID: "))
                assigned_dr = int(input("Please select the doctor: "))
                self.appointment_list[self.appointment_count]={"Date time":check_date_time,"Duration":duration ,"Patient ID":patient_id, "Assigned doctor":assigned_dr}
                break

        return print(self.appointment_list)
    
    def cancel_reschedule_appointments(self):
        patient_id = int(input("Type the id number of the patient you would like to reschedule: "))
        for i in self.appointment_list:
                if self.appointment_list[i]["Patient ID"]==patient_id:
                    print(f"{self.appointment_list}")
        appointment_no = int(input("Type the appointment number you would like to change: "))
        option = int(input("Would you like to change an appointment or remove it?\n1.Change it \n2.Remove it:\n "))

        if option == 1:
            self.schedule_appointment()
            del self.appointment_list[appointment_no] 
            print(f"Appointment has been succesfully reschuled")

        elif option == 2:
            
            del self.appointment_list[appointment_no] 
            print(f"Appointment {appointment_no} for patient {patient_id} has been succesfully cancelled")

        else:
            print(f"Invalid entry")

    def view_upcoming_appointments(self):
        # Prints the nicely formatted dictionary
        pprint.pprint(self.appointment_list)

#=====================================================================================================================
class MedicalRecords(PatientManagement):

    def __init__(self):
        pass
        
    def return_record(self):
        pprint.pprint(PatientManagement().patient_database)
    
    def add_prescription(self):
        patient_for_prescription = PatientManagement().search_for_patient()
        prescription = input("Enter details of the prescription: ")

        for k, v in PatientManagement().patient_database.items():
            if k == patient_for_prescription:
                PatientManagement().patient_database["Prescription"] = prescription

#==========================================================================================================================
class HMS:
    def __init__(self):
        pass

    def run_hms(self):
        print("Welcome to the InterCodex Health Management System 👨🏾‍⚕️ 👩🏾‍⚕️ 💜 🖤")
        while True:
            staff_access = int(input("Would you like to register or login?\n1.Login\n2.Register: \n"))

            if staff_access == 1:
                UserAuthentication().login()
                if UserAuthentication().login() == True:
                    print("What would you like to do?")
                    optionz = int(input("\n1.Appointments\n2.Retrive medical records\n3.Patient portal\n4.Exit"))
                
                    if optionz == 1:
                        optionx = int(input("\n1.Schedule an appointment\n2.Reschedule/Cancel an appointment\n3.View upcoming appointments\n4.Exit"))
                        if optionx == 1:
                            Appointments().schedule_appointment()
                        elif optionx == 2:
                            Appointments().cancel_reschedule_appointments()
                        elif  optionx == 3:
                            Appointments().view_upcoming_appointments()
                        elif optionx == 4:
                            break
                    
                    elif optionz == 2:
                        optionc = int(input("\n1.Return medical records\n2.Add prescription\n3.Exit"))
                        if optionc == 1:
                            MedicalRecords().return_record()
                        elif optionc == 2:
                            MedicalRecords().add_prescription()
                        elif optionc == 3:
                            break

                    elif optionz == 3:
                        optionv = int(input("\n1.Register a patient\n2.Search for patient\n3.Update patient\n4.Exit"))
                        if optionv == 1:
                            PatientManagement().register_user()
                        elif optionv == 2:
                            PatientManagement().search_for_patient()
                        elif optionv == 3:
                            PatientManagement().update_patient()
                        elif optionv == 4:
                            break
                else:
                    break

            elif staff_access == 2:
                # id_number = int(input("Please enter your ID number: "))
                # name = input("Please enter your name: ")
                # role = input("Please enter your role: ")
                # department = input("Please enter your department: ")
                # password = input("Create a new password: ")

                StaffManagement().register_user()
            else: 
                print("Invalid entry")

       

#=========================================================================================================================
if __name__ == "__main__":
    hms = HMS()

    hms.run_hms()
    
