#!/usr/bin/env python
# coding: utf8
#
# Python link-grammar test script
#
from itertools import chain
import unittest

from linkgrammar import Parser, Linkage, ParseOptions, Link
import _clinkgrammar as clg

class ParseOptionsTestCase(unittest.TestCase):
    def test_setting_verbosity(self):
        po = ParseOptions()
        po.verbosity = 2
        #Ensure that the PO object reports the value correctly
        self.assertEqual(po.verbosity, 2)
        #Ensure that it's actually setting it.
        self.assertEqual(clg.parse_options_get_verbosity(po._po), 2)

    def test_setting_verbosity_to_not_allow_value_raises_value_error(self):
        po = ParseOptions()
        self.assertRaises(ValueError, setattr, po, "verbosity", 14)

    def test_setting_verbosity_to_non_integer_raises_type_error(self):
        po = ParseOptions()
        self.assertRaises(TypeError, setattr, po, "verbosity", "a")

    def test_setting_linkage_limit(self):
        po = ParseOptions()
        po.linkage_limit = 3
        self.assertEqual(clg.parse_options_get_linkage_limit(po._po), 3)

    def test_setting_linkage_limit_to_non_integer_raises_type_error(self):
        po = ParseOptions()
        self.assertRaises(TypeError, setattr, po, "linkage_limit", "a")

    def test_setting_linkage_limit_to_negative_number_raises_value_error(self):
        po = ParseOptions()
        self.assertRaises(ValueError, setattr, po, "linkage_limit", -1)

    def test_setting_disjunct_cost(self):
        po = ParseOptions()
        po.disjunct_cost = 3.0
        self.assertEqual(clg.parse_options_get_disjunct_cost(po._po), 3.0)

    def test_setting_disjunct_cost_to_non_integer_raises_type_error(self):
        po = ParseOptions()
        self.assertRaises(TypeError, setattr, po, "disjunct_cost", "a")

    def test_setting_min_null_count(self):
        po = ParseOptions()
        po.min_null_count = 3
        self.assertEqual(clg.parse_options_get_min_null_count(po._po), 3)

    def test_setting_min_null_count_to_non_integer_raises_type_error(self):
        po = ParseOptions()
        self.assertRaises(TypeError, setattr, po, "min_null_count", "a")

    def test_setting_min_null_count_to_negative_number_raises_value_error(self):
        po = ParseOptions()
        self.assertRaises(ValueError, setattr, po, "min_null_count", -1)

    def test_setting_max_null_count(self):
        po = ParseOptions()
        po.max_null_count = 3
        self.assertEqual(clg.parse_options_get_max_null_count(po._po), 3)

    def test_setting_max_null_count_to_non_integer_raises_type_error(self):
        po = ParseOptions()
        self.assertRaises(TypeError, setattr, po, "max_null_count", "a")

    def test_setting_max_null_count_to_negative_number_raises_value_error(self):
        po = ParseOptions()
        self.assertRaises(ValueError, setattr, po, "max_null_count", -1)

    def test_setting_null_block(self):
        po = ParseOptions()
        po.null_block = 3
        self.assertEqual(clg.parse_options_get_null_block(po._po), 3)

    def test_setting_null_block_to_non_integer_raises_type_error(self):
        po = ParseOptions()
        self.assertRaises(TypeError, setattr, po, "null_block", "a")

    def test_setting_null_block_to_negative_number_raises_value_error(self):
        po = ParseOptions()
        self.assertRaises(ValueError, setattr, po, "null_block", -1)

    def test_setting_short_length(self):
        po = ParseOptions()
        po.short_length = 3
        self.assertEqual(clg.parse_options_get_short_length(po._po), 3)

    def test_setting_short_length_to_non_integer_raises_type_error(self):
        po = ParseOptions()
        self.assertRaises(TypeError, setattr, po, "short_length", "a")

    def test_setting_short_length_to_negative_number_raises_value_error(self):
        po = ParseOptions()
        self.assertRaises(ValueError, setattr, po, "short_length", -1)

    def test_setting_max_sentence_length(self):
        po = ParseOptions()
        po.max_sentence_length = 3
        self.assertEqual(clg.parse_options_get_max_sentence_length(po._po), 3)

    def test_setting_max_sentence_length_to_non_integer_raises_type_error(self):
        po = ParseOptions()
        self.assertRaises(TypeError, setattr, po, "max_sentence_length", "a")

    def test_setting_max_sentence_length_to_negative_number_raises_value_error(self):
        po = ParseOptions()
        self.assertRaises(ValueError, setattr, po, "max_sentence_length", -1)

    def test_setting_islands_ok(self):
        po = ParseOptions()
        po.islands_ok = True
        self.assertEqual(po.islands_ok, True)
        self.assertEqual(clg.parse_options_get_islands_ok(po._po), 1)
        po.islands_ok = False
        self.assertEqual(po.islands_ok, False)
        self.assertEqual(clg.parse_options_get_islands_ok(po._po), 0)

    def test_setting_islands_ok_to_non_boolean_raises_type_error(self):
        po = ParseOptions()
        self.assertRaises(TypeError, setattr, po, "islands_ok", "a")

    def test_setting_max_parse_time(self):
        po = ParseOptions()
        po.max_parse_time = 3
        self.assertEqual(clg.parse_options_get_max_parse_time(po._po), 3)

    def test_setting_max_parse_time_to_non_integer_raises_type_error(self):
        po = ParseOptions()
        self.assertRaises(TypeError, setattr, po, "max_parse_time", "a")

    def test_setting_screen_width(self):
        po = ParseOptions()
        po.screen_width = 3
        self.assertEqual(clg.parse_options_get_screen_width(po._po), 3)

    def test_setting_screen_width_to_non_integer_raises_type_error(self):
        po = ParseOptions()
        self.assertRaises(TypeError, setattr, po, "screen_width", "a")

    def test_setting_screen_width_to_negative_number_raises_value_error(self):
        po = ParseOptions()
        self.assertRaises(ValueError, setattr, po, "screen_width", -1)

    def test_setting_allow_null(self):
        po = ParseOptions()
        po.allow_null = True
        self.assertEqual(po.allow_null, True)
        self.assertEqual(clg.parse_options_get_allow_null(po._po), 1)
        po.allow_null = False
        self.assertEqual(po.allow_null, False)
        self.assertEqual(clg.parse_options_get_allow_null(po._po), 0)

    def test_setting_allow_null_to_non_boolean_raises_type_error(self):
        po = ParseOptions()
        self.assertRaises(TypeError, setattr, po, "allow_null", "a")

    def test_setting_display_morphology(self):
        po = ParseOptions()
        po.display_morphology = True
        self.assertEqual(po.display_morphology, True)
        self.assertEqual(clg.parse_options_get_display_morphology(po._po), 1)
        po.display_morphology = False
        self.assertEqual(po.display_morphology, False)
        self.assertEqual(clg.parse_options_get_display_morphology(po._po), 0)

    def test_setting_display_walls(self):
        po = ParseOptions()
        po.display_walls = True
        self.assertEqual(po.display_walls, True)
        self.assertEqual(clg.parse_options_get_display_walls(po._po), 1)
        po.display_walls = False
        self.assertEqual(po.display_walls, False)
        self.assertEqual(clg.parse_options_get_display_walls(po._po), 0)

    def test_setting_display_walls_to_non_boolean_raises_type_error(self):
        po = ParseOptions()
        self.assertRaises(TypeError, setattr, po, "display_walls", "a")

    def test_setting_all_short_connectors(self):
        po = ParseOptions()
        po.all_short_connectors = True
        self.assertEqual(po.all_short_connectors, True)
        self.assertEqual(clg.parse_options_get_all_short_connectors(po._po), 1)
        po.all_short_connectors = False
        self.assertEqual(po.all_short_connectors, False)
        self.assertEqual(clg.parse_options_get_all_short_connectors(po._po), 0)

    def test_setting_all_short_connectors_to_non_boolean_raises_type_error(self):
        po = ParseOptions()
        self.assertRaises(TypeError, setattr, po, "all_short_connectors", "a")


