# This is the main cloud function that gets deployed and handles the http request
# You shouldn't put any real code here, edit your function(s) in the `functions` directory, and then just call that here
# This is built to handle http requests to pass different parameters to your function, but you may not need to leverage that depending on your use case (just leave it as-is)

import functions_framework
import functions.my_cool_function as fun 

@functions_framework.http
def hello_http(request):
    # THIS FUNCTION MUST BE THE SAME NAME AS THE CLOUD FUNCTION IN THE DEPLOYMENT
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    # If you pass json it comes here, this gets passed to your function
    # request_json = request.get_json(silent=True)    
    # resp = fun.cool_function_1(request_json)
    
    return 'hello'
