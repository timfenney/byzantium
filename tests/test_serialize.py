# -*- coding: utf-8 -*-

from byzantium.serialize import serialize, deserialize
import unittest

class SerializeTestSuite(unittest.TestCase):
    """serialize test cases."""

    def test_serialize_round_trips_some_data(self):
        data = {
            'foo': [ 'bar', 1, 2, 3 ]
        }
        self.assertEqual(deserialize(serialize(data)), data)

if __name__ == '__main__':
    unittest.main()
