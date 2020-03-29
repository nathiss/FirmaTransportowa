from django.core.management.base import BaseCommand, no_translations

# pylint: disable=import-error
from webapp.models import Post

class Command(BaseCommand):
    help = 'Populates the databse with example data.'

    def __clear_posts(self):
        # pylint: disable=no-member
        all = Post.objects.all()
        if len(all) == 0:
            self.stderr.write(self.style.WARNING('Post table has no entries.'))
        else:
            all.delete()
            self.stdout.write(self.style.SUCCESS('Deleted all entries in Post table.'))

    @no_translations
    def handle(self, *args, **kwargs):
        self.__clear_posts()
