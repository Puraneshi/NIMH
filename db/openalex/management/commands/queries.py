from openalex.models import Works
from django.core.management.base import BaseCommand
'''
!!Find out all types available as a list!!
'''


class Command(BaseCommand):
    help = 'runs your code in the django environment'

    def handle(self, *args, **options):
        # Define the desired "type" value
        desired_type = "article"

        # Perform the query to filter by "type" and retrieve IDs
        works_with_desired_type = Works.objects.filter(type=desired_type).values_list('id', flat=True)

        # Print the IDs
        for work_id in works_with_desired_type:
            self.stdout.write(f"Work ID with type '{desired_type}': {work_id}")
