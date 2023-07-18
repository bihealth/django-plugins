DIRS := djangoplugins example-project

.PHONY: all
all:

.PHONY: dev-deps
dev-deps:
	pip install black==23.7.0 isort==5.12.0 flake8

.PHONY: format
format: black isort

.PHONY: isort
isort:
	isort --force-sort-within-sections --profile=black $(DIRS)

.PHONY: black
black:
	black --line-length 100 $(DIRS)

.PHONY: lint
lint: check-black check-isort flake8

.PHONY: check-black
check-black:
	black --check --diff --line-length 100 $(DIRS)

.PHONY: check-isort
check-isort:
	isort --force-sort-within-sections --profile=black --check $(DIRS)

.PHONY: flake8
flake8:
	flake8 $(DIRS)

.PHONY: test
test:
	cd example-project
	python manage.py test djangoplugins
	python manage.py makemigrations
	python manage.py migrate
	python manage.py syncplugins
