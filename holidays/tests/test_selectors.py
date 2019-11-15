from django.test import TestCase

from holidays.selectors import is_on_holiday
from holidays.tests.holiday_test_objects import create_holiday_test_object


# import dateutil.parser


def convert_to_date(iso_date_string):
    pass




class TestSelector(TestCase):
    def setUp(self):
        self.holiday = create_holiday_test_object()
        self.date = convert_to_date(self.holiday.date)

    def test_is_on_holiday(self):
        self.assertEqual(is_on_holiday('2019-12-25'), True)

