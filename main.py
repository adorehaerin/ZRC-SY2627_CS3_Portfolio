

class AssignmentSubmission:
    def __init__(self, student_name: str, student_id: str, assignment_title: str, due_date: str):
        self._assignment_title = assignment_title
        self._student_name = student_name
        self.student_id = student_id
        self._due_date = due_date
        self.__grade = None
        self.__is_submitted = False
        self.__submitted_files: list[str] = []

    def __validate_grade(self, score: float) -> bool:
        return 0 <= score <= 100

    def assign_grade(self, grade: float) -> None:
        self.__grade = grade
        print(f"[Success] Grade of {grade} assigned to {self._student_name}")

    def __check_submission_status(self) -> bool:
        return self.__is_submitted

    def __is_duplicate(self, filename: str) -> bool:
        return filename in self.__submitted_files


    def add_file(self, filename: str):
    
        if self.__is_duplicate(filename):
            print(f"[warning] '{filename}' is already attached!")
        self.__submitted_files.append(filename)
        self.__is_submitted = True
        len(self.__submitted_files)
        print(f"[Success] {self._student_name} has attached the file '{filename}' for the assignment '{self._assignment_title}'. Total files: {len(self.__submitted_files)}.")

    def remove_file(self, filename: str):
        if filename not in self.__submitted_files:
            print(f"[Error] File '{filename}' is not found in the submission.")
            return
        self.__submitted_files.remove(filename)
        print(f"[Success] {self._student_name} has removed the file '{filename}'.")

    def get_grade(self):
        return self.__grade

    def view_files(self) -> list[str]:
        return list(self.__submitted_files)

    def get_status_report(self) -> str:
        status = "Submitted" if self.__is_submitted else "Not Submitted"
        if self.__grade is None:
            status = "Not graded"
        print("FINAL SYSTEM REPORT:")
        return f"ID: {self.student_id} | Name: {self._student_name} | Assignment Title: {self._assignment_title} |Due Date: {self._due_date} | Status: {status} | Grade: {self.__grade} | Submitted Files: {len(self.__submitted_files)}"


student1 = AssignmentSubmission(student_name="Alex Gonzaga", student_id="pshs-1090-x", assignment_title="CS-101", due_date="2026-10-01")

student1.add_file("main.py")
student1.remove_file("main.py")

print(student1.get_status_report())
