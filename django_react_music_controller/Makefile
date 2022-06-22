start-app:
# make start-app name=frontend to create frontend directory in project
	django-admin startapp $(name)

update-db-django:
# run this when db/models changes
	./manage.py makemigrations
	./manage.py migrate

run-server:
# always need
	./manage.py runserver

run-frontend-dev:
# always need
	npm --prefix frontend/ run dev

lint:
	black --line-length 90 -vS .
	flake8 --max-line-length 90 .

