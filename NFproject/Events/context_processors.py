from .models import Types


def types(request):
    return {"types": Types.objects.all()}
