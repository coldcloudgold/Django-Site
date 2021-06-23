from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from Posts.models import Post


class LatestPostsFeed(Feed):
    title = "Pied Piper - сжимаем сильнее всяких шакалов"
    link = "/"
    description = "Лучшая соцсеть века - Pied Piper"

    def items(self):  
        return Post.objects.filter(is_pub=True)[:10]  

    def item_title(self, item):  
        return truncatewords(item.title, 10)

    def item_description(self, item):  
        return truncatewords(item.text, 25)
    
    def item_link(self, item):
        return reverse('post', kwargs={"username": item.author, "pk": item.pk})
