from django.http import HttpResponse


# Create your views here.
def index(request):
    """ # TODO: Add type hinting

    Args:
        request:

    Returns:

    """
    print(type(request))
    return HttpResponse("Hello, world.")
