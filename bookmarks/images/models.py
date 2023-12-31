from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class Image(models.Model):
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                            related_name='images_created',
                            on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)
    total_likes = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created']),
                   models.Index(fields=['-total_likes'])]
        
    def __str__(self):
        return self.title
    
    
    """
    We will override the save() method of the Image model
    to automatically generate the slug field based
    on the value of the title field. 
    Import the slugify() function and add a save() method to the Image model,
    """
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
        
        
    def get_absolute_url(self):
        # passing url with 'namespace:name'
        return reverse('images:detail', args=[self.id, self.slug]) 
        