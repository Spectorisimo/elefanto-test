from django.urls import include, path


urlpatterns = [
    path('books/', include('src.api.v1.books.urls'))
]
