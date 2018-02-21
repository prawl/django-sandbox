# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from django.test import TestCase

from .models import Course, Step

class CourseModelTests(TestCase):
  def test_course_creation(self):
    course = Course.objects.create(
      title="Python Regular Expression",
      description="Learn to write regular expression in Python"
    )
    now = timezone.now()
    self.assertLess(course.created_at, now)

class StepModelTests(TestCase):
  def test_step_creation(self):
    step = Step.objects.create(
      title="Test title",
      description="Some really cool description",
      content="Content goes here",
      course=Course.objects.create()
    )
    self.assertIn(step.title, "Test title")
    self.assertIn(step.description, "Some really cool description")
    self.assertIn(step.content, "Content goes here")
