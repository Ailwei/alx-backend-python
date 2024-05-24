#!/usr/bin/env python3
"""
Familiarize yourself with the utils.access_nested_map function and
understand its purpose. Play with it in the Python console to make
sure you understand.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """TestAccessNestedMap class for unit testing access_nested_map function.

    Args:
        unittest (_type_): TestCase class from the unittest module.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_output):
        """Test access_nested_map function with different inputs.

        Args:
            nested_map (dict): Dictionary containing nested mappings.
            path (tuple): Tuple representing the path to access the
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_output):
        """Test access_nested_map function to raise exceptions.

        Args:
            nested_map (dict): Dictionary containing nested mappings
            expected_output (exception): Expected exception type.

        Returns:
            None
        """
        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """TestGetJson class for unit testing get_json function.

    Args:
        unittest (_type_): TestCase class from the unittest module.
    """
    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    def test_get_json(self, url, expected_output):
        """Test get_json function with mocked responses.

        Args:
            url (str): URL to retrieve JSON data from.
            expected_output (dict): Expected JSON response.

        Returns:
            None
        """
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('requests.get', return_value=mock_response):
            response = get_json(url)
            self.assertEqual(response, expected_output)


class TestMemoize(unittest.TestCase):
    """TestMemoize class for unit testing memoize decorator.

    Args:
        unittest (_type_): TestCase class from the unittest module.
    """

    def test_memoize(self):
        """Test memoize decorator functionality.

        Returns:
            None
        """

        class TestClass:
            """TestClass for memoize decorator testing.

            Args:
                None
            """
            def a_method(self):
                """Method to return a constant value.

                Returns:
                    int: Constant value.
                """
                return 42

            @memoize
            def a_property(self):
                """Property decorated with memoize.

                Returns:
                    int: Constant value.
                """
                return self.a_method()

        test_obj = TestClass()

        with patch.object(test_obj, 'a_method') as mock_method:
            mock_method.return_value = 42

            result1 = test_obj.a_property
            result2 = test_obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
