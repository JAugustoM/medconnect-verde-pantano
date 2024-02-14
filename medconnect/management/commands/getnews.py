from django.core.management.base import BaseCommand, CommandError
import requests

class Command(BaseCommand):

    help = "Get news from the News API V2"

    def add_arguments(self, parser):
        parser.add_argument(
            '--display',
            action='store_true'
        )

    def handle(self, *args, **options):
        api_key = 'f862b9961adc4d15a8639de489d90cd2'
        url = ('https://newsapi.org/v2/top-headlines?'
        'country=br&'
        'category=health&'
        'pageSize=12&'
        f'apiKey={api_key}')

        response = requests.get(url)
        data = response.json()

        for item in data["articles"]:
            print(item["title"])