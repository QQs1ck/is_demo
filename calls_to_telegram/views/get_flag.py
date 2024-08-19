from django.http import HttpResponse
from is_demo.integration_utils.bitrix24 import main_auth
from is_demo.integration_utils.bitrix24 import BitrixUserToken


@main_auth(on_cookies=True)
def get_flag(request):
    if request.method == 'GET':
        but = BitrixUserToken.objects.filter(user__is_admin=True, is_active=True).first()
        try:
            flag = but.call_api_method('app.option.get', {})['result']['call_sync_flag']
        except (KeyError, TypeError):
            flag = "false"
            but.call_api_method('app.option.set', {'options': {'call_sync_flag': flag}})
        return HttpResponse(f"{flag}")
    return HttpResponse("Invalid state or token.")
