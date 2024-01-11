# Exercise 4: Interface Segregation Principle (ISP)
# Scenario: You are tasked with developing software for a multifunction printer. This printer can print, scan, fax, and photocopy.
# Task: Design the software components ensuring that clients (like a computer or a user) that use this software will not be forced to depend on interfaces they do not use.

class Printer:
    def print_document(self, document):
        pass

class Scanner:
    def scan_document(self):
        pass

class FaxMachine:
    def send_fax(self, document):
        pass

class Photocopier:
    def photocopy_document(self, document):
        pass

class MultifunctionPrinter(Printer, Scanner, FaxMachine, Photocopier):
    def print_document(self, document):
        # Implementation for printing

     def scan_document(self):
        # Implementation for scanning

      def send_fax(self, document):
        # Implementation for sending fax

       def photocopy_document(self, document):
             