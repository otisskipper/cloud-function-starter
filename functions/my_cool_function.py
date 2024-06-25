# This is a file for whatever you want to do with your cloud function
#

# Pass a json array of parameters to this function (these came in from the http request)
def cool_function_1(params):
    print('params:', params)
    # DO STUFF HERE
    
    return '{} is a silly girl'.format(params['name'])
    # return 'the function ran'