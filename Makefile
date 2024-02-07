install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt
format:
	#format code
	black *.py lib/*.py
lint:
	#flaske8 or #pylint
	pylint --disable=R,C *.py lib/*.py
test:
	#test
	python -m pytest -vv --cov=lib --cov=main test_*.py
build:
	#build container
	docker build -t deploy-aws-fastapi .
run:
	#run docker
	#docker run -p 127.0.0.1:8080:8080 8b312c9cb94c
deploy:
	#deploy
all: install lint test deploy