from django.db import models


class Authors(models.Model):
    id = models.TextField(primary_key=True)
    orcid = models.TextField(blank=True, null=True)
    display_name = models.TextField(blank=True, null=True)
    display_name_alternatives = models.JSONField(blank=True, null=True)
    works_count = models.IntegerField(blank=True, null=True)
    cited_by_count = models.IntegerField(blank=True, null=True)
    last_known_institution = models.TextField(blank=True, null=True)
    works_api_url = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)


class AuthorsCountsByYear(models.Model):
    author_id = models.TextField(primary_key=True)
    year = models.IntegerField()
    works_count = models.IntegerField(blank=True, null=True)
    cited_by_count = models.IntegerField(blank=True, null=True)


class AuthorsIds(models.Model):
    author_id = models.TextField(primary_key=True)
    openalex = models.TextField(blank=True, null=True)
    orcid = models.TextField(blank=True, null=True)
    scopus = models.TextField(blank=True, null=True)
    twitter = models.TextField(blank=True, null=True)
    wikipedia = models.TextField(blank=True, null=True)
    mag = models.BigIntegerField(blank=True, null=True)


class Concepts(models.Model):
    id = models.TextField(primary_key=True)
    wikidata = models.TextField(blank=True, null=True)
    display_name = models.TextField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    works_count = models.IntegerField(blank=True, null=True)
    cited_by_count = models.IntegerField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    image_thumbnail_url = models.TextField(blank=True, null=True)
    works_api_url = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)


class ConceptsAncestors(models.Model):
    concept_id = models.TextField(blank=True, null=True)
    ancestor_id = models.TextField(blank=True, null=True)


class ConceptsCountsByYear(models.Model):
    concept_id = models.TextField(primary_key=True)
    year = models.IntegerField()
    works_count = models.IntegerField(blank=True, null=True)
    cited_by_count = models.IntegerField(blank=True, null=True)


class ConceptsIds(models.Model):
    concept_id = models.TextField(primary_key=True)
    openalex = models.TextField(blank=True, null=True)
    wikidata = models.TextField(blank=True, null=True)
    wikipedia = models.TextField(blank=True, null=True)
    umls_aui = models.JSONField(blank=True, null=True)
    umls_cui = models.JSONField(blank=True, null=True)
    mag = models.BigIntegerField(blank=True, null=True)


class ConceptsRelatedConcepts(models.Model):
    concept_id = models.TextField(blank=True, null=True)
    related_concept_id = models.TextField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)


class Institutions(models.Model):
    id = models.TextField(primary_key=True)
    ror = models.TextField(blank=True, null=True)
    display_name = models.TextField(blank=True, null=True)
    country_code = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    homepage_url = models.TextField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)
    image_thumbnail_url = models.TextField(blank=True, null=True)
    display_name_acronyms = models.JSONField(blank=True, null=True)
    display_name_alternatives = models.JSONField(blank=True, null=True)
    works_count = models.IntegerField(blank=True, null=True)
    cited_by_count = models.IntegerField(blank=True, null=True)
    works_api_url = models.TextField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)


class InstitutionsAssociatedInstitutions(models.Model):
    institution_id = models.TextField(null=True)
    associated_institution_id = models.TextField(null=True)
    relationship = models.TextField(null=True)


class InstitutionsCountsByYear(models.Model):
    institution_id = models.TextField(primary_key=True)
    year = models.IntegerField()
    works_count = models.IntegerField(null=True)
    cited_by_count = models.IntegerField(null=True)


class InstitutionsGeo(models.Model):
    institution_id = models.TextField(primary_key=True)
    city = models.TextField(null=True)
    geonames_city_id = models.TextField(null=True)
    region = models.TextField(null=True)
    country_code = models.TextField(null=True)
    country = models.TextField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)


class InstitutionsIds(models.Model):
    institution_id = models.TextField(primary_key=True)
    openalex = models.TextField(null=True)
    ror = models.TextField(null=True)
    grid = models.TextField(null=True)
    wikipedia = models.TextField(null=True)
    wikidata = models.TextField(null=True)
    mag = models.BigIntegerField(null=True)


class Publishers(models.Model):
    id = models.TextField(primary_key=True)
    display_name = models.TextField(null=True)
    alternate_titles = models.JSONField(null=True)
    country_codes = models.JSONField(null=True)
    hierarchy_level = models.IntegerField(null=True)
    parent_publisher = models.TextField(null=True)
    works_count = models.IntegerField(null=True)
    cited_by_count = models.IntegerField(null=True)
    sources_api_url = models.TextField(null=True)
    updated_date = models.DateTimeField(null=True)


class PublishersCountsByYear(models.Model):
    publisher_id = models.TextField(primary_key=True)
    year = models.IntegerField()
    works_count = models.IntegerField(null=True)
    cited_by_count = models.IntegerField(null=True)


