"""
unit test for module image_output
"""
import os
import unittest
import image_output
class UnitTests(unittest.TestCase):
    """
    unit test
    """
    def test_data(self):
        '''
        Check if the output csv file exist
        '''
        image_output.image_output('userData/', 'user1.jpg')
        self.assertTrue(os.path. isfile('userData/selected_image.csv'))

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTests)
_ = unittest.TextTestRunner().run(suite)
