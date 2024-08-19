from django.shortcuts import render

from audio_recognition.utils.get_text import get_text
from is_demo.integration_utils.bitrix24 import main_auth


@main_auth(on_cookies=True)
def show_info(request):
    if request.method == 'POST':
        recon_txt = get_text()
        return render(request, 'show_info.html', context={'recognized_text': recon_txt})
    return render(request, 'show_info.html')
