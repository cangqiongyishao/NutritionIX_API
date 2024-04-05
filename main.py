import requests
from datetime import datetime
import os

APP_ID=os.getenv('NUTRITIONIX_ID')
API_KEY=os.getenv('NUTRITIONIX_API_KEY')

exercise_endpoint='https://trackapi.nutritionix.com/v2/natural/exercise'
sheet_endpoint='https://api.sheety.co/2a16d91d2d20064fc7bdf066ad5e657e/myWorkouts（副本）/workouts'

text=input('Tell me which exercises you did:')

headers={
    'x-app-id':APP_ID,
    'x-app-key':API_KEY,
}

parameters={
    'query':text
}

response=requests.post(exercise_endpoint,json=parameters,headers=headers)
result=response.json()
print(result)


today_date=datetime.now().strftime('%d/%m/%Y')
today_time=datetime.now().strftime('%X')

sheet_headers={
    'Authorization':'Basic Y2FuZ3Fpb25neWlzaGFvOmZlbmd4aWFv'
}

for exercise in result['exercises']:
    sheet_inputs={
        'workout':{
            'date':today_date,
            'time':today_time,
            'exercise':exercise['user_input'].title(),
            'duration':exercise['duration_min'],
            'calories':exercise['nf_calories']
        }
    }

    sheet_response=requests.post(sheet_endpoint,json=sheet_inputs,headers=sheet_headers)

    print(sheet_response.text)

