from abc import ABC, abstractmethod

# Part 1: Define specific interfaces for each functionality

class PrintCapability(ABC):
    @abstractmethod
    def print_document(self, document):
        pass

class ScanCapability(ABC):
    @abstractmethod
    def scan_document(self):
        pass

class FaxCapability(ABC):
    @abstractmethod
    def send_fax(self, document):
        pass

class CopyCapability(ABC):
    @abstractmethod
    def photocopy_document(self, document):
        pass

# Part 2: Implement classes with specific capabilities

class SimplePrinter(PrintCapability):
    def print_document(self, document):
        print(f"Printing: {document}")

class SimpleScanner(ScanCapability):
    def scan_document(self):
        print("Scanning document")

class SimpleFax(FaxCapability):
    def send_fax(self, document):
        print(f"Sending fax: {document}")

class SimpleCopier(CopyCapability):
    def photocopy_document(self, document):
        print(f"Photocopying: {document}")

# Part 3: Usage example

class Computer:
    def __init__(self, printer, scanner):
        self.printer = printer
        self.scanner = scanner

    def user_print(self, document):
        self.printer.print_document(document)

    def user_scan(self):
        self.scanner.scan_document()

# Example Usage:

simple_printer = SimplePrinter()
simple_scanner = SimpleScanner()

computer = Computer(simple_printer, simple_scanner)
computer.user_print("Important Report")
computer.user_scan()
