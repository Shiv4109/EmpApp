from django.contrib import admin
from django.urls import path,include
from EmpApp import views
from rest_framework.routers import DefaultRouter

#creating router object
router= DefaultRouter()

#Register EmployeeViewSet with router
router.register('EmployeeApi', views.EmployeeModelViewSet, basename='Employee')

#Register EmployeeViewSet with router
router.register('DepartmentApi', views.DepartmentModelViewSet, basename='Department')

#Register ProjectModelViewSet
router.register('ProjectApi', views.ProjectModelViewSet, basename='Project')

#Register ManagerModelViewSet
router.register('ManagerApi', views.ManagerModelViewSet, basename='Project')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee', include(router.urls)),
    

]