class PublishersIds(models.Model):
    publisher_id = models.TextField(primary_key=True)
    openalex = models.TextField(null=True)
    ror = models.TextField(null=True)
    wikidata = models.TextField(null=True)


class Sources(models.Model):
    id = models.TextField(primary_key=True)
    issn_l = models.TextField(null=True)
    issn = models.JSONField(null=True)
    display_name = models.TextField(null=True)
    publisher = models.TextField(null=True)
    works_count = models.IntegerField(null=True)
    cited_by_count = models.IntegerField(null=True)
    is_oa = models.BooleanField(null=True)
    is_in_doaj = models.BooleanField(null=True)
    homepage_url = models.TextField(null=True)
    works_api_url = models.TextField(null=True)
    updated_date = models.DateTimeField(null=True)


class SourcesCountsByYear(models.Model):
    source_id = models.TextField(primary_key=True)
    year = models.IntegerField()
    works_count = models.IntegerField(null=True)
    cited_by_count = models.IntegerField(null=True)


class SourcesIds(models.Model):
    source_id = models.TextField(primary_key=True)
    openalex = models.TextField(null=True)
    issn_l = models.TextField(null=True)
    issn = models.JSONField(null=True)
    mag = models.BigIntegerField(null=True)
    wikidata = models.TextField(null=True)
    fatcat = models.TextField(null=True)


class Works(models.Model):
    id = models.TextField(primary_key=True)
    doi = models.TextField(null=True)
    title = models.TextField(null=True)
    display_name = models.TextField(null=True)
    publication_year = models.IntegerField(null=True)
    publication_date = models.TextField(null=True)
    type = models.TextField(null=True)
    cited_by_count = models.IntegerField(null=True)
    is_retracted = models.BooleanField(null=True)
    is_paratext = models.BooleanField(null=True)
    cited_by_api_url = models.TextField(null=True)
    abstract_inverted_index = models.JSONField(null=True)


class WorksPrimaryLocations(models.Model):
    work_id = models.TextField(null=True)
    source_id = models.TextField(null=True)
    landing_page_url = models.TextField(null=True)
    pdf_url = models.TextField(null=True)
    is_oa = models.BooleanField(null=True)
    version = models.TextField(null=True)
    license = models.TextField(null=True)


class WorksLocations(models.Model):
    work_id = models.TextField(null=True)
    source_id = models.TextField(null=True)
    landing_page_url = models.TextField(null=True)
    pdf_url = models.TextField(null=True)
    is_oa = models.BooleanField(null=True)
    version = models.TextField(null=True)
    license = models.TextField(null=True)


class WorksBestOALocations(models.Model):
    work_id = models.TextField(null=True)
    source_id = models.TextField(null=True)
    landing_page_url = models.TextField(null=True)
    pdf_url = models.TextField(null=True)
    is_oa = models.BooleanField(null=True)
    version = models.TextField(null=True)
    license = models.TextField(null=True)


class WorksAuthorships(models.Model):
    work_id = models.TextField(null=True)
    author_position = models.TextField(null=True)
    author_id = models.TextField(null=True)
    institution_id = models.TextField(null=True)
    raw_affiliation_string = models.TextField(null=True)


class WorksBiblio(models.Model):
    work_id = models.TextField(primary_key=True)
    volume = models.TextField(null=True)
    issue = models.TextField(null=True)
    first_page = models.TextField(null=True)
    last_page = models.TextField(null=True)


class WorksConcepts(models.Model):
    work_id = models.TextField(null=True)
    concept_id = models.TextField(null=True)
    score = models.FloatField(null=True)


class WorksIds(models.Model):
    work_id = models.TextField(primary_key=True)
    openalex = models.TextField(null=True)
    doi = models.TextField(null=True)
    mag = models.BigIntegerField(null=True)
    pmid = models.TextField(null=True)
    pmcid = models.TextField(null=True)


class WorksMesh(models.Model):
    work_id = models.TextField(null=True)
    descriptor_ui = models.TextField(null=True)
    descriptor_name = models.TextField(null=True)
    qualifier_ui = models.TextField(null=True)
    qualifier_name = models.TextField(null=True)
    is_major_topic = models.BooleanField(null=True)


class WorksOpenAccess(models.Model):
    work_id = models.TextField(primary_key=True)
    is_oa = models.BooleanField(null=True)
    oa_status = models.TextField(null=True)
    oa_url = models.TextField(null=True)
    any_repository_has_fulltext = models.BooleanField(null=True)


class WorksReferencedWorks(models.Model):
    work_id = models.TextField(null=True)
    referenced_work_id = models.TextField(null=True)


class WorksRelatedWorks(models.Model):
    work_id = models.TextField(null=True)
    related_work_id = models.TextField(null=True)
