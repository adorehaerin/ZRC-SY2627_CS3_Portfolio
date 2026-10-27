
class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount


    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_bill_amount(self, bill_amount):
        self.__bill_amount = bill_amount

    def calculate_bill(self):
        return self.__bill_amount


# Child class for senior citizens
class SeniorPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return super().calculate_bill() * 0.80


class PhilHealthPatient(Patient):
    def __init__(self, name, bill_amount):
        super().__init__(name, bill_amount)

    def calculate_bill(self):
        return super().calculate_bill() * 0.85


regular_patient = Patient("Juan Dela Cruz", 15000)
senior_patient = SeniorPatient("Maria Santos", 15000)
philhealth_patient = PhilHealthPatient("Pedro Reyes", 15000)

print("\n----Hospital Billing System----\n")

patients = [
    regular_patient,
    senior_patient,
    philhealth_patient
]

for patient in patients:
    print("Patient Name:", patient.get_name())
    print("Original Bill: ₱", f"{patient.get_bill_amount():.2f}")
    print("Final Bill: ₱", f"{patient.calculate_bill():.2f}")
    print("-" * 35)