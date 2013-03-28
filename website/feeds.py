from django.contrib.syndication.views import Feed
from django.db.models import Q
from nomadblog.models import Post

class LatestEntries(Feed):
    title = "Nomadblue.com"
    link = "/"
    description = "Nomadblue.com: Latest entries"

    def items(self):
        return Post.objects.order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content


class LatestEntriesDjango(Feed):
    title = "Nomadblue.com"
    link = "/blog/django/"
    description = "Nomadblue.com: Latest entries in Django category"

    def items(self):
        return Post.objects.filter(category__name='django').order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

class LatestEntriesPython(Feed):
    title = "Nomadblue.com"
    link = "/blog/python/"
    description = "Nomadblue.com: Latest entries in Python category"

    def items(self):
        return Post.objects.filter(Q(category__name='django') | Q(category__name='python')).order_by('-pub_date')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content


