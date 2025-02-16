from django.http import JSonResponse
def test_view(request):
    return JSonResponse({"message":
                         "Backend is working"})

