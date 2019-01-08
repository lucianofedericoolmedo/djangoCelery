import logging
import os
import json
import time

from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
def mock_alta_garantia(request, format=None):
	time.sleep(3)
	return Response('ALTA OK', status=status.HTTP_200_OK)
