from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
	title=models.CharField(u"Blog title",max_length=100)
	category=models.CharField(u"Blog tag",max_length=50,blank=True)
	pub_date=models.DateTimeField("Publish date",auto_now_add=True,editable=True)
	content=models.TextField(blank=True,null=True)
	
	def __str__(self):
		return self.title
		
	class Meta:
		ordering=['-pub_date']
		verbose_name='Article'
		verbose_name_plural='Article'
