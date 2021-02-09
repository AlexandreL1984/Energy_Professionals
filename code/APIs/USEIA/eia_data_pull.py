from code.APIs.USEIA.eia_oop import USEIA_API

api = USEIA_API()

# Getting Data from a Route
endpoint_params = {
    "request":{
    "category_id":457052,
    "command":"category"
    },

api.get_route('Natural_Gas_Summary')
api.retrieve_data(endpoint_params)
