# Create this file at: countries/management/commands/fetch_countries.py
import requests
from django.core.management.base import BaseCommand
from country_app.models import Country

class Command(BaseCommand):
    help = 'Fetches country data from REST API and stores in database'

    def handle(self, *args, **options):
        self.stdout.write('Fetching country data...')
        
        try:
            response = requests.get('https://restcountries.com/v3.1/all')
            response.raise_for_status()
            countries_data = response.json()
            
            for country_data in countries_data:
                # Extract required fields
                name = country_data.get('name', {}).get('common', '')
                cca2 = country_data.get('cca2', '')
                capital = country_data.get('capital', [''])[0] if country_data.get('capital') else ''
                population = country_data.get('population', 0)
                region = country_data.get('region', '')
                subregion = country_data.get('subregion', '')
                timezones = country_data.get('timezones', [])
                languages = country_data.get('languages', {})
                flag_png = country_data.get('flags', {}).get('png', '')
                
                # Create or update country
                country, created = Country.objects.update_or_create(
                    cca2=cca2,
                    defaults={
                        'name': name,
                        'capital': capital,
                        'population': population,
                        'region': region,
                        'subregion': subregion,
                        'timezones': timezones,
                        'languages': languages,
                        'flag_png': flag_png,
                    }
                )
                
                if created:
                    self.stdout.write(f'Created {name}')
                else:
                    self.stdout.write(f'Updated {name}')
            
            self.stdout.write(self.style.SUCCESS('Successfully fetched and stored country data'))
            
        except requests.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error fetching data: {e}'))