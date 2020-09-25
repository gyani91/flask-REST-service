# flask-REST-service

## Requirements

* Python = 3.7
* Postgres >= 10.0
* Flask == 1.1.1
* everything in Conda environment.yml file

## Installation 

Install Miniconda, then:
~~~
conda env update
conda activate flask_rest_env
~~~

## DB Preparation

### Running existing migrations

* Create postgres database called `flask_rest_dev` for development or `flask_rest_live` for production.
* With an activated conda environment run:
~~~
export CONFIG_TYPE=dev
FLASK_APP=run.py flask db upgrade
~~~
Use "dev" for development server and "live" for production server.

### Creating a new migration
~~~
FLASK_APP=run.py flask db migrate -m "Description of migration"
~~~
Replace the "Description of migration" with an appropriate description.

To view the history and current version
~~~
FLASK_APP=run.py flask db history
FLASK_APP=run.py flask db current
~~~

### Code standards

Use Python Black formatting:
~~~
black --check --line-length 120 .
~~~

## Unit testing

* With an activated conda environment run:
~~~
export CONFIG_TYPE=dev
python -m pytest unit_tests/ -vs
~~~