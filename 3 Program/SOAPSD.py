# Sistem Optimasi Alokasi Pekerjaan dan Sumber Daya
# SOAPSD.py
# Version 0.4.0

# List used
skillSet = []
skillResource = []
taskList = []
selectedResource = []

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
    'UI DESIGN': [{'name':'Figma','prov':3},{'name':'UI Design','prov':3}],
    'INTEGRASI': [{'name':'PHP','prov':3}, {'name':'Laravel','prov':4}, {'name':'Golang','prov':3}],
    'DEV DASHBOARD': [{'name':'PHP','prov':4}, {'name':'Laravel','prov':4}, {'name':'HTML','prov':3}, {'name':'CSS','prov':3}, {'name':'Bootstrap','prov':3}],
    'FRONT END': [{'name':'PHP','prov':4}, {'name':'Laravel','prov':4}, {'name':'HTML','prov':3}, {'name':'CSS','prov':3}, {'name':'Bootstrap','prov':3}],
    'FRONTEND': [{'name':'PHP','prov':4}, {'name':'Laravel','prov':4}, {'name':'HTML','prov':3}, {'name':'CSS','prov':3}, {'name':'Bootstrap','prov':3}],
    'FE': [{'name':'PHP','prov':4}, {'name':'Laravel','prov':4}, {'name':'HTML','prov':3}, {'name':'CSS','prov':3}, {'name':'Bootstrap','prov':3}],
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

# execute select task list
cursor.execute("SELECT tid,task_name,pic_id,pic_name FROM sistemoptimasialokasipekerjaan.tasktable")

# Save row to a list task
for row in cursor:
    taskList.append({'TID':row[0],'task_name':row[1],'pic_id':row[2],'pic_name':row[3]})

# close the cursor and connection
cursor.close()
conn.close()

taskName = input('Input Task Name: ')
difficultyLevel = input('Input Difficulty Level (low,med,high): ')
proviciencyLevel = input('Input Proviciency Level (beg,int,exp): ')

# Logic Skill
for task, skills in skillDict.items():
    # Split task name into words
    task_words = taskName.upper().split()
    # Check if any of the words match a task in the skillDict
    if any(word in task_words for word in task.split()):
        skillSet.extend(skills)

skillSet = [dict(t) for t in {tuple(d.items()) for d in skillSet}]

# Find matching resources
matchingResources = []
for resource in skillResource:
    for skill in skillSet:
        if any(skill['name'] == s['name'] for s in resource['skill_resource']):
            matchingResources.append(resource)
            break

# Skill calculator
# Create a dictionary to store the prov SUM for each task
taskProvSum = {}

# Create a dictionary to store the prov AVG for each task
taskProvAvg = {}

# Split the input task name into words
taskNameWords = taskName.upper().split()

# Iterate over each task and its associated skills
for task, skills in skillDict.items():
    # Initialize the prov sum to zero for this task
    taskProvSum[task] = 0

    # Check if any of the words in the input task name match a task in the skillDict
    if any(word in taskNameWords for word in task.split()):
        for skill in skills:
            taskProvSum[task] += int(skill['prov'])

# Calculate the prov sum for each matching word in the input task name
for word in taskNameWords:
    for task, skills in skillDict.items():
        if word in task.upper():
            if task not in taskProvSum:
                taskProvSum[task] = 0
            for skill in skills:
                taskProvSum[task] += int(skill['prov'])

# Calculate the average prov for all tasks that contain a matching word in the input task name
matchingTasks = list(taskProvSum.keys())
taskProvAvg = {task: taskProvSum[task] / len(skillDict[task]) for task in matchingTasks}


# Perform operations on matching resources
if len(matchingResources) == 0:
    print('No matching resources found for the given task and skills.')
else:
    # Add 'prov_avg' key to matching resources
    for resource in matchingResources:
        resource['prov_sum'] = sum(skill['prov'] for skill in resource['skill_resource'])
        resource['prov_avg'] = resource['prov_sum']/len(resource['skill_resource'])
        
        # Count the number of tasks assigned to the resource
        picDict = {}
        for task in taskList:
            if task['pic_id'] == resource['pic_id']:
                picDict[task['TID']] = task['task_name']
        
        resource['task_occupation'] = len(picDict)
    
    # Sort the matching resources based on difficulty level and task occupation
    matchingResources.sort(key=lambda x: (x['prov_sum'], x['task_occupation']) if difficultyLevel == 'low' else (-x['prov_sum'], x['task_occupation']))
    
    # Print the results
    print('Matching resources for the given task and skills:')
    for resource in matchingResources:
        print('Pic ID:', resource['pic_id'], '- Pic Name:', resource['pic_name'],'- Task Occupation:', resource['task_occupation'])
    
    # Random Forest Logic
    selectedResource = []
    for resource in matchingResources:
        if resource['prov_avg'] >= taskProvAvg.get(taskName.upper(), 0) and resource['task_occupation'] < 10: 
            selectedResource.append(resource)


    print('\n','Optimum Resource to be Selected: ')
    if len(selectedResource) == 0:
        print('No suitable resources found.')
    else:
        print('PIC Id: ',selectedResource[0]['pic_id'],'- Pic Name:', selectedResource[0]['pic_name'])