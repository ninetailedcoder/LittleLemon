from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import menu,booking
from .serializers import menuSerializer,bookingSerializer

# Create your views here.
def index(request):
    return render(request, 'index.html', {})


class MenuItemView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView,generics.RetrieveUpdateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer

