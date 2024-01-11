# Exercise 4: Interface Segregation Principle (ISP)
# Scenario: You are tasked with developing software for a multifunction printer. This printer can print, scan, fax, and photocopy.
# Task: Design the software components ensuring that clients (like a computer or a user) that use this software will not be forced to depend on interfaces they do not use.

# Your implementation here
# Interface for printing
class PrintFunctionality:
    def print_document(self):
        pass

# Interface for scanning
class ScanFunctionality:
    def scan_document(self):
        pass

# Interface for faxing
class FaxFunctionality:
    def send_fax(self):
        pass

# Interface for photocopying
class PhotocopyFunctionality:
    def photocopy_document(self):
        pass

# MultifunctionPrinter class implementing all interfaces
class MultifunctionPrinter(PrintFunctionality, ScanFunctionality, FaxFunctionality, PhotocopyFunctionality):
    def print_document(self):
        print("Printing document")

    def scan_document(self):
        print("Scanning document")

    def send_fax(self):
        print("Sending fax")

    def photocopy_document(self):
        print("Photocopying document")

# Example usage
printer = MultifunctionPrinter()
printer.print_document()
printer.scan_document()
printer.send_fax()
printer.photocopy_document()