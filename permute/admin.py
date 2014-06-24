from permute.models import CoulumA, CoulumB, CoulumC,CoulmD, CoulumE, Adbatch
#from permute.forms import DataImport
from django.contrib import admin


class DataAdmin(admin.ModelAdmin):
	#list_display = ("dataa")
	#form = DataImport
	pass

admin.site.register(CoulumA, DataAdmin)


class DatabAdmin(admin.ModelAdmin):

	pass
admin.site.register(CoulumB, DatabAdmin)


class DatacAdmin(admin.ModelAdmin):
	pass
admin.site.register(CoulumC, DatacAdmin)


class DatadAdmin(admin.ModelAdmin):
	pass
admin.site.register(CoulmD, DatacAdmin)


class DataeAdmin(admin.ModelAdmin):
	pass

admin.site.register(CoulumE, DataeAdmin)

class AdbatchAdmin(admin.ModelAdmin):
	pass
admin.site.register(Adbatch, AdbatchAdmin)