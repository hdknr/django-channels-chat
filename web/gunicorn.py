'''
WSGI:

    gunicorn -c gunicorn.py  app.wsgi:application

ASGI: 

    gunicorn -w 4 -k uvicorn.workers.UvicornWorker -c gunicorn.py  app.asgi:application
'''
import gunicorn
gunicorn.SERVER_SOFTWARE = 'Gunicorn'

import os
import sys

# for Gunicorn to find app.wsgi:application
DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(DIR)

# logs
# http://gunicorn-docs.readthedocs.org/en/latest/deploy.html#logging
#
#  kill -USR1 $(cat /var/run/gunicorn.pid)
#
LOGS = os.path.join(os.path.dirname(DIR), 'logs')
if not os.path.isdir(LOGS):
    os.makedirs(LOGS)

# Gunicorn Configuration
accesslog = os.path.join(LOGS, "gunicorn.access.log")
errorlog = os.path.join(LOGS, "gunicorn.error.log")
pidfile = os.path.join(LOGS, "gunicorn.pid")
timeout = 180
bind = "unix:" + os.path.join(LOGS, "gunicorn.sock")
# bind = "127.0.0.1:8000"   # USE TCP
