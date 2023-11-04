from django.core.management.base import BaseCommand
from blog.models import Post

class Command(BaseCommand):
    help = 'Create a new blog post'

    def handle(self, *args, **kwargs):
        title = "How To Make Money"
        body = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatum saepe aliquid voluptatibus voluptas nam dolorum modi minima unde?"
        for i in range(15):
            slug="how-to-make-money-%s" % i
            Post.objects.create(title=title, body=body, slug=slug)
            self.stdout.write(self.style.SUCCESS('Successfully created a blog post'))