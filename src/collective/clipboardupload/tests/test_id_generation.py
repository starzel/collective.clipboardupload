import unittest
from plone.app.testing import TEST_USER_ID, setRoles
from collective.clipboardupload.testing import COLLECTIVE_CLIPBOARDUPLOAD_FUNCTIONAL_TESTING
from collective.clipboardupload.imageupload import generate_image_id

class TestIdGeneration(unittest.TestCase):

    layer = COLLECTIVE_CLIPBOARDUPLOAD_FUNCTIONAL_TESTING

    def test_default_method(self):
        portal = self.layer['portal']
        self.assertTrue(generate_image_id(portal).startswith('Clipboard_image_'))
       
    def test_acquired_method(self):
        portal = self.layer['portal']
        def dummy_generate_image_id(context):
            return "FooBar"
        setattr(portal, 'generate_image_id', dummy_generate_image_id)
        self.assertEqual(generate_image_id(portal), 'FooBar')
        delattr(portal, 'generate_image_id')
        
