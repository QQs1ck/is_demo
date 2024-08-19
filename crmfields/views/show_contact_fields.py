from django.shortcuts import render

from is_demo.integration_utils.bitrix24 import main_auth


@main_auth(on_cookies=True)
def show_contact_fields(request):
    but = request.bitrix_user_token
    res = but.call_api_method("crm.contact.fields")['result']
    len_res = len(res)
    return render(request, 'showcontactfields.html', locals())
