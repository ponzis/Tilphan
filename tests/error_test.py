from unittest import TestCase

from tilphan.managers import errors


class TestTest(TestCase):
    def test_test(self):
        self.assertTrue(errors.test(), "It worked.")
