#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

import reta


class TestStringMethods(unittest.TestCase):
    def __init__(self):
        super().__init__()
        self.tabs = reta.Tables()

    def test_upper(self):
        self.tabs.
        self.assertEqual("foo".upper(), "FOO")

    def test_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_split(self):
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == "__main__":
    unittest.main()
