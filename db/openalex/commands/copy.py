import psycopg2
import os
from dotenv import load_dotenv

# .env variables
load_dotenv()

# Database parameters from .env
db_params = {
    'dbname': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT')
}

# Table names and corresponding CSV file paths
table_mapping = {
    'openalex_works': '/csv-files/works.csv.gz',
    'openalex_worksprimarylocations': '/csv-files/works_primary_locations.csv.gz',
    'openalex_workslocations': '/csv-files/works_locations.csv.gz',
    'openalex_worksbestoalocations': '/csv-files/works_best_oa_locations.csv.gz',
    'openalex_worksauthorships': '/csv-files/works_authorships.csv.gz',
    'openalex_worksbiblio': '/csv-files/works_biblio.csv.gz',
    'openalex_worksconcepts': '/csv-files/works_concepts.csv.gz',
    'openalex_worksids': '/csv-files/works_ids.csv.gz',
    'openalex_worksmesh': '/csv-files/works_mesh.csv.gz',
    'openalex_worksopenaccess': '/csv-files/works_open_access.csv.gz',
    'openalex_worksreferencedworks': '/csv-files/works_referenced_works.csv.gz',
    'openalex_worksrelatedworks': '/csv-files/works_related_works.csv.gz'
}
# Table names and corresponding column names.
# column names must match csv headers
table_columns = {
    'openalex_works': ['id', 'doi', 'title', 'display_name', 'publication_year', 'publication_date', 'type',
                       'cited_by_count', 'is_retracted', 'is_paratext', 'cited_by_api_url', 'abstract_inverted_index'],
    'openalex_worksprimarylocations': ['work_id', 'source_id', 'landing_page_url', 'pdf_url', 'is_oa', 'version',
                                       'license'],
    'openalex_workslocations': ['work_id', 'source_id', 'landing_page_url', 'pdf_url', 'is_oa', 'version', 'license'],
    'openalex_worksbestoalocations': ['work_id', 'source_id', 'landing_page_url', 'pdf_url', 'is_oa', 'version',
                                      'license'],
    'openalex_worksauthorships': ['work_id', 'author_position', 'author_id', 'institution_id',
                                  'raw_affiliation_string'],
    'openalex_worksbiblio': ['work_id', 'volume', 'issue', 'first_page', 'last_page'],
    'openalex_worksconcepts': ['work_id', 'concept_id', 'score'],
    'openalex_worksids': ['work_id', 'openalex', 'doi', 'mag', 'pmid', 'pmcid'],
    'openalex_worksmesh': ['work_id', 'descriptor_ui', 'descriptor_name', 'qualifier_ui', 'qualifier_name',
                           'is_major_topic'],
    'openalex_worksopenaccess': ['work_id', 'is_oa', 'oa_status', 'oa_url', 'any_repository_has_fulltext'],
    'openalex_worksreferencedworks': ['work_id', 'referenced_work_id'],
    'openalex_worksrelatedworks': ['work_id', 'related_work_id']
}

# Connect to the database
conn = psycopg2.connect(**db_params)
cursor = None
try:
    cursor = conn.cursor()

    # Execute COPY for each table
    for table_name, columns in table_columns.items():
        copy_sql = f"COPY {table_name} ({', '.join(columns)}) FROM PROGRAM 'gunzip -c {os.getcwd() + table_mapping[table_name]}' CSV HEADER"
        cursor.execute(copy_sql)

    conn.commit()
except psycopg2.Error as e:
    print(f"Error: {e}")
finally:
    if cursor:
        cursor.close()
    conn.close()
