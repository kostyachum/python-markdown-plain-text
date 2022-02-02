import unittest

from markdown_plain_text.extention import convert_to_plain_text


class TestCase(unittest.TestCase):
    def test_convert_to_plain_text_with_js(self):
        text = 'XSS'
        html = convert_to_plain_text(f'[Click Me](javascript:alert({text}))')
        self.assertEqual(html, 'Click Me')

    def test_convert_to_plain_text(self):
        html = convert_to_plain_text(f'# Test\n**bold**')
        self.assertEqual(html, 'Test\nbold')

    def test_convert_to_plain_text_root_tag(self):
        html = convert_to_plain_text(f'_Test thing_')
        self.assertEqual(html, 'Test thing')
