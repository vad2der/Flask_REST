import requests
import unittest
import json
import os

os.environ['NO_PROXY'] = '127.0.0.1'
test_data = {'title': "Unique title 1", 'description': "Description for the test data"}
url = 'http://127.0.0.1:5000/api/v1/item/'.strip()


class TestApi(unittest.TestCase):
    def test_get_all_api(self):
        print "-----------------------------------------------------------"
        print "Context: GET of all entries"        
        r = requests.get(url+'all')
        response_body = json.loads(r.content)
        #print "Response content: {}".format(response)
        self.assertEqual(str(r), "<Response [200]>", "Unexpected response on GET: "+ str(r) )
        self.assertTrue(response_body, "Unexpected response on GET of all entries")

    def test_post_api(self):
        print "-----------------------------------------------------------"
        print "Context: POST for url {0} with data = {1}".format(url, test_data)
        response = requests.post(url+'new', data=test_data)        
        self.assertEqual(str(response), "<Response [201]>", "Unexpected response on POST: "+ str(response) )
        # response = json.loads(requests.get(url+'title?title='+test_data['title'], data=test_data))
        # self.assertEqual(response[0], test_data, "Unexpected response on GET of newly entry")

if __name__ == '__main__':
    unittest.main()