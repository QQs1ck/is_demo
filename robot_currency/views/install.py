from django.http import HttpResponse

from is_demo.integration_utils.bitrix24 import main_auth
from robot_currency.models.robot_currency_model import CurrencyRobot


@main_auth(on_cookies=True)
def install(request):
    try:
        CurrencyRobot.install_or_update('bitrix_robot_currency:handler_robot', request.bitrix_user_token)
    except Exception as exc:
        return HttpResponse(str(exc))

    return HttpResponse('ok')
