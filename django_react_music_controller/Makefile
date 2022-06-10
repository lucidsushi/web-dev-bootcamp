update-db-django:
	./manage.py makemigrations
	./manage.py migrate

run-server:
	./manage.py runserver

start-app:
# make start-app name=frontend
	django-admin startapp $(name)


run-frontend-dev:
	npm --prefix frontend/ run dev