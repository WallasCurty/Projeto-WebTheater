from django.contrib import admin

from videos.models import Categoria, Video

# Register your models here.
admin.site.urls(Categoria)
admin.site.urls(Video)

#usuario e e-mail: admin@user.com / senha: q1w2e3r4
