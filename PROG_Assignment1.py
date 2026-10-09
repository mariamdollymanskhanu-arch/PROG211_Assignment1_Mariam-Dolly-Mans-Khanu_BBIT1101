"""
Student Learning Portal
Object-Oriented Programming 1 - Individual Assignment
Domain: Education
Aligned with Digital Public Goods (DPG) principles
"""

from datetime import datetime

# ============================================================
# CLASS 1: Student
# ============================================================
class Student:
    """Represents a student in the learning portal."""

    total_students = 0

    def __init__(self, student_id, level, programme, enrollment_date, status="Active"):
        """
        Privacy note: Only anonymized data is stored.
        No real names or personal details.
        """
        self.student_id = student_id          # e.g. "STU-2026-001"
        self.level = level                    # e.g. "Year 1", "Year 2"
        self.programme = programme            # e.g. "Computer Science"
        self.enrollment_date = enrollment_date
        self.status = status
        self.courses = []                     # list of course codes the student is taking

        Student.total_students += 1

    # ---------- Instance Methods ----------
    def display_info(self):
        """Display student information."""
        print(f"\n--- Student Details ---")
        print(f"ID              : {self.student_id}")
        print(f"Level           : {self.level}")
        print(f"Programme       : {self.programme}")
        print(f"Enrollment Date : {self.enrollment_date}")
        print(f"Status          : {self.status}")
        print(f"Courses         : {', '.join(self.courses) if self.courses else 'None'}")

    def enroll_course(self, course_code):
        """Enroll the student in a course (instance method)."""
        if course_code not in self.courses:
            self.courses.append(course_code)
            print(f"{self.student_id} successfully enrolled in {course_code}.")
        else:
            print(f"{self.student_id} is already enrolled in {course_code}.")

    def update_status(self, new_status):
        """Update student status."""
        valid = ["Active", "Inactive", "Graduated", "Suspended"]
        if new_status in valid:
            old = self.status
            self.status = new_status
            print(f"Status of {self.student_id} changed from '{old}' to '{new_status}'.")
        else:
            print(f"Invalid status. Allowed: {valid}")

    # ---------- Class Method ----------
    @classmethod
    def create_standard(cls, level, programme):
        """Class method: Create a new student with auto-generated ID."""
        Student.total_students += 1
        new_id = f"STU-{datetime.now().year}-{Student.total_students:03d}"
        today = str(datetime.now().date())

        return cls(
            student_id=new_id,
            level=level,
            programme=programme,
            enrollment_date=today,
            status="Active"
        )

    # ---------- Static Method ----------
    @staticmethod
    def validate_id_format(student_id):
        """Static method: Check if student ID format is correct."""
        return student_id.startswith("STU-") and len(student_id) >= 12


# ============================================================
# CLASS 2: Course
# ============================================================
class Course:
    """Represents a course in the learning portal."""

    total_courses = 0

    def __init__(self, course_code, title, credit_hours, department, status="Open"):
        self.course_code = course_code        # e.g. "CS101"
        self.title = title
        self.credit_hours = credit_hours
        self.department = department
        self.status = status

        Course.total_courses += 1

    def display_info(self):
        """Display course information (instance method)."""
        print(f"\n--- Course Details ---")
        print(f"Code         : {self.course_code}")
        print(f"Title        : {self.title}")
        print(f"Credit Hours : {self.credit_hours}")
        print(f"Department   : {self.department}")
        print(f"Status       : {self.status}")

    def update_status(self, new_status):
        """Update course status."""
        valid = ["Open", "Closed", "Cancelled"]
        if new_status in valid:
            old = self.status
            self.status = new_status
            print(f"Status of {self.course_code} changed from '{old}' to '{new_status}'.")
        else:
            print(f"Invalid status. Allowed: {valid}")

    @classmethod
    def create_standard(cls, title, credit_hours, department):
        """Class method: Create a new course with auto-generated code."""
        Course.total_courses += 1
        new_code = f"CRS{Course.total_courses:03d}"

        return cls(
            course_code=new_code,
            title=title,
            credit_hours=credit_hours,
            department=department,
            status="Open"
        )

    @staticmethod
    def validate_code_format(course_code):
        """Static method: Validate course code format."""
        return len(course_code) >= 5


# ============================================================
# DATA STRUCTURE + HELPER FUNCTIONS (Task 2)
# ============================================================
# Dictionary to store students and courses
# Key = ID / Code , Value = object
portal = {}


def add_record(record):
    """Add a Student or Course object to the portal dictionary."""
    if isinstance(record, Student):
        key = record.student_id
    elif isinstance(record, Course):
        key = record.course_code
    else:
        print("Error: Only Student or Course objects can be added.")
        return

    if key in portal:
        print(f"Record with ID/Code {key} already exists.")
    else:
        portal[key] = record
        print(f"Record {key} added successfully.")


def display_all_records():
    """Display every record in the portal."""
    if not portal:
        print("\nNo records found in the system.")
        return

    print("\n========== ALL RECORDS IN PORTAL ==========")
    for key, record in portal.items():
        record.display_info()
    print("===========================================")


def display_record_by_id(record_id):
    """Display a single record by ID or Code."""
    record = portal.get(record_id)
    if record:
        record.display_info()
    else:
        print(f"No record found with ID/Code: {record_id}")


def count_records():
    """Return total number of records."""
    return len(portal)


# ============================================================
# DEMONSTRATION / MAIN PROGRAM
# ============================================================
def main():
    print("=" * 60)
    print("          STUDENT LEARNING PORTAL")
    print("   (Aligned with Digital Public Goods Principles)")
    print("=" * 60)

    # ----- Create objects using class methods -----
    print("\n[1] Creating students and courses...")

    student1 = Student.create_standard("Year 1", "Computer Science")
    student2 = Student.create_standard("Year 2", "Information Technology")
    course1 = Course.create_standard("Introduction to Programming", 3, "Computer Science")
    course2 = Course.create_standard("Database Systems", 3, "Information Technology")

    # ----- Add to dictionary -----
    print("\n[2] Adding records to the portal (dictionary)...")
    add_record(student1)
    add_record(student2)
    add_record(course1)
    add_record(course2)

    # ----- Object interaction -----
    print("\n[3] Enrolling students in courses (object interaction)...")
    student1.enroll_course(course1.course_code)
    student1.enroll_course(course2.course_code)
    student2.enroll_course(course1.course_code)

    # ----- Display all -----
    print("\n[4] Displaying all records...")
    display_all_records()

    # ----- Instance method -----
    print("\n[5] Updating student status...")
    student2.update_status("Inactive")

    # ----- Static method -----
    print("\n[6] Validating ID formats...")
    print(f"Is 'STU-2026-001' valid? → {Student.validate_id_format('STU-2026-001')}")
    print(f"Is 'XYZ-99' valid?      → {Student.validate_id_format('XYZ-99')}")

    # ----- Summary -----
    print(f"\n[7] Total students created : {Student.total_students}")
    print(f"    Total courses created  : {Course.total_courses}")
    print(f"    Total records in portal: {count_records()}")

    print("\n" + "=" * 60)
    print("Demonstration completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()