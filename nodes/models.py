from django.db import models
from accounts.models import MyUser
# from enterprise.models import Enterprise
from django.template.defaultfilters import slugify
from django.utils.timezone import now
from activities.models import Activity


class FeedManager(models.Manager):
    def get_queryset(self):
        return super(FeedManager, self).get_queryset().filter(parent=None, category='F')


class ArticleManager(models.Manager):
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(parent=None, category='A')


class Node(models.Model):
    myuser = models.ForeignKey(MyUser)
    node_type = (('F', 'Feed'), ('A', 'Article'), ('C', 'Comment'))
    category = models.CharField(max_length=1, choices=node_type, default='F')
    title = models.TextField(max_length=255, null=True, blank=True, db_index=True)
    post = models.TextField()
    slug = models.SlugField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True)
    comments = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    score = models.FloatField(default=0)

    objects = models.Manager()
    feed = FeedManager()
    article = ArticleManager()

    def __str__(self):
        if self.category is 'A':
            return self.title
        else:
            return self.post

    class Meta:
        ordering = ('-score', '-date')

    @staticmethod
    def get_feeds():
        feeds = Node.feed.all()
        return feeds

    # @staticmethod
    # def get_feeds_after(node):
    #     feeds = Node.feed.all(id__gt=node)
    #     return feeds

    @staticmethod
    def get_nodes():
        nodes = Node.objects.all()
        return nodes

    @staticmethod
    def get_articles():
        return Node.article.all()

    def save(self, *args, **kwargs):
        if not self.id:             # Newly created object, so set slug
            if not self.parent:
                if self.category is 'A':
                    self.slug = slugify(self.title).__str__()
                elif self.category is 'F':
                    self.slug = slugify(self.post[:250]).__str__()

        super(Node, self).save(*args, **kwargs)

    def get_summary(self):
        if self.title:
            return self.title
        elif self.post > 200:
            return self.post[:200]
        else:
            return self.post

    def create_tags(self, tags):
        try:
            tags = tags.strip()
            tag_list = tags.split(' ')
            for tag in tag_list:
                if tag:
                    t, created = Tag.objects.get_or_create(tag=tag.lower(), article=self)

        except Exception as e:
            return e

    def get_tags(self):
        return Tag.objects.filter(article=self)

    def get_comments(self):
        pieces = Node.objects.filter(parent=self).order_by('-date',)
        return pieces

    def calculate_likes(self):
        likes = Activity.objects.filter(activity='L', node=self.pk).count()
        self.likes = likes
        self.save()
        self.calculate_comments()
        self.set_rank()
        return likes

    # def get_likes(self):
    #     likes = Activity.objects.filter(activity_type=Activity.LIKE, node=self.pk)
    #     return likes

    def get_likers(self):
        likes = self.get_likes()
        likers = []
        for like in likes:
            likers.append(like.myuser)
        return likers

    def calculate_comments(self):
        comments = Node.objects.filter(parent=self).count()
        self.save()
        return comments

    def comment(self, myuser, post):
        feed_comment = Node(myuser=myuser, post=post, parent=self)
        feed_comment.save()
        self.comments = Node.objects.filter(parent=self).count()
        self.save()
        return feed_comment

    def create(self, myuser, post):
        feed = Node.objects.create(post=post, myuser=myuser)
        feed.save()
        return feed

    def set_rank(self):
        gravity = 1.2
        delta = now() - self.date
        node_age = delta.total_seconds()/3600
        popularity = 0.3*self.likes + 0.7*self.comments
        self.score = popularity/pow((node_age+2), gravity)
        self.save()

    # def linkfy_post(self):
    #     return bleach.linkify(escape(self.post))


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    article = models.ForeignKey(Node)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        unique_together = (('tag', 'article'),)
        index_together = [['tag', 'article'], ]

    def __str__(self):
        return self.tag

    @staticmethod
    def get_popular_tags():
        tags = Tag.objects.all()
        count = {}
        for tag in tags:
            if tag.article.category == 'A':
                if tag.tag in count:
                    count[tag.tag] = count[tag.tag] + 1
                else:
                    count[tag.tag] = 1
        sorted_count = sorted(count.items(), key=lambda t: t[1], reverse=True)
        return sorted_count[:10]



# Create your models here.