class ParserTestCase(unittest.TestCase):
    def test_specifying_options_when_instantiating_parser(self):
        p = Parser(linkage_limit=10)
        self.assertEqual(clg.parse_options_get_linkage_limit(p.parse_options._po), 10)

    def test_that_parser_can_be_destroyed_when_linkages_still_exist(self):
        """
        If the parser is deleted before the associated swig objects
        are, there will be bad pointer dereferences (as the swig
        objects will be pointing into freed memory).  This test ensures
        that parsers can be created and deleted without regard for
        the existence of PYTHON Linkage objects
        """
        p = Parser()
        linkages = p.parse_sent('This is a sentence.')
        del p



class ParsingTestCase(unittest.TestCase):
    def setUp(self):
        self.p = Parser()

    def test_that_parse_sent_returns_list_of_linkage_objects_for_valid_sentence(self):
        result = self.p.parse_sent("This is a relatively simple sentence.")
        self.assertTrue(isinstance(result, list))
        self.assertTrue(isinstance(result[0], Linkage))
        self.assertTrue(isinstance(result[1], Linkage))

    def test_utf8_encoded_string(self):
        result = self.p.parse_sent("I love going to the café.")
        self.assertTrue(isinstance(result, list))
        self.assertTrue(1 < len(result))
        self.assertTrue(isinstance(result[0], Linkage))
        self.assertTrue(isinstance(result[1], Linkage))

    def test_unicode_encoded_string(self):
        result = self.p.parse_sent(u"I love going to the caf\N{LATIN SMALL LETTER E WITH ACUTE}.".encode('utf8'))
        self.assertTrue(isinstance(result, list))
        self.assertTrue(1 < len(result))
        self.assertTrue(isinstance(result[0], Linkage))
        self.assertTrue(isinstance(result[1], Linkage))

    def test_unknown_word(self):
        result = self.p.parse_sent("I love going to the qertfdwedadt.")
        self.assertTrue(isinstance(result, list))
        self.assertTrue(1 < len(result))
        self.assertTrue(isinstance(result[0], Linkage))
        self.assertTrue(isinstance(result[1], Linkage))

    def test_unknown_euro_utf8_word(self):
        result = self.p.parse_sent("I love going to the qéáéğíóşúüñ.")
        self.assertTrue(isinstance(result, list))
        self.assertTrue(1 < len(result))
        self.assertTrue(isinstance(result[0], Linkage))
        self.assertTrue(isinstance(result[1], Linkage))

    def test_unknown_cyrillic_utf8_word(self):
        result = self.p.parse_sent("I love going to the доктором.")
        self.assertTrue(isinstance(result, list))
        self.assertTrue(1 < len(result))
        self.assertTrue(isinstance(result[0], Linkage))
        self.assertTrue(isinstance(result[1], Linkage))

    def test_getting_link_distances(self):
        result = self.p.parse_sent("This is a sentence.")[0]
        self.assertEqual(result.link_distances, [5,2,1,1,2,1,1])
        result = self.p.parse_sent("This is a silly sentence.")[0]
        self.assertEqual(result.link_distances, [6,2,1,1,3,2,1,1])

