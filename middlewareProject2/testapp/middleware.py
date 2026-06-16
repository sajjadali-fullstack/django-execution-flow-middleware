from django.http import HttpResponse

# We don't wanna display view.py function in template bcoz  our application is in the maintaince face

# Create Custom MiddleWare

class AppMaintainceMiddleware(object): # object is a Parent class of AppMaintainceMiddleware

    def __init__(self, get_response):  # get_response is a function
        self.get_response = get_response

    def __call__(self, request):
        # Display custom msg to he custome middleware
        return HttpResponse('<h1> Curently... Application is under maintenance.. Try after 3 Days')  
    