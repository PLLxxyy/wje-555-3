from django.core.management.base import BaseCommand
from django.db import connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        self.stdout.write("ok")

