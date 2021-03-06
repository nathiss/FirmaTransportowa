import datetime

from django.core.management.base import BaseCommand, no_translations

# pylint: disable=import-error
from webapp.models import Post

class Command(BaseCommand):
    help = 'Populates the databse with example data.'

    def __populate_posts(self):
        post = Post()
        post.title = 'Witaj na naszej stronie!'
        post.datetime = datetime.datetime(2004, 4, 27, 13, 45)
        post.content = """
        Witaj na naszej stronie! Jesteśmy firmą transportową, która zajmuje się transportem ludzi. <br />
        Cieszymy się, że chcesz korzystać z naszych usłów. Zobacz zakładkę <b>O nas</b> aby dowiedzieć się więcej.
        """
        post.save()
        self.stdout.write(self.style.SUCCESS('Successfuly added entries to Post table.'))

    @no_translations
    def handle(self, *args, **kwargs):
        self.__populate_posts()
