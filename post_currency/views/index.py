from django.shortcuts import render
from is_demo.integration_utils.bitrix24 import main_auth


@main_auth(on_start=True, set_cookie=True)
def index(request):
    return render(request, 'post_currency_index.html', locals())
