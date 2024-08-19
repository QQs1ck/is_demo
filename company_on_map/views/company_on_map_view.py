from django.shortcuts import render

from is_demo.integration_utils.bitrix24 import main_auth


@main_auth(on_cookies=True)
def company_on_map(request):
    but = request.bitrix_user_token
    comp_id = but.call_list_method('crm.company.list')
    address = but.call_list_method('crm.address.list')
    return render(request, 'company_on_map_temp.html', locals())
