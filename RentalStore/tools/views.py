from django.shortcuts import render
from basket.forms import AddToBasketForm
from tools.models import Tool, ToolType

def tools_list(request):
    tools_list = Tool.default_manager.all()
    return render(request, 'tools.html',{'tools':tools_list})
def tool_detail(request, pk):
    tool = Tool.default_manager.get(pk=pk)
    form = AddToBasketForm({'tool':tool.id,'quantity':1})
    return render(request,'tool.html',{'tool':tool,'form':form},) 