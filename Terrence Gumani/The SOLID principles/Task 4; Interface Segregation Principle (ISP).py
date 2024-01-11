# Define separate interfaces for each functionality

class Print:
    def print_document(self):
        pass

class Scan:
    def scan_document(self):
        pass

class Fax:
    def send_fax(self):
        pass

class Photocopy:
    def photocopy_document(self):
        pass

# Create a multifunction printer class that implements all the interfaces

class MultifunctionPrinter(Print, Scan, Fax, Photocopy):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

    def send_fax(self):
        print("Sending fax")

    def photocopy_document(self):
        print("Photocopying document")

# Clients can now depend only on the interfaces they need

class ComputerClient:
    def __init__(self, printer: Print):
        self.printer = printer

    def perform_print_job(self):
        self.printer.print_document()

class UserClient:
    def __init__(self, printer: Scan):
        self.printer = printer

    def perform_scan_job(self):
        self.printer.scan_document()

# Example usage

printer = MultifunctionPrinter()

computer_client = ComputerClient(printer)
computer_client.perform_print_job()

user_client = UserClient(printer)
user_client.perform_scan_job()
