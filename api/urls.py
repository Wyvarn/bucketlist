"""
The format_suffix_pattern allows us to specify the data format (raw json or even html) when we use the URLs. It appends the format to be used to every URL in the pattern.
"""

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView, DetailsView, UserView, UserDetailsView
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = {
    url("^auth/", include("rest_framework.urls", namespace="rest_framework")),
    url("^bucketlists/$", CreateView.as_view(), name="create"),
    url("^bucketlists/(?P<pk>[0-9]+)/$", DetailsView.as_view(), name="details"),
    url("^users/$", UserView.as_view(), name="users"),
    url(r'users/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token)
}

urlpatterns = format_suffix_patterns(urlpatterns)
