# Sistem Optimasi Alokasi Pekerjaan dan Sumber Daya
# SOAPSD.py
# Version 0.1.0

# Library Used
import pandas as pd
import mysql.connector

skillDict = {
    'ADAPTER': ['Way4', 'Tibco'],
    'MIDDLEWARE': ['Way4', 'Tibco'],
    'SOLUSI BISNIS': ['UML', 'Flowchart'],
    'BRD': ['UML', 'Flowchart'],
    'SOLUSI TEKNIS': ['ITIL', 'Sequence Diagram', 'Parameter Mapping'],
    'TOR': ['ITIL', 'Sequence Diagram', 'Parameter Mapping'],
    'IFA': ['ITIL', 'Sequence Diagram', 'Parameter Mapping'],
    'EXECUTING': ['Project Management', 'scrum', 'agile'],
    'PLANNING': ['Project Management', 'scrum', 'agile'],
    'MEETING': ['Project Management'],
    'PROMOTE': ['Way4', 'Tibco', 'Google Cloud'],
    'MIGRASI': ['Way4', 'Tibco', 'Google Cloud'],
    'DEPLOY': ['Way4', 'Tibco', 'Google Cloud'],
    'SETTING FEE': ['FIRA', 'Portal'],
    'KONFIGURASI REKON': ['FIRA', 'Portal'],
    'SQA': ['Postman', 'SOAPUI'],
    'UI': ['Figma'],
    'INTEGRASI': ['PHP', 'Laravel', 'Golang'],
    'DEV DASHBOARD': ['PHP', 'Laravel', 'HTML', 'CSS', 'Bootstrap'],
    'DEVELOP UI': ['PHP', 'Laravel', 'HTML', 'CSS', 'Bootstrap'],
    'DASHBOARD': ['Tableau', 'SQL', 'PostgreSQL'],
    'API': ['PHP', 'Golang', 'Java', 'Python', 'SQL', 'PostgreSQL'],
    'APK': ['Flutter'],
    'MOBILE': ['Flutter'],
    'STRESS': ['SOAPUI'],
    'UAT': ['Postman', 'Application test']
}

# DATA LOADER
# establish a connection to the MySQL server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dr@gblacker05",
    database="sistemoptimasialokasipekerjaan"
)

# create a cursor object to interact with the database
cursor = conn.cursor()

# execute a SELECT statement
cursor.execute("SELECT PID FROM sistemoptimasialokasipekerjaan.projecttable")

# fetch all rows from the result set
rows = cursor.fetchall()

# print the rows
#for row in rows:
    #print(row)

# close the cursor and connection
cursor.close()
conn.close()

taskName = input('Input Task Name: ')

# Logic Skill
for task, skills in skillDict.items():
    if task in taskName.upper():
        skillSet.extend(skills)

skillSet = list(set(skillSet))
print(skillSet)