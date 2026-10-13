class CampusDirector:
    def __init__(self, orders):
        self.orders = orders

    def announce_orders(self):
        print("Campus Director: Announcing the following orders:")
        for order in self.orders:
            print(f"- {order}")

class CurriculumInstructionsDivision(CampusDirector):
    def __init__(self, orders, curriculum, signature, schedule):
        super().__init__(orders)
        self.curriculum = curriculum
        self.signature = "Signature sa CID"
        self.schedule = schedule

    def review_curriculum(self):
        print("Curriculum Instructions Division: Reviewing the curriculum:")
        for subject, details in self.curriculum.items():
            print(f"- {subject}: {details}")
    def sign_curriculum(self):
        print(f"Curriculum Instructions Division: Curriculum signed by {self.signature}.")

class StudentServicesDivision(CampusDirector):
    def __init__(self, orders, services, student_files):
        super().__init__(orders)
        self.services = services
        self.student_files = student_files

    def provide_services(self):
        print("Student Services Division: Providing the following services:")
        for service in self.services:
            print(f"- {service}")
    def manage_student_files(self):
        print("Student Services Division: Managing student files:")
        for file in self.student_files:
            print(f"- {file}")

class Gwynne(CurriculumInstructionsDivision):
    def __init__(self, orders, curriculum, signature, schedule):
        super().__init__(orders, curriculum, signature, schedule)
        self.teach = "Teaching the curriculum to students."
    def teach_students(self):
        print(f"Gwynne: {self.teach}")
#lovenalovenakosimaamgwynne

class Gie(CurriculumInstructionsDivision):
    def __init__(self, orders, curriculum, signature, schedule):
        super().__init__(orders, curriculum, signature, schedule)
        self.adviser = "Advising students on curriculum matters."
    def advise_students(self):
        print(f"Gie: {self.adviser}")

class JJAli(CurriculumInstructionsDivision):
    def __init__(self, orders, curriculum, signature, schedule):
        super().__init__(orders, curriculum, signature, schedule)
        self.assess = "Assessing student performance based on the curriculum."
    def assess_students(self):
        print(f"JJAli: {self.assess}")

class Kaiza(Gie):
    def __init__(self, orders, curriculum, signature, schedule):
        super().__init__(orders, curriculum, signature, schedule)
        self.student = "Kaiza is a student who follows the curriculum and receives guidance from Gie."
    def follow_curriculum(self):
        print(f"Kaiza: {self.student}")
class MADETH(StudentServicesDivision):
    def __init__(self, orders, services, student_files):
        super().__init__(orders, services, student_files)
        self.support = "Providing support to students in various aspects."
    def support_students(self):
        print(f"MADETH: {self.support}")

class Flor (MADETH):
    def __init__(self, orders, services, student_files):
        super().__init__(orders, services, student_files)
        self.assist = "Assisting students with their needs and concerns."
    def assist_students(self):
        print(f"Flor: {self.assist}")