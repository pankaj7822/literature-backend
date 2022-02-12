from django.urls import path
from core.views import literature_list


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('literature/',literature_list),
]
