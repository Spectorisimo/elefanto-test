from django.urls import include, path


urlpatterns = [
    path('v1/', include('src.api.v1.urls'))
]
