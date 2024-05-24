#!/usr/bin/env python3
"""
unnit testing
"""


import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize
from client import GithubOrgClient


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class that inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map function returns the expected result.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in nested map")
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_message
            ):
        """
        Test that access_nested_map function raisees.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class that inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json function returns the expected result.
        """
        # Mocking the response of requests.get
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload
        # Testing get_json
        result = get_json(test_url)

        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    TestMemoize class that inherits from unittest.TestCase.
    """

    def test_memoize(self):
        """
        Test that memoize decorator works as expected.
        """
        # Define TestClass
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Mock a_method
        with patch.object(
                TestClass, 'a_method', return_value=42
                ) as mock_method:
            # Create an instance of TestClass
            test_instance = TestClass()

            # Call a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Assert that a_method is only called once
            mock_method.assert_called_once()


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class that inherits from unittest.TestCase.
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
        Test that org function returns the correct value.
        """
        # Mocking get_json
        mock_get_json.return_value = "Mocked response"

        # Testing org
        result = GithubOrgClient(org_name).org

        self.assertEqual(result, "Mocked response")
        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}"
                )

    # Implement other test methods for Task 5, 6, 7, and 8


if __name__ == '__main__':
    unittest.main()
