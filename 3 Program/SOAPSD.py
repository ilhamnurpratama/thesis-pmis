# Sistem Optimasi Alokasi Pekerjaan dan Sumber Daya
# SOAPSD.py
# Version 0.2.0

# List used
skillSet = []
skillResource = []

# Library Used
import mysql.connector
import ast

# Logic Service
skillDict = {
    'ADAPTER': [{'name':'Way4','prov':4}, {'name':'Tibco','prov':4}],
    'MIDDLEWARE': [{'name':'Way4','prov':4}, {'name':'Tibco','prov':4}],
    'SOLUSI BISNIS': [{'name':'UML','prov':3},{'name':'Flowchart','prov':3}],
    'BRD': [{'name':'UML','prov':'3'},{'name':'Flowchart','prov':'3'}],
    'SOLUSI TEKNIS': [{'name':'ITIL','prov':3},{'name':'Sequence diagram','prov':4},{'name':'Parameter mapping','prov':4}],
    'TOR': [{'name':'ITIL','prov':3},{'name':'Sequence diagram','prov':4},{'name':'Parameter mapping','prov':4}],
    'IFA': [{'name':'ITIL','prov':3},{'name':'Sequence diagram','prov':4},{'name':'Parameter mapping','prov':4}],
    'EXECUTING': [{'name':'Project Management','prov':3}, {'name':'Scrum','prov':3}, {'name':'agile','prov':4}],
    'PLANNING': [{'name':'Project Management','prov':4}, {'name':'Scrum','prov':4}, {'name':'agile','prov':2}],
    'MEETING': [{'name':'Project Management','prov':2}],
    'PROMOTE': [{'name':'Way4','prov':3},{'name':'Tibco','prov':3},{'name':'Google Cloud','prov':2}],
    'MIGRASI': [{'name':'Way4','prov':3},{'name':'Tibco','prov':3},{'name':'Google Cloud','prov':2}],
    'DEPLOY': [{'name':'Way4','prov':3},{'name':'Tibco','prov':3},{'name':'Google Cloud','prov':2}],
    'SETTING FEE': [{'name':'FIRA','prov':3},{'name':'Portal','prov':3}],
    'KONFIGURASI REKON': [{'name':'FIRA','prov':3},{'name':'Portal','prov':3}],
    'SQA': [{'name':'Postman','prov':3}, {'name':'SOAPUI','prov':3}],
    'UI': [{'name':'Figma','prov':3}],
    'INTEGRASI': [{'name':'PHP','prov':3}, {'name':'Laravel','prov':4}, {'name':'Golang','prov':3}],
    'DEV DASHBOARD': [{'name':'PHP','prov':4}, {'name':'Laravel','prov':4}, {'name':'HTML','prov':3}, {'name':'CSS','prov':3}, {'name':'Bootstrap','prov':3}],
    'DEVELOP UI': [{'name':'PHP','prov':3}, {'name':'Laravel','prov':3}, {'name':'HTML','prov':4}, {'name':'PHP','prov':4}, {'name':'Bootstrap','prov':3}],
    'DASHBOARD': [{'name':'Tableau','prov':3}, {'name':'SQL','prov':3}, {'name':'PostgreSQL','prov':3}],
    'API': [{'name':'PHP','prov':4}, {'name':'Golang','prov':2}, {'name':'Java','prov':1}, {'name':'Python','prov':2},{'name':'SQL','prov':3}, {'name':'PostgreSQL','prov':3}],
    'APK': [{'name':'Flutter','prov':3}],
    'MOBILE': [{'name':'Flutter','prov':3}],
    'STRESS': [{'name':'SOAPUI','prov':3}],
    'UAT': [{'name':'Postman','prov':3},{'name':'Application test','prov':3}]
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
cursor.execute("SELECT pic_id,pic_name,skill_resource FROM sistemoptimasialokasipekerjaan.resourcetable")

# Generate skill from table
for row in cursor:
    skillResource.append({'pic_id': row[0], 'pic_name': row[1], 'skill_resource': ast.literal_eval(row[2])})

# close the cursor and connection
cursor.close()
conn.close()

taskName = input('Input Task Name: ')
difficultyLevel = input('Input Difficulty Level: ')

# Logic Skill
for task, skills in skillDict.items():
    if task in taskName.upper():
        skillSet.extend(skills)

skillSet = [dict(t) for t in {tuple(d.items()) for d in skillSet}]

# Find matching resources
matchingResources = []
for resource in skillResource:
    for skill in skillSet:
        if any(skill['name'] == s['name'] for s in resource['skill_resource']):
            matchingResources.append(resource)
            break

# Perform operations on matching resources
if len(matchingResources) == 0:
    print('No matching resources found for the given task and skills.')
else:
    # Sum the prov of each resource
    for resource in matchingResources:
        resource['prov_sum'] = sum(skill['prov'] for skill in resource['skill_resource'])
    
    # Sort the matching resources based on difficulty level
    if difficultyLevel == 'low':
        matchingResources.sort(key=lambda x: x['prov_sum'])
    elif difficultyLevel == 'high':
        matchingResources.sort(key=lambda x: x['prov_sum'], reverse=True)
    
    # Print the results
    print('Matching resources for the given task and skills:')
    for resource in matchingResources:
        print('Pic ID:', resource['pic_id'],'-','Pic Name:', resource['pic_name'])
