from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from core.constants import (
    CATEGORY_CHOICES, STATUS_CHOICES, CREATIVE_UNIQUE,
    DEFAULT_BLOG_IMAGE, STATUS_DRAFT, CONFIRMATION_CHOICES,
    CONFIRMATION_WAIT
)


class Post(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField('slug', max_length=255,
                            unique=True, null=True, blank=True,
                            help_text=(
                                'If blank, the slug will be generated automatically '
                                'from the given title.'
                            )
                            )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=40, default=CREATIVE_UNIQUE)
    content = models.TextField(max_length=100000)
    created_ad = models.DateTimeField(auto_now_add=True, editable=False)
    updated_ad = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=40, default=STATUS_DRAFT)
    image = models.ImageField(default=DEFAULT_BLOG_IMAGE)
    tag = models.ManyToManyField('Tag', blank=True)
    confirmation = models.CharField(choices=CONFIRMATION_CHOICES, max_length=40, default=CONFIRMATION_WAIT)
    likes = models.ManyToManyField(User, through='Like', related_name='liked_posts')

    class Meta:
        ordering = ("-updated_ad",)

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super(Post, self).save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Comment(models.Model):
    content = models.TextField(max_length=3000)
    created_ad = models.DateTimeField(auto_now_add=True, editable=False)
    updated_ad = models.DateTimeField(auto_now=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment_author")
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='posts_comment')

    def __str__(self):
        return f'{self.author.username} - {self.post.title}'

    class Meta:
        ordering = ("-updated_ad",)


class Support(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_support")
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=3000)
    created_ad = models.DateTimeField(auto_now_add=True, editable=False)
    updated_ad = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.user.username} - {self.subject}'


class ContactInfo(models.Model):
    phone = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    list = (('active', 'Active'), ('deactive', 'Deactive'))
    status = models.CharField(choices=list, max_length=100, default="deactive")

    def __str__(self):
        return f'Contact information - {self.address} - {self.status}'

    class Meta:
        verbose_name = 'ContactInfo'
        verbose_name_plural = 'ContactInfo'


class AboutUs(models.Model):
    header_main = models.CharField(max_length=300)
    text_main = models.TextField(max_length=3000)
    header2 = models.CharField(max_length=300)
    text_2 = models.TextField(max_length=3000)
    header3 = models.CharField(max_length=300)
    text_3 = models.TextField(max_length=3000)
    header4 = models.CharField(max_length=300)
    text_4 = models.TextField(max_length=3000)
    header5 = models.CharField(max_length=300)
    text_5 = models.TextField(max_length=3000)
    header6 = models.CharField(max_length=300)
    text_6 = models.TextField(max_length=3000)
    header7 = models.CharField(max_length=300)
    text_7 = models.TextField(max_length=3000)
    header8 = models.CharField(max_length=300)
    text_8 = models.TextField(max_length=3000)
    header9 = models.CharField(max_length=300)
    text_9 = models.TextField(max_length=3000)
    header10 = models.CharField(max_length=300)
    text_10 = models.TextField(max_length=3000)
    list = (('active', 'Active'), ('deactive', 'Deactive'))
    status = models.CharField(choices=list, max_length=100, default="deactive")

    def __str__(self):
        return f'About us - {self.status}'

    class Meta:
        verbose_name = 'AboutUs'
        verbose_name_plural = 'AboutUs'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
