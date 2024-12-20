from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, ArtistSerializer, AlbumSerializer, SongSerializer
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from .models import Artist, Album, Song
# Create your views here.


class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['GET', 'POST'])
def hello_world(request):
    if(request.method == 'POST'):
        return Response({'data': request.data})
    return Response({'message': 'Hello world'})


# class ArtistView(APIView):
#     authentication_classes = [authentication.TokenAuthentication]
#     # permission_classes = [permissions.IsAuthenticated]
#     permission_classes = [permissions.AllowAny]

#     def get(self, request):
#         return Response(Artist.objects.all())

#     def post(self, request):
#         return Response({'data', request.data})


""" Simplified to : """

class ArtistGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):

    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]
    # throttle_classes

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ArtistDetailsGenericView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]
    # throttle_classes

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

""" Again Simplified to : """

class ArtistView(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]
    # throttle_classes


class ArtistDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.AllowAny]
    # throttle_classes


""" Again Simplifying by merging two into one using viewsets : """

class AlbumView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.AllowAny]
    # throttle_classes
    # throttle_scope


class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.AllowAny]
    # throttle_classes
    # throttle_scope