from django.shortcuts import render ,HttpResponseRedirect
from django.http import Http404
from django.views.decorators.http import require_POST
from basket.forms import AddToBasketForm
from tools.models import Tool
from basket.models import Basket
@require_POST
def add_to_basket(request):
    response = HttpResponseRedirect(request.POST.get('next','/'))
    basket = Basket.get_basket(request.COOKIES.get('basket_id',None))
    if basket is None:
        raise Http404
    response.set_cookie("basket_id",basket.id)
    if not basket.validate_user(request.user):
        raise Http404
    form = AddToBasketForm(request.POST)
    if form.is_valid():
        form.save(basket)

    # tool_id = request.POST.get('tool_id',None)
    # if tool_id is not None:
    #     try:
    #         tool = Tool.default_manager.get(pk=tool_id)
    #     except Tool.DoesNotExist:
    #         raise Http404
    #     else:
    #         basket.add(tool)

    return response

    
    