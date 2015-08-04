#!/bin/bash
dropdb helios
createdb helios
python manage.py syncdb
python manage.py migrate
echo "from helios_auth.models import User; User.objects.create(user_type='password',user_id='me@hamidx9.ir', name='Hamid Zamani',info={'name':'Hamid Zamani', 'password':'4646679'}, admin_p='true')" | python manage.py shell
