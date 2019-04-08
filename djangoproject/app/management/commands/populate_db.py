from django.core.management.base import BaseCommand
from app.models import Phase, Tag, ContentType
from django.contrib.auth.models import Group

class Command(BaseCommand):
        
    def _create_tags(self):
        tags = ["Social", "Economics", "Environment", "Security", "Artificial Intelligence", "Development"]
        for tag in tags:
            temp = Tag(title=tag)
            temp.save()

    def _create_phases(self):
        phases = ["Ideating", "Concepting", "Committing", "Validating", "Scaling", "Establishing"]
        for phase in phases:
            temp = Phase(title=phase)
            temp.save()

    def _create_contentTypes(self):
        contentTypes = ["Blogpost", "Article", "Event"]
        for contentType in contentTypes:
            temp = ContentType(title=contentType)
            temp.save()

    def _create_groups(self):
        groups = ["Person", "Startup", "Investor"]
        for group in groups:
            temp = Group(name=group)
            temp.save()

    def handle(self, *args, **options):
        self._create_tags()
        self._create_phases()
        self._create_contentTypes()
        self._create_groups()
