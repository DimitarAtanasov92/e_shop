def img_processor(request):
    if request.user.is_authenticated:
        profile = request.user.profile
    else:
        profile = ""
    return {
        'profile': profile
    }
