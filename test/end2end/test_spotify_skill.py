"""End-to-end tests for ovos-skill-spotify (OCP skill)."""
from unittest import TestCase

from ovoscope import get_minicroft


class TestSpotifySkillLoads(TestCase):
    """Verify the skill plugin loads and reaches READY state."""

    @classmethod
    def setUpClass(cls):
        cls.skill_id = "ovos-skill-spotify.openvoiceos"
        cls.minicroft = get_minicroft([cls.skill_id])

    @classmethod
    def tearDownClass(cls):
        if cls.minicroft:
            cls.minicroft.stop()

    def test_skill_loaded(self):
        """Skill must appear in the loaded skill set."""
        loaded_ids = [s.skill_id for s in self.minicroft.skills]
        self.assertIn(self.skill_id, loaded_ids)
