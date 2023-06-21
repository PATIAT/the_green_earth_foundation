from django.test import TestCase
from .models import TeamMember


# Create your tests here.
class TestTeamViews(TestCase):

    def test_get_teams_page(self):
        response = self.client.get('/team/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'team/team_members.html')


class TestTeamModels(TestCase):

    def test_string_representation(self):
        team = TeamMember(name="Test Name")
        self.assertEqual(str(team), team.name)

    def test_team_content(self):
        team = TeamMember.objects.create(
            name="Test Name",
            age="99",
            biography="This is a test biography",
            passion="Test Passion",
            favorite_place="Test Favourite Place",
        )

        self.assertTrue(TeamMember.name)
