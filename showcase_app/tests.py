from django.template.loader import render_to_string
from django.test import TestCase
from django.http import HttpRequest
from showcase_app.views import index, projects, contact


class IndexPageTest(TestCase):
    
    def test_root_url_resolves_to_index_page_view(self):
        request = HttpRequest()
        response = index(request)
        expected_html = render_to_string('showcase_app/index.html')
        self.assertEqual(response.content.decode(), expected_html)

class ProjectsPageTest(TestCase):

    def test_projects_url_resolves_to_projects_page_view(self):
        request = HttpRequest()
        response = projects(request)
        expected_html = render_to_string('showcase_app/projects.html')
        self.assertEqual(response.content.decode(), expected_html)
