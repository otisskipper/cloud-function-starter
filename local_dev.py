# If you don't like terminal do this:
# This is a file you can run to locally mimick a call to your cloud function
# It mimicks a request object and passes it to the http function in you `main` script
# If you edit the `params` dictionary, you can change the input to the cloud function

# If you are comfortable in terminal do this:
# You can also use the functions-framework package to run your cloud function locally following this guide: https://cloud.google.com/functions/docs/running/function-frameworks
# You can then make a curl call from terminal to test your function. Here is an example: curl -X GET "localhost:8080?name=Otis"

import main 
from flask import Request

# Edit these to change the input to the cloud function (this just applies to local testing)
params = {'name': 'Otis'}

req = Request.from_values(json=params)

resp = main.hello_http(req)
print(resp)