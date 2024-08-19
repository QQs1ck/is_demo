from django.shortcuts import render

from is_demo.integration_utils.bitrix24 import main_auth


@main_auth(on_cookies=True)
def entrance(request):
    """
    Отображает описание приложения.
    """

    return render(request, 'export_deals_temp.html')
