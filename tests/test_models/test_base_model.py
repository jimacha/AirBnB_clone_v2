#!/usr/bin/python3
"""
Test module for the BaseModel class
"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class to test the BaseModel class
    """
    def test_instance_attributes(self):
        """
        Test initialization of instance attributes
        """
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_save_method(self):
        """
        Test save method
        """
        base_model = BaseModel()
        previous_updated_at = base_model.updated_at
        base_model.save()
        self.assertNotEqual(previous_updated_at, base_model.updated_at)

    def test_to_dict_method(self):
        """
        Test to_dict method
        """
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['class'], 'BaseModel')
        self.assertEqual(obj_dict['id'], base_model.id)
        self.assertEqual(obj_dict['created_at'],
                         base_model.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'],
                         base_model.updated_at.isoformat())


if name == 'main':
    unittest.main()
