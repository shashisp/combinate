import csv
from django import forms
from permute.models import CoulumA

class Dataimport(forms.ModelForm):
	file = forms.FileField()
    cola = forms.ModelChoiceField(queryset=CoulumA.objects.all()) 
	class Meta:
		model = CoulumA
		fields = ("file_to_import", "dataa")

	def save(self, commit=False, *args, **kwargs):
		form_input = Dataimport()
		self.place = self.cleaned_data['dataa']
		file_csv = request.FILES['file_to_import']
		datafile = open(file_csv, 'rb')
		records = csv.reader(datafile)
		for line in records:
			self.dataa = line[1]
		datafile.close()
