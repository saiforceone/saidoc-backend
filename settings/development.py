from .base import *

Debug = True

DATABASES = {
  'default': {
    'NAME': 'doctors_appointment_dev',
    'ENGINE': 'django.db.backends.mysql',
    'PORT': 3306,
    'USER': 'doctors_appt_user',
    'PASSWORD': '6nRc2_u4v!'
  }
}

GRAPHENE = {
  "SCHEMA": "doctors_appointment_core.graph_ql_api.schema"
}

print("Started Doctor's Appointment booking system in development mode...")