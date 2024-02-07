[![Python application test with GitHub Actions](https://github.com/p-atharva/aws_microservice/actions/workflows/devops.yml/badge.svg)](https://github.com/p-atharva/aws_microservice/actions/workflows/devops.yml)
# aws_microservice
Learning Aws microservice from youtube tutorial

## SCaffold

1. Create a python Virtual Environment `python3 -m venv ~/.venv` or `virtualenv ~/.venv`
2. Then do `vim ~/.bashrc` and put this at the botton `source ~/.venv/bin/activate`
3. Create empty files using `touch filename`.(Makefile, requirements, Dockerfile, dirc lib, and main.py,etc)
4. Populate `Makefile`
5. Setup Continuous Integration, i.e check code for issues like lint errors

6. Build cli using Python Fire library ` ./cli_fire.py --help` to test logic
