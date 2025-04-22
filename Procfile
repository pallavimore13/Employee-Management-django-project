web: gunicorn emp_mgmt_project.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn emp_mgmt_project.wsgi
