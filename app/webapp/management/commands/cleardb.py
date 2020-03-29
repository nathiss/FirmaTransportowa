from django.core.management.base import BaseCommand, no_translations

# pylint: disable=import-error
from webapp.models import Post

class Command(BaseCommand):
    help = 'Populates the databse with example data.'

    def __clear_posts(self):
        posts = Post.objects.all()
        if len(posts) == 0:
            self.stderr.write(self.style.WARNING('Post table has no entries.'))
        else:
            posts.delete()
            self.stdout.write(self.style.SUCCESS('Deleted all entries in Post table.'))

    @no_translations
    def handle(self, *args, **kwargs):
        self.__clear_posts()
