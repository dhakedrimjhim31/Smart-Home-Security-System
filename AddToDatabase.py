import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime

cred = credentials.Certificate("smarthomesecuritysystem.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smarthomesecuritysystem-7e9a0-default-rtdb.firebaseio.com/'
})

ref = db.reference('Authorized')

data = {
    '4848':
        {
            'name': 'Vedant Tripathi',
            'last_check_in': datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        },
    '4001':
        {
            'name': 'Bill',
            'last_check_in': datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        },
    '4904':
            {
                'name': 'Prashant Rai',
                'last_check_in': datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            },
    '4905':
            {
                'name': 'Satyarth P. Srivastav',
                'last_check_in': datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            },
    '4498':
            {
                'name': 'Rimjhim',
                'last_check_in': datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
}

for key, value in data.items():
    ref.child(key).set(value)