from io_xplane2blender.xplane_export_skip_unchanged import (
    content_hash,
    should_skip_unchanged_export,
)
from io_xplane2blender.tests import *


class TestSkipUnchangedRootExports(XPlaneTestCase):
    def test_content_hash_is_stable(self):
        text = "A\n1\n2\n3\n"
        self.assertEqual(content_hash(text), content_hash(text))
        self.assertNotEqual(content_hash(text), content_hash(text + "x"))

    def test_should_skip_when_hash_matches(self):
        text = "OBJ content"
        stored = content_hash(text)
        self.assertTrue(
            should_skip_unchanged_export(True, False, stored, text),
        )

    def test_should_not_skip_when_disabled_or_forced(self):
        text = "OBJ content"
        stored = content_hash(text)
        self.assertFalse(should_skip_unchanged_export(False, False, stored, text))
        self.assertFalse(should_skip_unchanged_export(True, True, stored, text))

    def test_should_not_skip_without_stored_hash(self):
        self.assertFalse(
            should_skip_unchanged_export(True, False, "", "first export"),
        )


runTestCases([TestSkipUnchangedRootExports])
