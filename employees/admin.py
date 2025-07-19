from django.contrib import admin
from .models import Employee

# Register your models here.


# **it is used to display our models in the django admin panel
# **admin panel help us to do basic CRUD(Create, Read, Update, and Delete)

# **after creating models and then migrating them
# **To see the models in admin panel, we need to register them in the admin.py file

# **admin.site.register(YourModelName)  Replace YourModelName with your actual model name

admin.site.register(Employee)


