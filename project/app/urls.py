from django.conf.urls import url
#from .views import PlanListSearchAPIView
from app import views
# from .views import EmployeeListView


urlpatterns = [

    url(r'^get-gender-info/$', views.no_male_female),
    url(r'^get-relationship-info/$', views.no_relationship),
    url(r'^EmployeeList/$', views.employeeList),

]
