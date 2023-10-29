import csv
from http.client import HTTPResponse

from django.core.management.base import BaseCommand
from django.http import HttpResponse

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            product = Phone(id = phone['id'], name = phone['name'], price = phone['price'],
                            image = phone['image'], release_date = phone['release_date'],
                            lte_exists = phone['lte_exists'], slug = phone['id'])
            product.save()
            print(f'Мобильные телефон "{phone["name"]}" добавлен в базу данных.')
            # TODO: Добавьте сохранение модели
            # pass
