import os
import logging
import requests
from .worker import app
from django.conf import settings

logger = logging.getLogger(__name__)

@app.task(bind=True, name='fetch_data_from_quandl')
def fetch_data_from_quandl(self, database_code, dataset_code):
    url = f'https://www.quandl.com/api/v3/dastasets/{database_code}/{dataset_code}/data.json'
    response = requests.get(url)
    logger.info(f'GET {url} returned status_code {response.status_code}')
    if response.ok:
        if not os.path.exists(settings.DATA_PATH):
            logger.info(f'{settings.DATA_PATH} does not exist, create')
            os.makedirs(settings.DATA_PATH)
        slug = f'{database_code}-{dataset_code}'
        logger.info(f'Write data to {slug}')
        with open(os.path.join(settings.DATA_PATH, slug), 'w') as f:
            f.write(response.text)

@app.task(bind=True, name='fogar_alta_garantia_prestamo')
def fogar_alta_garantia_prestamo(self, garantia):
    url = 'http://appfogar:8080/mock_alta_garantia'
    try:
        response = requests.get(url)
        logger.info(response)
        if response.ok:
            logger.info(response.text)
        else:
            logger.info('No anduvo')
    except requests.exceptions.ConnectionError:
        r.status_code = "Connection refused"

         
    

