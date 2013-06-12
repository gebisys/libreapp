from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import datetime

class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)
	title = models.CharField(max_length=255)
	slug = models.CharField(max_length=255, blank=True, default='', unique=True)
	content = models.TextField()
	published = models.BooleanField(default=True)
	author = models.ForeignKey(User, related_name="posts")
	
	def save(self, *args, **kwargs):
		if not self.slug:
			date = datetime.date.today()
			self.slug = '%i/%i/%i/%s' % (
				date.year, date.month, date.day, slugify(self.title)
			)
		super(Post, self).save(*args, **kwargs)
	
	class Meta:
		ordering = ['-created_at']
		
	def get_absolute_url(self):
		return '/post/%s' % self.slug

	def get_preview_post(self):
		return self.content.split('<p><!--pagebreak--></p>')[0]
    