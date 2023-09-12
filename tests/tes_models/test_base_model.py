#!/usr/bin/python3
"""Unit tests for the base_model python file"""

from models.base_model import BaseModel
import datetime
import json
import unittest
from uuid import UUID

class test_basemodel(unittest.TestCase):

    def test_innit(self, *args, **kwargs):