import mysql.connector

dbConn = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "Somewhere_27",
    database = "student_profiling"
    )
cursor = dbConn.cursor(buffered=True)

def check_if_ID_exists(student_id):
    sqlQuery = 'SELECT student_id FROM student_table WHERE student_id = %s'
    value = (student_id,)
    try:
        cursor.execute(sqlQuery, value)
        results = cursor.fetchall()
    
        if (len(results) == 1):
            return True
        elif (len(results) == 0):
            return False
        else:    
            print("There is more than one id: {} duplicate ids".format(len(results)))
            return False

    except mysql.connector.Error as err:
        print("Error: {}".format(err))

#for student creation
def studentCreate(student_id, fname, lname, student_address, course_year, birth_date, email, mobile_no):
    if student_id.isnumeric() and len(student_id) == 10:
        if check_if_ID_exists(student_id):
            print('Student {} already exists!'.format(student_id))
        else:
            sqlQuery = """  INSERT INTO student_table (student_id, fname, lname, student_address, course_year, birth_date, email, mobile_no) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            value = (student_id, fname, lname, student_address, course_year, birth_date, email, mobile_no)
            try:
                cursor.execute(sqlQuery, value)
                print("Student:{} added".format(student_id))
            except mysql.connector.Error as err:
                print('Error: {}'.format(err))
                print("Unable to add student")
    else:
        print('Format of student id is invalid!')
    
#for student deletion
def studentDelete(student_id):
    
    if check_if_ID_exists(student_id):
        sqlQuery = "DELETE FROM student_table WHERE student_id = %s"
        value = (student_id,)
        try:
            cursor.execute(sqlQuery, value)
            if check_if_ID_exists(student_id):
                print('Student: {} was not deleted'.format(student_id))
            else:
                print("Student: {} deleted".format(student_id))
        except mysql.connector.Error as err:
            print('Error: {}'.format(err))
            print("Unable to delete student {}".format(student_id))    
    elif student_id == None:
            print('Nothing was selected for deletion')
    else:
            print('Student: {} could not be deleted as they do not exist'.format(student_id))

#gets a particular student, also used in student update in gui
def studentView(student_id):
    sqlQuery = """  SELECT fname, lname, student_address, course_year, birth_date, email, mobile_no 
                    FROM student_table 
                    WHERE student_id = %s  """
    value = (student_id,)
    try:
        cursor.execute(sqlQuery, value)
        student = cursor.fetchone()
        if(student == None):
            print("ID: {} doesn't exist".format(student_id))
        else:
            print("Student: {} retrieved successfully".format(student_id))
            return student       
    except mysql.connector.Error as err:
        print('Error: {}'.format(err))
        print("Unable to get student")

#gets all students
def studentsView():
    sqlQuery = "SELECT * FROM student_table"
    try:
        cursor.execute(sqlQuery)
        students = cursor.fetchall()
        if(students == None):
            print("No students found")
        else:
            print("Students retrieved successfully")
            return students
    except:
        print("Unable to get students")

def executeQuerytoGetResult(query, value1, value2):
    cursor.execute(query, value1, value2)
    try: 
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return ()

#updates student info 
#will be possibly deprecated
#def studentUpdate(student_id, fname, lname, student_address, course_year, birth_date, email, mobile_no):
#    sqlQuery = """ UPDATE student_table 
#                    SET fname = %s, lname = %s, student_address = %s, course_year = %s, birth_date = %s, email  = %s, mobile_no = %s 
#                    WHERE student_id = %s"""
#    value = (fname, lname, student_address, course_year, birth_date, email, mobile_no, student_id,)

#    try:
#        cursor.execute(sqlQuery, value)
#        print("Student: {} updated successfully".format(student_id))
#    except mysql.connector.Error as err:
#        print('Error: {}'.format(err))
#        print("Unable to update student")
    
def studentUpdate_one(student_id, param, value):
    sqlQuery = "UPDATE student_table SET {} = %s WHERE student_id = %s".format(param)
    value = (value, student_id)
    try:
        cursor.execute(sqlQuery, value)
        test_query = 'SELECT student_id FROM student_table WHERE {} = %s AND student_id = %s'.format(param)
        result = executeQuerytoGetResult(test_query, value, student_id)
        if result == None:
            print("Change of {} to {} of student {} not executed".format(param, value, student_id))
        elif result == 1:
            print("Student: {} updated successfully".format(student_id))
        else:
            print("Error, one student should be updated at a time, not {}")
    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        print("Unable to update student")

#save changes to database
def commitChanges():
    try:
        dbConn.commit()
        print("Saving changes to database")
    except mysql.connector.Error as err:
        print('Error: {}'.format(err))
        print("Unable to save changes")


#def authenticate_user(user, password):
#    sqlQuery = 'SELECT COUNT username FROM user_table WHERE username = %s, password = %s'
#    value = (user, password)
#    try:
#        cursor.execute(sqlQuery, value)
#        results = cursor.fetchall()  
#        if (len(results) == 1):
#            return True
#        elif (len(results) == 0):
#            print("Incorrect password/user")
#            return False
#        else:    
#            print("There is more than one id: {}".format(len(results)))
#    except mysql.connector.Error as err:
#        print("Error: {}".format(err))
#def add_user(user, password):
#    sqlQuery = 'INSERT INTO user_table (username, password) VALUES (%s, %s)'
#    value = (user, password)
#    try:
#        cursor.execute(sqlQuery, value)
#        print("User added")
#    except mysql.connector.Error as err:
#        print('Error: {}'.format(err))
#        print("Unable to add student")
#def view_users()
#    sqlQuery = 'SELECT username WHERE '