class LinkageTestCase(unittest.TestCase):
    def setUp(self):
        self.p = Parser()

    def test_getting_words(self):
        self.assertEqual(self.p.parse_sent('This is a sentence.')[0].words,
             ['LEFT-WALL', 'this.p', 'is.v', 'a', 'sentence.n', '.', 'RIGHT-WALL'])

    def test_getting_num_of_words(self):
        #Words include punctuation and a 'LEFT-WALL' and 'RIGHT_WALL'
        self.assertEqual(self.p.parse_sent('This is a sentence.')[0].num_of_words, 7)

    def test_getting_links(self):
        sent = 'This is a sentence.'
        linkage = self.p.parse_sent(sent)[0]
        self.assertEqual(linkage.links[0],
                         Link('LEFT-WALL','Xp','Xp','.'))
        self.assertEqual(linkage.links[1],
                         Link('LEFT-WALL','WV','WV','is.v'))
        self.assertEqual(linkage.links[2],
                         Link('LEFT-WALL','Wd','Wd','this.p'))
        self.assertEqual(linkage.links[3],
                         Link('this.p','Ss*b','Ss','is.v'))
        self.assertEqual(linkage.links[4],
                         Link('is.v','O*m','Os','sentence.n'))
        self.assertEqual(linkage.links[5],
                         Link('a','Ds','Ds','sentence.n'))
        self.assertEqual(linkage.links[6],
                         Link('.','RW','RW','RIGHT-WALL'))

    def test_spell_guessing_on(self):
        self.p = Parser(spell_guess = True)
        result = self.p.parse_sent("I love going to shoop.")
        for resultx in result:
            if resultx.words[5] == 'shop[~].v':
                break;
        self.assertEqual(resultx.words,
             ['LEFT-WALL', 'I.p', 'love.v', 'going.v', 'to.r', 'shop[~].v', '.', 'RIGHT-WALL'])

    def test_spell_guessing_off(self):
        self.p = Parser(spell_guess = False)
        result = self.p.parse_sent("I love going to shoop.")
        self.assertEqual(result[0].words,
             ['LEFT-WALL', 'I.p', 'love.v', 'going.v', 'to.r', 'shoop[?].v', '.', 'RIGHT-WALL'])


