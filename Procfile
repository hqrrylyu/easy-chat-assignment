release: python manage.py makemigrations && python manage.py migrate
web: daphne domecode.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=config.settings -v2
