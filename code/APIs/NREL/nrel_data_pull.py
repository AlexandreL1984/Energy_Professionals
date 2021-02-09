from code.APIs.NREL.nrel_oop import NREL_API

api = NREL_API()

# Getting Data from a Route
endpoint_params = {
                    'address': 'INPUT: ',
                        }

api.get_route('utility_rates/v3')
api.retrieve_data(endpoint_params)