class LinkTestCase(unittest.TestCase):
    def test_link_display_with_identical_link_type(self):
        self.assertEqual(unicode(Link('Left','Link','Link','Right')),
                         u'Left-Link-Right')

    def test_link_display_with_identical_link_type(self):
        self.assertEqual(unicode(Link('Left','Link','Link*','Right')),
                         u'Left-Link-Link*-Right')

# Tests are run in alphabetical order; do the language tests last.
class ZLangTestCaseDE(unittest.TestCase):
    def setUp(self):
        self.p = Parser(lang = 'de')

    def test_a_getting_num_of_words(self):
        #Words include punctuation and a 'LEFT-WALL' and 'RIGHT_WALL'
        self.assertEqual(self.p.parse_sent('Dies ist den Traum.')[0].num_of_words, 7)
        self.assertEqual(self.p.parse_sent('Der Hund jagte ihn durch den Park.')[0].num_of_words, 10)

    def test_b_getting_words(self):
        self.assertEqual(self.p.parse_sent('Der Hund jagte ihn durch den Park.')[0].words,
            ['LEFT-WALL', 'der.d', 'Hund.n', 'jagte.s', 'ihn', 'durch',
               'den.d', 'Park.n', '.', 'RIGHT-WALL'])

    def test_c_getting_links(self):
        sent = 'Dies ist den Traum.'
        linkage = self.p.parse_sent(sent)[0]
        self.assertEqual(linkage.links[0],
                         Link('LEFT-WALL','Xp','Xp','.'))
        self.assertEqual(linkage.links[1],
                         Link('LEFT-WALL','W','W','ist.v'))
        self.assertEqual(linkage.links[2],
                         Link('dies','Ss','Ss','ist.v'))
        self.assertEqual(linkage.links[3],
                         Link('ist.v','O','O','Traum.n'))
        self.assertEqual(linkage.links[4],
                         Link('den.d','Dam','Dam','Traum.n'))
        self.assertEqual(linkage.links[5],
                         Link('.','RW','RW','RIGHT-WALL'))

# Tests are run in alphabetical order; do the language tests last.
class ZLangTestCaseRU(unittest.TestCase):
    def setUp(self):
        self.p = Parser(lang = 'ru')

    def test_a_getting_num_of_words(self):
        #Words include punctuation and a 'LEFT-WALL' and 'RIGHT_WALL'
        self.assertEqual(self.p.parse_sent('это тести.')[0].num_of_words, 5)
        self.assertEqual(self.p.parse_sent('вверху плыли редкие облачка.')[0].num_of_words, 7)

    def test_b_getting_words(self):
        self.assertEqual(self.p.parse_sent('вверху плыли редкие облачка.')[0].words,
            ['LEFT-WALL', 'вверху.e', 'плыли.vnndpp', 'редкие.api',
                'облачка.ndnpi', '.', 'RIGHT-WALL'])

    def test_c_getting_links(self):
        sent = 'вверху плыли редкие облачка.'
        linkage = self.p.parse_sent(sent)[0]
        self.assertEqual(linkage.links[0],
                         Link('LEFT-WALL','Xp','Xp','.'))
        self.assertEqual(linkage.links[1],
                         Link('LEFT-WALL','W','Wd','плыли.vnndpp'))
        self.assertEqual(linkage.links[2],
                         Link('вверху.e','EI','EI','плыли.vnndpp'))
        self.assertEqual(linkage.links[3],
                         Link('плыли.vnndpp','SIp','SIp','облачка.ndnpi'))
        self.assertEqual(linkage.links[4],
                         Link('редкие.api','Api','Api','облачка.ndnpi'))
        self.assertEqual(linkage.links[5],
                         Link('.','RW','RW','RIGHT-WALL'))

unittest.main()
