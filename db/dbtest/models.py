from django.db import models


class Authors(models.Model):
    id = models.TextField(primary_key=True)
    orcid = models.TextField(null=True, blank=True)
    display_name = models.TextField(null=True, blank=True)
    display_name_alternatives = models.JSONField(null=True, blank=True)
    works_count = models.IntegerField(null=True, blank=True)
    cited_by_count = models.IntegerField(null=True, blank=True)
    last_known_institution = models.TextField(null=True, blank=True)
    works_api_url = models.TextField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)


class AuthorsIds(models.Model):
    author_id = models.TextField(primary_key=True)
    openalex = models.TextField(null=True, blank=True)
    orcid = models.TextField(null=True, blank=True)
    scopus = models.TextField(null=True, blank=True)
    twitter = models.TextField(null=True, blank=True)
    wikipedia = models.TextField(null=True, blank=True)
    mag = models.BigIntegerField(null=True, blank=True)


class Concepts(models.Model):
    id = models.TextField(primary_key=True)
    wikidata = models.TextField(null=True, blank=True)
    display_name = models.TextField(null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    works_count = models.IntegerField(null=True, blank=True)
    cited_by_count = models.IntegerField(null=True, blank=True)
    image_url = models.TextField(null=True, blank=True)
    image_thumbnail_url = models.TextField(null=True, blank=True)
    works_api_url = models.TextField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)


class Works(models.Model):
    id = models.TextField(primary_key=True)
    doi = models.TextField(null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    display_name = models.TextField(null=True, blank=True)
    publication_year = models.IntegerField(null=True, blank=True)
    publication_date = models.TextField(null=True, blank=True)
    type = models.TextField(null=True, blank=True)
    cited_by_count = models.IntegerField(null=True, blank=True)
    is_retracted = models.BooleanField(null=True, blank=True)
    is_paratext = models.BooleanField(null=True, blank=True)
    cited_by_api_url = models.TextField(null=True, blank=True)
    abstract_inverted_index = models.JSONField(null=True, blank=True)

