from django.views.generic import ListView
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from core import models, forms, filters, serializers


class ProgrammerViewSet(viewsets.ModelViewSet):
    queryset = models.Programmer.objects.all()
    serializer_class = serializers.Programmer


# class Programmer(APIView):
#
#     def get(self, request):
#         qs = models.Programmer.objects.all()
#         names = [p.name for p in qs]
#
#         return Response(names)
#
#     def get(self, request):
#         qs = models.Programmer.objects.all()
#         serializer = serializers.Programmer(qs, many=True)
#
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = serializers.Programmer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'massage': 'OK'})
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = Programmer(snippet, data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
