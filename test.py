import requests
import unittest
import json
import os
import time

os.environ['NO_PROXY'] = '127.0.0.1'
test_data = {'title': "Unique title 1", 'description': "Description for the test data"}
test_data_update = {'title': "Unique title 01", 'description': "Description for the test data updated"}
url = 'http://127.0.0.1:5000/api/v1/item/'.strip()
sleep_time = 0
test_item_id = None

class TestApi(unittest.TestCase):
    def test_get_all_api(self):
        print "-----------------------------------------------------------"
        print "Context: GET of all entries"        
        r = requests.get(url+'all')
        response_body = json.loads(r.content)
        #print "Response content: {}".format(response)
        self.assertEqual(str(r), "<Response [200]>", "Unexpected response on GET: "+ str(r))
        self.assertTrue(response_body, "Unexpected response on GET of all entries")
        time.sleep(sleep_time)

    def test_post_api(self):
        print "-----------------------------------------------------------"
        print "Context: POST for url {0} with data = {1}".format(url+'new', test_data)
        response = requests.post(url+'new', data=test_data)
        self.assertEqual(str(response), "<Response [201]>", "Unexpected response on POST: "+ str(response))
        time.sleep(sleep_time)
        
    def test_update_api(self):
        print "-----------------------------------------------------------"
        print "Context: PUT/UPDATE for url {0} with data = {1}".format(url+'update', test_data_update)
        test_item_id = json.loads(requests.get(url+'title?title='+test_data['title']).content)[0]['id']        
        test_data_update['id'] = test_item_id
        print "id of posted element is: {}".format(test_item_id)
        response = requests.put(url+'update', data=test_data_update)
        self.assertEqual(str(response), "<Response [201]>", "Unexpected response on UPDATE: "+ str(response))
        rs = json.loads(requests.get(url+str(test_item_id)).content)        
        #print rs
        self.assertEqual(rs['title'], test_data_update['title'], "Unexpected entry after UPDATE: "+ str(rs))
        time.sleep(sleep_time)

    def test_delete_api(self):
        print "-----------------------------------------------------------"
        print "Context: DELETE for url {0} with data = {1}".format(url+'delete', test_data_update)
        response = requests.delete(url+'delete', data={'id': test_item_id})
        self.assertEqual(str(response), "<Response [204]>", "Unexpected response on DELETE: "+ str(response))
        response = json.loads(requests.get(url+'all').content)
        #print response
        response_id_list = [item['id'] for item in response]
        print response_id_list
        self.assertFalse(test_item_id in response, "Unexpected response on DELETE: "+ str(response))
        time.sleep(sleep_time)

if __name__ == '__main__':
    unittest.main()