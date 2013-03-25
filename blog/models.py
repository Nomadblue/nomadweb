from django.db import models

from nomadblog.models import Post


class NomadPost(Post):
    summary = models.TextField()

    def __unicode__(self):
        return self.post_ptr.title

    def previous_post(self):
        posts = list(NomadPost.objects.order_by('pub_date'))
        pos = posts.index(self)
        if pos:  # pos is not 0
            return posts[pos-1].post_ptr.get_absolute_url()

    def next_post(self):
        posts = list(NomadPost.objects.order_by('pub_date'))
        pos = posts.index(self)
        if not pos == len(posts) - 1:  # pos is not 0
            return posts[pos+1].post_ptr.get_absolute_url()
