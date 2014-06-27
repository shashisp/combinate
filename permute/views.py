from permute.models import CoulumA, CoulumB, CoulumC, CoulmD, CoulumE,Adbatch
#from forms import DataImport
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
import itertools,csv
'''
def upload(self, commit=False, *args, **kwargs):
        form_input = DataImport()
        #self.place = self.cleaned_data['place']
        file_csv = request.FILES['file_to_import']
        datafile = open(file_csv, 'rb')
        records = csv.reader(datafile)
        for line in records:
            self.dataa = line[1]
            form_input.save()
        datafile.close()'''



def render(request):
	a = CoulumA.objects.all()
	b = CoulumB.objects.all()
	c = CoulumC.objects.all()
	d = CoulmD.objects.all()
	e = CoulumE.objects.all()
	ad_id = Adbatch.objects.all()
	context = { 'a' : a, 'b' : b, 'c' : c, 'd' : d, 'e' : e,'ad_id' : ad_id}
	return render_to_response('render.html', context, context_instance=RequestContext(request))
   

_adbatch_count = 1

def que(request):
	
    cola = request.POST.getlist('cola')
    colb = request.POST.getlist('colb')
    colc = request.POST.getlist('colc')
    cold = request.POST.getlist('cold')
    cole = request.POST.getlist('cole')
    global _adbatch_count
    
    mainlist = [cola, colb, colc, cold, cole]
    perlist = list(itertools.product(*mainlist))
    from permute.models import Adbatch
    for i in perlist:
    	Adbatch.objects.create(adbatch_id =_adbatch_count,abbatch_cola = i[0], abbatch_colb = i[1], abbatch_colc = i[2], abbatch_cold = i[3], abbatch_cole = i[4])

    _adbatch_count+=1
    return HttpResponseRedirect('/render')


def export(request):
	response = HttpResponse(mimetype = 'text/csv')
	response['Content-Dispositon'] = 'attachment; filename= "adbatches.csv"'
	writer = csv.writer(response)
	adbatches = Adbatch.objects.filter()
	for adbatch in adbatches:
			writer.writerow([adbatch.abbatch_cola, adbatch.abbatch_colb, adbatch.abbatch_colc, adbatch.abbatch_cold, adbatch.abbatch_cole])

	return response
	