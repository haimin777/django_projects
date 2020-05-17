from django.test import TestCase
from .models import Subject
# Create your tests here.

class SubjectModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Subject.objects.create(title='Chemistry', slug='chem')

    def test_title_content(self):
        subject = Subject.objects.get(id=1)

        expected_object_name = f'{subject.title}'
        self.assertEquals(expected_object_name, 'Chemistry')

    def test_slug_content(self):
        subject = Subject.objects.get(id=1)

        expected_object_name = f'{subject.slug}'
        self.assertEquals(expected_object_name, 'chem')