from django.shortcuts import render

from is_demo.integration_utils.bitrix24 import main_auth


@main_auth(on_cookies=True)
def show_company_fields(request):

    but = request.bitrix_user_token
    res = but.call_api_method("crm.company.fields")['result']
    quantity_fields = len(res)

    return render(request, 'showcompanyfields.html', locals())
