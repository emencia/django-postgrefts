from importlib import import_module

from django.test import SimpleTestCase


class TestImport(SimpleTestCase):
    def test_import_models(self):
        import_module('postgrefts.models')
