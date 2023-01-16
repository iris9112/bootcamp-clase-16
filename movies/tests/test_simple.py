from django.test import SimpleTestCase


class TestSimpleAssertion(SimpleTestCase):
    """SimpleTestCase disallows database queries by default"""

    def test_zero_is_false(self):
        assert 0 == False

    def test_two_plus_two_is_four(self):
        self.assertTrue(2 + 2, 4)
