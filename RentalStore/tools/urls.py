from django.urls import path
from tools.views import tools_list

urlpatterns = [
    path('<str:type>', tools_list, name="tools_list")
]
