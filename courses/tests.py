from django.test import TestCase
from .models import Subject, Course
from django.contrib.auth.models import User

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


class CourseTests(TestCase):
    @classmethod
    def setUpTestData(cls):

        # Create a user
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')
        testuser1.save()
        test_subject = Subject.objects.create(title='Chemistry', slug='chem')
        # Create a Course
        test_course = Course.objects.create(owner=testuser1,
                                            subject=test_subject,
                                            title='C2H5OH',
                                            slug='c2h5oh',
                                            overview='overview')
        test_course.save()

    def test_course_content(self):
        course = Course.objects.get(id=1)
        owner = f'{course.owner}'
        subject = f'{course.subject}'
        title = f'{course.title}'
        slug = f'{course.slug}'
        overview = f'{course.overview}'

        self.assertEqual(owner, 'testuser1')
        self.assertEqual(subject, 'Chemistry')
        self.assertEqual(title, 'C2H5OH')
        self.assertEqual(slug, 'c2h5oh')
        self.assertEqual(overview, 'overview')
