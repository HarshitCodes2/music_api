from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from music_api_be.views import UserViewsets, hello_world, ArtistView, ArtistDetailsView, AlbumView, SongView
from rest_framework.schemas import get_schema_view
from django.views.generic.base import TemplateView

router = routers.DefaultRouter()
router.register(r'users', UserViewsets) #add Userviewset
router.register(r'songs', SongView)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("test/", hello_world, name='hello_world'),
    path("artists/", ArtistView.as_view(), name='artists'),
    path("artists/<int:pk>", ArtistDetailsView.as_view(), name='artists_details'),
    # Using viewset view without router : 
    path("albums", AlbumView.as_view({'get': 'list', 'post': 'create'}), name='album'),
    path("albums/<int:pk>", AlbumView.as_view({'delete': 'destroy', 'put': 'update', 'get': 'retrieve'}), name='album_details'),
    # To use viewset view with router do what line 7-9 does for SongView
    path(r'openapi-schema', get_schema_view(
        title="Music API",  # Title of your app
        description="Music catalog API",  # Description of your app
        version="1.0.0",
        public=True,
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name = 'music_api_be/swagger-ui.html',
        extra_context = {'schema_url': 'openapi-schema'}
    ), name='swagger-ui')
]

