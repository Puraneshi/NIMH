import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database connection parameters
db_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

# Define the table names and corresponding CSV file paths
table_mapping = {
    'openalex_works': '/csv-files/works.csv.gz',
    'openalex.works_primary_locations': '/csv-files/works_primary_locations.csv.gz',
    'openalex.works_locations': '/csv-files/works_locations.csv.gz',
    'openalex.works_best_oa_locations': '/csv-files/works_best_oa_locations.csv.gz',
    'openalex.works_authorships': '/csv-files/works_authorships.csv.gz',
    'openalex.works_biblio': '/csv-files/works_biblio.csv.gz',
    'openalex.works_concepts': '/csv-files/works_concepts.csv.gz',
    'openalex.works_ids': '/csv-files/works_ids.csv.gz',
    'openalex.works_mesh': '/csv-files/works_mesh.csv.gz',
    'openalex.works_open_access': '/csv-files/works_open_access.csv.gz',
    'openalex.works_referenced_works': '/csv-files/works_referenced_works.csv.gz',
    'openalex.works_related_works': '/csv-files/works_related_works.csv.gz'
}

# print(os.getcwd()+'/csv-files/works.csv.gz')

# Establish a connection to the database
conn = psycopg2.connect(**db_params)

try:
    # Create a cursor
    cursor = conn.cursor()

    # Loop through table mappings and execute the COPY command for each table
    for table_name, csv_file_path in table_mapping.items():
        copy_sql = f"COPY {table_name} FROM PROGRAM 'gunzip -c {os.getcwd()+csv_file_path}' CSV HEADER"
        cursor.execute(copy_sql)

    # Commit the changes
    conn.commit()
except psycopg2.Error as e:
    print(f"Error: {e}")
finally:
    # Close the cursor and the database connection
    if cursor:
        cursor.close()
    conn.close()
