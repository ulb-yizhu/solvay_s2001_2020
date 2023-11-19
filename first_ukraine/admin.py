from django.contrib import admin

from first_ukraine.models import User

"""
create admin user command 
python manage.py createsuperuser
memo: admin for all
"""


admin.site.register(User)
