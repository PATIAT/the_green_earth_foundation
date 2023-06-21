from django.test import TestCase
from .models import Article
from django.contrib.auth.models import User


# Create your tests here.
class TestArticlesViews(TestCase):

    def test_get_contact_page(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_list.html')


class TestArticleModels(TestCase):
    def test_string_representation(self):
        article = Article(title="Test Title")
        self.assertEqual(str(article), article.title)

    def test_replied_defaults_to_false(self):
        author = User.objects.create(username="Test Author")
        article = Article.objects.create(
            title="Test Title",
            author=author,
            content="This is test article content.",
        )
        self.assertTrue(article)
