# -*- coding: utf-8 -*-
"""
Tests for pymetatop

"""
import unittest2 as unittest

from pymetatop.top import MetaTop

class PyMetaTopTest(unittest.TestCase):
    ''' Test class for pymetatop module '''
    def test_init(self):
        '''Test of init function'''
        meta = MetaTop(base_url=None)
        self.assertNotEquals(meta.base_url, None)

    def test_result(self):
        '''General test. Result top shouldn't be empty'''
        meta = MetaTop(base_url=None)
        meta.fetch()
        self.assertNotEquals(meta.top, [])

    def test_connection(self):
        '''Should raise fetching exception'''
        meta = MetaTop(base_url="https://non-existing-host.non-domain/")
        self.assertRaises(MetaTop.FetchError, meta.fetch)

    def test_parse(self):
        '''Should raise parsing exception'''
        meta = MetaTop(base_url="https://google.com/")
        self.assertRaises(MetaTop.ParseError, meta.fetch)

    def test_clean(self):
        '''  Top should be empty after executing .clean()'''
        meta = MetaTop(base_url=None)
        meta.fetch()
        self.assertNotEquals(meta.top, [])
        meta.clean()
        self.assertEquals(meta.top, [])
        