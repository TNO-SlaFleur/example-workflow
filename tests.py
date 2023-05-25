from unittest import TestCase

class TestFoor(TestCase):

    def test__should_work(self):
        print('Hello world!')

        self.assertEqual('Hello', 'Hello')

    def test__fails_on_3_10(self):
        import sys
        # if sys.version_info[0] == 3 and sys.version_info[1] == 10:
        #     raise RuntimeError('This should fail only on 3.10')
