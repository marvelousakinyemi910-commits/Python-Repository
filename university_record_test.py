import unittest
from unittest import expectedFailure

from university_record import *

class TestUniversityRecord(unittest.TestCase):
    def setUp(self):
        students["Marv101"] = { "name" : "Marvellous",
                                "age" : 25,
                                "courses": {"english", "biology"},
                                "address": {
                                    "city": "Lagos",
                                     "zip_code": "10011"
                                }

         }
    #
    def test_total_number_of_students(self):
         self.assertEqual(total_number_of_students(), 1)

    def test_that_a_city_is_displayed(self):
       self.assertEqual(display_student_city("Marv101"), "Lagos")



    def test_that_student_zip_code_is_displayed(self):

        self.assertEqual(display_student_zip_code("Marv101"), "10011")

    def test_that_student_student_courses_are_displayed(self):
        self.assertEqual( display_student_courses("Marv101"), {"english","biology"})

    def test_that_a_course_is_added(self):
        add_new_course("Marv101", "maths")
        self.assertEqual(students["Marv101"]["courses"], {"english","biology","maths"})

    def test_that_duplicate_courses_cannot_be_added(self):
        actual = add_new_course("Marv101", "english")

        expected = "Course already added"
        self.assertEqual(actual, expected)


    def test_that_a_student_record_is_displayed(self):
        actual = display_student_record("Marv101")
        expected = { "name" : "Marvellous",
                                "age" : 25,
                                "courses": {"english", "biology"},
                                "address": {
                                    "city": "Lagos",
                                     "zip_code": "10011"
                                }
                     }
        self.assertEqual(actual, expected)

    def test_that_a_student_record_is_not_displayed_if_the_username_is_not_found(self):
        actual = display_student_record("Dume111")
        expected = "Student not found"
        self.assertEqual(actual, expected)






if __name__ == '__main__':
    unittest.main()
