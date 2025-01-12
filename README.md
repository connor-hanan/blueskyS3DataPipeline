# Bluesky-post API

Personal project building a data piple using Bluesky's public API to AWS S3, deployed using Dagster. I used dlt, an open-source python library, to extract and load data from Bluesky's API endpoint, and dagster to orchestrate the pipeline.

## Tools

### [dlt](https://dlthub.com/docs/intro)

dlt is an open-source Python library that loads data from various, often messy data sources into well-structured, live datasets. It offers a lightweight interface for extracting data from REST APIs, SQL databases, cloud storage, Python data structures, and many more.

dlt is designed to be easy to use, flexible, and scalable:

    - dlt infers schemas and data types, normalizes the data, and handles nested data structures.
    - dlt supports a variety of popular destinations and has an interface to add custom destinations to create reverse ETL pipelines.
    - dlt can be deployed anywhere Python runs, be it on Airflow, serverless functions, or any other cloud deployment of your choice.
    - dlt automates pipeline maintenance with schema evolution and schema and data contracts.

### [Dagster](https://docs.dagster.io/getting-started)

Dagster is an orchestrator that's designed for developing and maintaining data assets, such as tables, data sets, machine learning models, and reports.

You declare functions that you want to run and the data assets that those functions produce or update. Dagster then helps you run your functions at the right time and keep your assets up-to-date.

Dagster is designed to be used at every stage of the data development lifecycle, including local development, unit tests, integration tests, staging environments, and production.

### Python

As with every new project, we create a virtual enviroment and add the Python version we want to develop with. I'm using Python verson 3.12 for this project

1: **Create a new virtual environment with Python 3.12**

```bash
brew install python@3.12
```

2: **Create a new virtual environment with Python 3.12**

```bash
python3.12 -m venv .venv
```

3: **Activate the new virtual environment**

```bash
source .venv/bin/activate
```

4: **Install the required packages from `requirements.txt`**

```bash
pip install -r requirements.txt
```

## Orchestration

Good orchestration is absolutley key for any quality data pipeline. A well orchestated pipline will be automated, helping us ensure clean, quality data at a consistnet time thats both scalable and efficent, helping us keep cost down and trust in the data high. It will have minimal manual interventions and robust error handling. Dagster, has all that and more.

```bash
mkdir dagster_bluesky_posts
cd dagster_bluesky_posts
dagster project scaffold
```

The dagster project scaffold command generates the default folder structure, including essential files like pyproject.toml and setup.py, providing a starting point for our pipeline.
