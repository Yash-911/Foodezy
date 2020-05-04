from django.contrib import admin
from .models import Cart
from .models import Checkout

admin.site.register(Cart)
admin.site.register(Checkout)