# Random Forest Model
# randomForest.py
# Version 0.1.0

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import CountVectorizer
import ast

import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

# Load data
data = pd.read_csv('taskTable.csv')

# Convert string representation of list of dicts to a list of dicts
data['skillResources'] = data['skill_resources'].apply(lambda x: ast.literal_eval(x))

# Convert the list of dicts in skillResources column to a string representation
data['skillResourcesStr'] = data['skillResources'].apply(str)

# Combine taskName and skillResourcesStr columns as features
data['features'] = data['skillResourcesStr'] + ' ' + data['task_name']

# Vectorize the features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['features'])

# Train a Random Forest classifier
y = data['skillResourcesStr']
rfc = RandomForestClassifier(n_estimators=100, random_state=42)
rfc.fit(X, y)

# Get the input task name from user
taskName = input("Enter a task name: ")

# Combine an empty string and taskName as features
testFeatures = ' ' + taskName

# Vectorize the test features
testFeaturesVectorized = vectorizer.transform([testFeatures])

# Predict the required skill resources for the task using the trained model
predictedSkillResources = rfc.predict(testFeaturesVectorized)

print("Skill resources needed for the task:", predictedSkillResources[0])
