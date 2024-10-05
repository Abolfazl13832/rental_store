from django.urls import path
from tools.views import tools_list, tool_detail

urlpatterns = [
    path('', tools_list, name="tools_list"),
    path('detail/<int:pk>', tool_detail, name="tool_detail")

]
