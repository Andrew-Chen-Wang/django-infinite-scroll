import os
import operator
import timeit

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection

from public.models import English



class Command(BaseCommand):
    help = (
        "Generates test data of english dict"
    )
    requires_migrations_checks = True

    def handle(self, *args, **options):
        # Check if words_alpha.txt exists
        path_to_dictionary = os.path.join(settings.BASE_DIR, "words_alpha.txt")
        if not os.path.exists(path_to_dictionary):
            import zipfile
            try:
                with zipfile.ZipFile(path_to_dictionary[:-3] + "zip", "r") as zip_ref:
                    zip_ref.extractall(settings.BASE_DIR)
            except FileNotFoundError as e:
                raise FileNotFoundError(f"You must include the zip file of the English"
                                        f" dictionary in the BASE_DIR, specified:\n{e}.")

        def load_words() -> set:
            """370099 words in the set"""
            with open("words_alpha.txt") as file:
                valid_words = set(file.read().split())
            return valid_words

        words = [x.lower() for x in load_words()]

        blah = [English(name=x) for x in words]
        English.objects.bulk_create(blah, batch_size=20000)
