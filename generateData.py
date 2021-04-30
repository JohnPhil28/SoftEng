import dbMySQL as s_db
import random as rd
import string

def generate_name():
    names_list = [
        'Johnny', 'Wiseau', 'Mia', 'Roderic', 'Melody', 
        'Mia', 'Mabini', 'Rosario', 'Juan', 'Weiss',
        'Brandy', 'Silvervale', 'Merryweather', 'Juniper', 'Calliope', 
        'Watson', 'Ina', 'Robert', 'Rosenthal', 'Haato', 
        'Jade', 'Diluc', 'Noelle', 'Venti', 'Merle',
        'Broca', 'Ceobe', 'Ceylon', 'Chiave', 'Mostima'
        ]
    name = [names_list[rd.randrange(0, len(names_list) - 1)], names_list[rd.randrange(0, len(names_list) - 1)]]
    return name

def generate_id():
    id = '20{}'.format(''.join(rd.choice(string.digits) for i in range(8)))
    try:
        if s_db.check_if_ID_exists(id):
            generate_id()
        else:
            return id
    except :
        print("Error occured")

def generate_email():
    email_list = [
        'yeah', 'lmao', 'dummy', 'elegance', 'boi',
        'Jade', 'Diluc', 'Noelle', 'Venti', 'Merle',
        'shadow', 'epic', 'poggers', 'awesome', 'xoxoxo'
        'heckin', 'flower', 'Stan', 'KPOP', 'nah',
        'gamer', 'ligma', 'miphat', '8a11s', 'hunter',
        'cho_con', 'n0tt', 'cringe', 'based', 'steve'
    ]
    email = '{}{}@gmail.com'.format(email_list[rd.randrange(0, len(email_list) - 1)], email_list[rd.randrange(0, len(email_list) - 1)])
    return email

def generate_birthdate():
    date = '{}-{}-{}'.format(rd.randrange(1995, 2005), rd.randrange(1, 12), rd.randrange(1, 28))
    return date

def generate_mobile_no():
    m_no = '09{}'.format(''.join(rd.choice(string.digits) for i in range(9)))
    return(m_no)

def generate_student_address():
    student_address_list = [
        'Akihabara, Japan', 'Cagayan de Oro, Philippines', 'Manila, Philippines', 
        'Britain, England', 'Palawan, Philippines', 'Kuala Lumpur, Malaysia', 
        'Dipolog, Philippines', 'Bukidnon, Philippines', 'Beijing, China'
    ]
    student_address = student_address_list[rd.randrange(0, len(student_address_list) - 1)]
    return student_address

def generate_course_year():
    course_list = [
        'BArch', 'BBM', 'BE', 'BN', 'CE',
        'BFA', 'BEd', 'BA', 'BHMCT', 'BLit'
        'BSBIO', 'BJ', 'BChE', 'BAE', 'BAGR',
        'BDSM', 'BOFA', ''
    ]
    course = '{}-{}'
    return course.format(course_list[rd.randrange(0, len(course_list) - 1)], rd.randrange(1, 4))

def populateTable(n):
    for x in range(n):
        name = generate_name()
        s_db.studentCreate(generate_id(), name[0], name[1], generate_student_address(), generate_course_year(), generate_birthdate(), generate_email(), generate_mobile_no())
    s_db.commitChanges()