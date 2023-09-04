# Django NIMH Project

## Project Overview

This Django project is designed to interact with and manage data from OpenAlex, an open and comprehensive catalog of scholarly papers, authors, institutions, and more. It includes models and commands for importing data, transforming it, and populating a database for further analysis. Below, you'll find essential directories, files, and instructions for setting up and running the project.

## Project Structure

### Directory: `./db/openalex`

#### Files:

- **admin.py**: This file handles the registration of models for interaction via the Django admin server.

- **models.py**: Contains the Django models adapted from OpenAlex, representing the data schema.

### Directory: `./db/openalex/commands`

#### Files:

- **pmidAPI.py**: Use this script to fetch Pubmed IDs (PMIDs) from a text file (create one if needed). It outputs a JSON Lines file and a text file listing failed searches.

- **flatten_works.py**: This script, adapted from OpenAlex, converts the gzipped JSON Lines file (`.jsonl.gz`) into CSV files suitable for database insertion.

- **copy.py**: Copies the CSV files into the database.

### Directory: `./db/openalex/commands/openalex-snapshot/data`

- Place gzipped JSON Lines files in this directory. The flattening script requires data files in this location to work.

- If you scrape more data via API, create subdirectories for `authors`, `concepts`, `institutions`, `publishers`, `sources`, and `works`.

### Directory: `./db/db`

#### Files:

- **settings.py**: Configure this file for database settings. Make sure to create a `.env` file for storing sensitive variables.

## HOW TO

Follow these steps to set up and run the project:

1. Set up your database according to your configuration in `./db/db/settings.py`.

2. Configure environment variables in a `.env` file for secure storage.

3. Run migrations using the command:
   ```bash
   python manage.py migrate
   ```
   ⚠️If you've made changes to models, run migrations again:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Run **pmidAPI.py** script to fetch data.

   ⚠️Ensure you have a text file containing Pubmed IDs (PMIDs) in the same folder as pmidAPI.py.

6. Run **flatten_works.py** to convert data into csv files.

   ⚠️Ensure the json line files are in ./openalex/openalex-snapshot/data/{`authors`, `concepts`, `institutions`, `publishers`, `sources`, or `works`}

7. Run **copy.py** to copy CSV data into the database.
   
