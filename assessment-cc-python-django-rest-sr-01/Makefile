.PHONY: dev
test:
	coverage run --source='.' manage.py test && coverage report && coverage html

test_module:
	@read -p "Enter Module Name: " test_module; \
	coverage run --source=./$$test_module manage.py test $$test_module && coverage report && coverage html

createsuperuser:
	python manage.py createsuperuser

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver

shell_plus:
	python manage.py shell_plus

PYLINT_FILES = battle/models_extended.py battle/utils_extended.py battle/views_extended.py monster/nested_serializers_extended.py monster/views_extended.py
lint:
	pylint $(PYLINT_FILES)
black:
	python -m black --target-version=py37 .
