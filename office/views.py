from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import OfficeSerializer, EmployeeSerializer
from .models import OfficeModel, EmployeeModel


class OfficeViews(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = OfficeSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

    def patch(self, *args, **kwargs):
        vasia = OfficeModel.objects.get(pk=3)
        serializer = OfficeSerializer(instance=vasia, data={'name': 'Samsung'}, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def get(self, *args, **kwargs):
        manager = EmployeeModel.objects
        qs = manager.filter(office__city='Kyiv')
        data = EmployeeSerializer(qs, many=True).data
        return Response(data)
