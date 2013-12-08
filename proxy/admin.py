from django.contrib import admin
from proxy.models import Bucket, S3Object
# Register your models here.


class BucketAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'put_once', 'comment', 'last_updated')
    list_filter = ['owner']
    search_fields = ['name', 'comment']


class S3ObjectAdmin(admin.ModelAdmin):
    list_display = ('key', 'bucket', 'last_updated')
    list_filter = ['bucket']
    search_fields = ['key']

admin.site.register(Bucket, BucketAdmin)
admin.site.register(S3Object, S3ObjectAdmin)
