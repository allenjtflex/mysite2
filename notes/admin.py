from django.contrib import admin

from .models import(   Category,
                        Department,
                        Reqlevel,
                        Treat,
                        Document,
                        TreatDoc,
                    )
# Register your models here.

admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Reqlevel)
admin.site.register(Treat)
admin.site.register(Document)
admin.site.register(TreatDoc)
