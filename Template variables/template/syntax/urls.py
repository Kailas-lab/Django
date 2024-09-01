# urls.py
from django.urls import path
from .views import all_members, member_details
from .import views 

urlpatterns = [
    path('',views.testing,name='testing'),
    path('members/', all_members, name='all_members'),  # URL for the list of members
    path('members/details/<int:member_id>/', member_details, name='member_details'),  # URL for member details
]
