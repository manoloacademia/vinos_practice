from django.contrib import admin
from models import Wine, Cellar, Brand

# Superuser created manoloacademia: 1234*5678

admin.site.register(Wine)
admin.site.register(Cellar)
admin.site.register(Brand)
