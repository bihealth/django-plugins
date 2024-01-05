from django.urls import re_path

from djangoplugins.utils import include_plugins

from .plugins import ContentType
from .views import index

urlpatterns = [
    re_path(r"^$", index, name="index"),
    re_path(r"^content/", include_plugins(ContentType)),
    re_path(r"^content/", include_plugins(ContentType, r"{plugin}/(?P<pk>\d+)/", "instance_urls")),
]
