import http

from django.test import TestCase

from .models import Episode


class EpisodeTests(TestCase):

    def setUp(self):
        self.episode = Episode.objects.create(
            title='test'
        )
        self.episode_list = Episode.objects.all()

    def test_episode_create(self):
        self.assertEqual(self.episode.title, 'test')

    def test_episode_list(self):
        self.assertEqual(self.episode_list, 1)

    def test_episode_update(self):
        self.episode.title = 'test2'
        self.episode.save()
        self.assertEqual(self.episode.title, 'test2')

    def test_episode_delete(self):
        self.episode.delete()
        self.assertEqual(self.episode.title, 'test')



