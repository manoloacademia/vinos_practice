from django.contrib import admin
from .models import Wine, Winery, Brand

# Superuser created manoloacademia: 1234*5678

admin.site.register(Wine)
admin.site.register(Winery)
admin.site.register(Brand)
