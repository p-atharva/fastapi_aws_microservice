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
	python -m pytest -vv --cov=lib test_logic.py
build:
	#build container
deploy:
	#deploy
all: install lint test deploy