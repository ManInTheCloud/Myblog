from django.contrib import admin

from blog.models import Article

class ArticleAdmin(admin.ModelAdmin):
	list_display=('title','pub_date','category')
	search_fields=('title','category')
	date_hierarchy='pub_date'
	ordering=('-pub_date',)
	
admin.site.register(Article,ArticleAdmin)