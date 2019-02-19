.PHONY: install test run

mongo-db-dump-dev:
	@echo "Importing mongo db for dev"
	mongoimport --db hivery-db --file app/resources/companies.json --jsonArray
	mongoimport --db hivery-db --file app/resources/people.json --jsonArray

mongo-db-dump-test:
	@echo "Importing mongo db for test"
	mongoimport --db hivery-test-db --file test/resources/companies.json --jsonArray
	mongoimport --db hivery-test-db --file test/resources/people.json --jsonArray

python-packages:
	@echo "Installing required python packages"
	pip install -r requirements.txt
	
setup-run:
	@echo "Setting the packages"
	python setup.py develop

install:mongo-db-dump-dev mongo-db-dump-test python-packages setup-run

test:
	@echo "Running test cases"
	python -m pytest
	@echo "Test cases completed"

run:
	@echo "Starting the app"
	python app/main.py

all:install test run

dev:install run

tests:install test
