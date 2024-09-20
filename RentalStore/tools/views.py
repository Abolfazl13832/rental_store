from django.shortcuts import HttpResponse
from tools.models import Tool, ToolType

def tools_list(request, type):
    tools=Tool.objects.all()
    type = ToolType.objects.filter(name=type)
    m=''
    for tool in type:
        m+=f"\n{tool.name}"
    return HttpResponse(m)
