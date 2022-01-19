import unittest, requests

class APITest(unittest.TestCase):
    API_URL = "http://127.0.0.1:8000"
    GET_CALL_ENDPOINT = "{}/get?url=www.Amazon.com".format(API_URL)
    GET_CALL_ENDPOINT_N = "{}/get?url=www.Amazon123.com".format(API_URL)  # N stands for -ve test case
    POST_CALL = "{}/create".format(API_URL)
    PAYLOAD = {"url": "www.musicband.com"}
    UPDATE_call = "{}/update".format(API_URL)
    DELETE_call = "{}/update".format(API_URL)

    def test_1_get_shorten_url_by_original_url(self):
        """
        Test to perform get call and validate the status code.
        """
        r = requests.get(APITest.GET_CALL_ENDPOINT)
        self.assertEqual(r.status_code, 200)

    # test case ending with negative says these are -ve test cases where API fails.
    def test_2_get_shortenurl_by_non_existing_original_url_negative(self):
        """
        Test to perform get call for the url which is not exist and validate the error msg.
        """
        r = requests.get(APITest.GET_CALL_ENDPOINT_N)
        msg = "url not found, Please do a POST call"
        self.assertEqual(r.json()['Error_msg'], msg)

    def test_3_create_new_shorten_url(self):
        """
        Test to create a shortend url for the given url.
        """
        r = requests.post(APITest.POST_CALL, json=APITest.PAYLOAD)
        self.assertEqual(r.status_code, 201)

    def test_4_create_new_shorten_url_negative(self):
        """
        Test to validate that trying to create url which is shortend already and validate the error message.
        """
        r = requests.post(APITest.POST_CALL, json=APITest.PAYLOAD)
        list = r.json()['Error_msg'].split()
        msg = "url already shortened {}".format(list[-1])
        self.assertEqual(r.json()['Error_msg'], msg)

    def test_5_update_shorten_url(self):
        """
        Test to update the shorten url and validate the status code and shorten_url.
        """
        api = "{}/get?{}".format(APITest.API_URL, "url=www.Google.com")
        r = requests.get(api)
        self.assertEqual(r.status_code, 200)
        list1 = r.json()['www.Google.com'].split() # Fetching the old shorten url
        r1 = requests.put(APITest.UPDATE_call, json={"url": "www.Google.com"})
        self.assertEqual(r1.status_code, 200)
        list2 = r1.json()['Success'].split() # Fetching the updated shorten url
        assert list1[-1] != list2[-1], 'Shorten url not updated' # Both should be different after updating

    def test_6_update_shorten_url_negative(self):
        """
        Test to update url which is empty
        """
        r = requests.put(APITest.UPDATE_call, json={"url": ""})
        msg = "url not present, Please do a POST call"
        self.assertEqual(r.json()['Error_msg'], msg)











