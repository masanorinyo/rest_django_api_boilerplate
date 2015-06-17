from django.conf.urls import include, url
from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)

logger.info(HttpResponse.META)

api_version = "v1"

urlpatterns = [
  # url(r'^/v1', include( "api."+ api_version +".urls", namespace=api_version )),
  url(r'', include( "api."+ api_version +".urls", namespace=api_version )),
]
