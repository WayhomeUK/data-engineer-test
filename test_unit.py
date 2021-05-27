import unittest
import requests
from numpy import load
from collect_data_to_df import  convert_dict_dif,load_data_api1
from pandas.testing import assert_frame_equal
import pandas as pd


class TestData(unittest.TestCase):       

    api_data={}

    def test_request_response(self):
        #Send a request to the API server and store the response.
        response = requests.get('https://europe-west2-wayhome-data-engineer-test.cloudfunctions.net/rand-registry-prices')

        #Confirm that the request-response completed sucessfully.
        self.assertTrue(response.ok)
    
    def test_load_data_api1(self):               
        result = load_data_api1(self.api_data)        
        self.assertTrue(result)

    def test_convert_dict_dif(self):           
        result1 = convert_dict_dif(load_data_api1(self.api_data))        
        self.assertTrue(result1.items())
    
    

if __name__== '__main__':
    unittest.main()
