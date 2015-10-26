from django.core.urlresolvers import resolve
from django.test import TestCase
from showcase_app.views import index 

class IndexPageTest(TestCase):
    
    def test_root_url_resolves_to_index_page_view(self):
        found = resolve('/showcase/')
        self.assertEqual(found.func, index)
