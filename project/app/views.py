from rest_framework import status
import json

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from app.models import *
from app.serializers import EmployeeSerializer

@api_view(['GET'])
@method_decorator(cache_page(60*60*2))
def no_male_female(request):

    if request.method == 'GET':

        male_female_count = Employee.objects.values('sex').annotate(count=Count('sex'))
        return Response({"data":male_female_count},status=status.HTTP_200_OK)

    else:

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@method_decorator(cache_page(60*60*2))
def no_relationship(request):

    if request.method == 'GET':

        relationship_count = Employee.objects.values('relationship').annotate(count=Count('relationship'))
        return Response({"data":relationship_count},status=status.HTTP_200_OK)


    else:

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


from django_filters import FilterSet
from django_filters import rest_framework as filters


class EmployeeFilter(FilterSet):
    sex = filters.CharFilter(method="filter_by_sex")
    race = filters.CharFilter(method="filter_by_race")
    relationship = filters.CharFilter(method="filter_by_relationship")

    class Meta:
        model = Employee
        fields = ["sex","race","relationship"]

    def filter_by_sex(self,queryset,name,value):
        sex_names = value.strip().split(",")
        sexs = Employee.objects.filter(sex__in = sex_names)
        return queryset.filter(sexs__in = tags).distinct()

    def filter_by_race(self,queryset,name,value):
        race_names = value.strip().split(",")
        races = Employee.objects.filter(race__in = race_names)
        return queryset.filter(races__in = races).distinct()

    def filter_by_relationship(self,queryset,name,value):
        relationship_names = value.strip().split(",")
        relationships = Employee.objects.filter(relationship__in = relationship_names)
        return queryset.filter(relationships__in = relationships).distinct()


@api_view(['GET'])
@method_decorator(cache_page(60*60*2))
def employeeList(request):

    if request.method == 'GET':
        qs=Employee.objects.all()

        filter_backends = (DjangoFilterBackend,)
        # filter_class = EmployeeFilter
        f = EmployeeFilter(request.GET, queryset=qs)
        # print(f)
        serializer=EmployeeSerializer(f,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    else:

        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
