from pymysql.err import InternalError
import mymariasql


password = '123'
username = 'phpmyadmin'


db = mymariasql.MariaSQL(host='localhost', user=username, password=password)


def setup():
    db.create_db('iturmas')
    db.use('iturmas')

    """
    enrollments = {
        # 'id': int,
        'term_name': str,
        'date_opening': str,       # datetime timestamp format
        'date_deadline': str,      # datetime timestamp format
        'db_name': str, 
        'archived': int,            # bool
        'runs': int,
        'pdf_filename': str,
        'csv_filename': str
    }
    """

    students = {
        # 'id': int,
        'name': str,
        'code': 'VARCHAR(30)',
        'max_load': int,
        'properties': dict
    }

    courses = {
        # 'id': int,
        'name': str,
        'code': str
    }

    classes = {
        # 'id': int,
        'course_id': int,
        'code': str,
        'schedule': str,
        'vacancies': int,
        'properties': dict
    }

    class_applications = {
        # 'id': int,
        'class_id': int,
        'student_id': int,
        'preference': int
    }

    course_applications = {
        # 'id': int,
        'course_id': int,
        'student_id': int,
        'preference': int
    }

    db.create_table('students', students, primary_key='code')
    db.create_table('courses', courses)
    db.create_table('classes', classes)
    db.create_table('class_applications', class_applications)
    db.create_table('course_applications', course_applications)

    db.query('CREATE FULLTEXT INDEX IF NOT EXISTS names ON students(name);')
    db.query('CREATE FULLTEXT INDEX IF NOT EXISTS codes ON students(code);')


try:
    db.use('iturmas')
except InternalError:
    setup()
