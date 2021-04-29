import unittest
import generateData as g
import dbMySQL as s_db

class TestApp(unittest.TestCase):
    def test_Create(self):
        print('Creation Test:')
        name = g.generate_name()
        s_id = '45vvv'
        s_db.studentCreate(s_id, name[0], name[1], g.generate_student_address(), g.generate_course_year(), g.generate_birthdate(), g.generate_email(), g.generate_mobile_no())
        s_db.commitChanges()
        self.assertTrue(s_db.check_if_ID_exists(s_id), [])
    
    def test_Delete(self):
        print('Deletion Test:')
        s_id = None
        s_db.studentDelete(s_id)
        s_db.commitChanges()
        print(s_db.check_if_ID_exists(s_id))
        self.assertFalse(s_db.check_if_ID_exists(s_id), [])
    
    #this test assumes that student below exists
    def test_View(self):
        print('Selection of One Test:')
        s_id = '545454-------------------------------'
        student = s_db.studentView(s_id)
        self.assertEqual(student, None, [])
    
    #this test assumes that there is at least one student
    def test_View_All(self):
        print('Selection of All Test:')
        student_list =s_db.studentsView()
        self.assertGreater(len(student_list), 0, [])

    def test_Update(self):
        print('Update Test:')
        #change the id number to fit any existing students in your db
        s_id = '000434'
        param = 'lname'  
        value = 'What'
        s_db.studentUpdate_one(s_id, param, value)
        s_db.commitChanges()
        query = 'SELECT student_id FROM student_table WHERE {} = %s AND student_id = %s'.format(param)
        check = s_db.executeQuerytoGetResult(query, param, s_id)
        self.assertEqual(len(check), 0, [])
