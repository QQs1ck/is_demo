from django.shortcuts import render
from is_demo.integration_utils.bitrix24 import main_auth


@main_auth(on_cookies=True)
def demo_data_form(request):
    return render(request, 'demodata.html', locals())
