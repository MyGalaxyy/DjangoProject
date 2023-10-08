from django.contrib.auth import logout
from django.shortcuts import redirect
def handleBannedUser(get_response):

    def middleware(request):

        response = get_response(request)

        if request.user.is_authenticated:
            if request.user.isBanned:

                logout(request)
                return redirect ('404page')
                # buraya 404 yerine ,Banlandiniz seklinde bilgi veren bir html ekle

        return response
    
    return middleware