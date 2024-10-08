from django.shortcuts import render
from ..utils.search_manager import search_manager
from is_demo.integration_utils.bitrix24 import main_auth


@main_auth(on_cookies=True)
def employee_list(request):
    but = request.bitrix_user_token
    user_dict, user_fields = search_manager(but)

    return render(request, 'list.html', context={'fields': user_fields, 'users': user_dict})
