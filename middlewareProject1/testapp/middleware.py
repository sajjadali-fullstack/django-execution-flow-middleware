class ExecutionFlowMiddleware(object):  # object is a Parent class of ExecutionFlowMiddleware

    # The python class should contain 2 mandatory methods

    # 1. constructor method
    # NOTEs: This method will be executed only once at a time of creating middleware class object, which is mostly happen at a time of server starting
    def __init__(self, get_response):  # self --> It is belong to the same class, get_response --> is a function which It will generate the response and it will get the request 
        print("init method execution")  # 1 op in terminal after server start
        self.get_response = get_response


    # 2. call method
    def __call__(self, request):
        print('Pre processing of request')  #2 op in terminal after refreshing the page
        response =  self.get_response(request)
        print('Post processing of request')  # 4 op in terminal after refreshing the page
        return response