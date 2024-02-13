from e_shop.stocks.models import Stock


def img_processor(request):
    if request.user.is_authenticated:
        profile = request.user.profile
    else:
        profile = ""
    return {
        'profile': profile
    }


def products_context(request):
    products = [[product.imgstocks_set.first().img.url, f'{product.pk}'] for product in Stock.objects.all()]
    return {"products": products}
