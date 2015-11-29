# This file is part of the galatea_newsletter module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class GalateaNewsletterTestCase(ModuleTestCase):
    'Test Galatea Newsletter module'
    module = 'galatea_newsletter'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        GalateaNewsletterTestCase))
    return suite
