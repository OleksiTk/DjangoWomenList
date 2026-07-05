from django.db import models
from django.urls import reverse

# Create your models here.


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Women.Status.PUBLISHED)
    

class Women(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Draft'
        PUBLISHED = 1, 'Published'

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, blank=True, db_index=True, verbose_name="URL",default="")
    content = models.TextField(blank=True, verbose_name="Контент")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.IntegerField(choices=Status.choices, default=Status.DRAFT)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория",related_name='get_posts')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='get_posts', verbose_name="Теги")
    objects = models.Manager()  # Менеджер по умолчанию
    published = PublishManager()
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Известные женщины"
        verbose_name_plural = "Известные женщины"
        ordering = ['time_create', 'title']
        
        
        
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})
    
    
    
class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL",default="")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']
        
        
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.slug})
    
    
    
class TagPost(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Тег")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL",default="")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ['id']
        
        
    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_id': self.slug})