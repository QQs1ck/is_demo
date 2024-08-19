from django.shortcuts import render

from is_demo.integration_utils.bitrix24 import main_auth


@main_auth(on_cookies=True)
def robot_currency(request):

    return render(request, 'robot_currency_temp.html', locals())
