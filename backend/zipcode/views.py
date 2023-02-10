from django.shortcuts import render
from rest_framework import status, viewsets
from .models import ZipCode
from .serializers import ZipCodeSerializer
from rest_framework.response import Response
from .utils import get_zipcode_or_raise_404, states_lojacorr
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', context=context)


class ZipCodeViewSet(viewsets.ModelViewSet):
    queryset = ZipCode.objects.all()
    serializer_class = ZipCodeSerializer

    def create(self, request):
        serializer = ZipCodeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            zipcode = serializer.save()
        if request.data.get("uf"):
            zipcode.lojacorr = request.data.get(
                "uf").upper() in states_lojacorr
            zipcode.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, zipcode_id):
        zipcode = get_zipcode_or_raise_404(zipcode_id)
        zipcode.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, zipcode_id):
        zipcode = get_zipcode_or_raise_404(zipcode_id)
        serializer = ZipCodeSerializer(
            zipcode, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            zipcode = serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
