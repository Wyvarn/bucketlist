"""
The format_suffix_pattern allows us to specify the data format (raw json or even html) when we use the URLs. It appends the format to be used to every URL in the pattern.
"""

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView


urlpatterns = {
    url("^bucketlists/$", CreateView.as_view(), name="create"),
    url("^bucketlists/(?P<pk>[0-9]+)/$", DetailsView.as_view(), name="details")
}

urlpatterns = format_suffix_patterns(urlpatterns)