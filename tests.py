from unittest import TestCase

class TestFoor(TestCase):

    def test__should_work(self):
        print('Hello world!')

        self.assertEqual('Hello', 'Hello')

    def test__fails(self):
        raise RuntimeError('This should fail')
