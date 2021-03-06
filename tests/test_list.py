import logging

from tests.base import JolokiaTestCase
from mock import Mock

logging.basicConfig(level=logging.DEBUG)


class TestList(JolokiaTestCase):

    def test_valid_request(self):

        resp = self._prepare_response(self.responses['valid_list'], 200, True)
        self.jc.session.request = Mock(return_value=resp)

        resp_data = self.jc.list(path='java.lang/type=Memory/attr/HeapMemoryUsage')

        assert type(resp_data) is dict
        assert resp_data['status'] == 200
        assert type(resp_data['value']) is dict

    def test_invalid_path(self):

        resp = self._prepare_response(self.responses['invalid_list_path'], 200, True)
        self.jc.session.request = Mock(return_value=resp)

        resp_data = self.jc.list(path='java.lang/type=Memory/HeapMemoryUsage')

        assert type(resp_data) is dict
        assert resp_data['status'] == 400
        assert resp_data['error_type'] == 'java.lang.IllegalArgumentException'
