import json
import requests
from getpass import getpass
from os import chdir, getcwd, listdir, makedirs

class USEIA_API:
    def __init__(self):
        self.key = getpass("Pass in your USEIA API Key: ")

    def get_route(self, endpoint_name: str):
        self.endpoint_name = endpoint_name
        some_route = f"{self.endpoint_name}"

        return f"https://api.eia.gov/series/?{some_route}.json"

    def retrieve_data(self, parameters: dict):

        self.route = self.get_route(self.endpoint_name)
        headers = {
              'Accepts': 'application/json',
              'X-Api-Key:': self.key,
            }

        # Create a HTTP Get Request based on the Final Route
        resp = requests.get(self.route, headers=headers).json()

        route_str = self.endpoint_name.split('/')
        route_folder = '_'.join(route_str)

        nrel_path = getcwd() + "/data/APIs/USEIA"

        if route_folder not in listdir(USEIA_path):
            chdir(nrel_path)
            makedirs(route_folder)
            chdir("../../..")

        # Serializing the Data with Version Control
        json_path = getcwd() + f"/data/APIs/USEIA/{route_folder}/json"
        vc_path = getcwd() + f"/data/APIs/USEIA/{route_folder}/version_check"

        # If the cryptocurrency quote endpoint hasn't been requested before, then generate this file
        if f"{self.endpoint_name}.txt" not in listdir(vc_path):
            with open(f"{vc_path}/{self.endpoint_name}.txt", "w") as my_file:
                my_file.write("0")

        # Storing the version number in memory
        version = int([line.replace("\n", "") for line in open(f"{vc_path}/{self.endpoint_name}.txt", "r").readlines()][0])

        # Read in the File that was written to update the version number
        with open(f"{vc_path}/{self.endpoint_name}.txt", "w") as my_file:
            my_file.write(f"{version + 1}")

        # Saving JSON File with correct version number
        with open(f"{json_path}/{self.endpoint_name}_v{version}.json", "w") as my_file:
            json.dump(resp, my_file)

        return self.route
