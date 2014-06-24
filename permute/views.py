from permute.models import CoulumA, CoulumB, CoulumC, CoulmD, CoulumE
#from forms import DataImport
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render_to_response
import itertools

def upload(self, commit=False, *args, **kwargs):
        form_input = DataImport()
        #self.place = self.cleaned_data['place']
        file_csv = request.FILES['file_to_import']
        datafile = open(file_csv, 'rb')
        records = csv.reader(datafile)
        for line in records:
            self.dataa = line[1]
            form_input.save()
        datafile.close()



def render(request):
	a = CoulumA.objects.all()
	b = CoulumB.objects.all()
	c = CoulumC.objects.all()
	d = CoulmD.objects.all()
	e = CoulumE.objects.all()
	context = { 'a' : a, 'b' : b, 'c' : c, 'd' : d, 'e' : e}
	return render_to_response('render.html', context, context_instance=RequestContext(request))
    #return render_to_response(request, 'data.html', ctx)



def que(request):
	#from permute.models import AdBatch
    cola = request.POST.getlist('cola')
    colb = request.POST.getlist('colb')
    colc = request.POST.getlist('colc')
    cold = request.POST.getlist('cold')
    cole = request.POST.getlist('cole')
    
    mainlist = [cola, colb, colc, cold, cole]
    perlist = list(itertools.product(*mainlist))
    #print perlist
    from permute.models import Adbatch
    for i in perlist:
    	Adbatch.objects.create(abbatch_cola = i[0], abbatch_colb = i[1], abbatch_colc = i[2], abbatch_cold = i[3], abbatch_cole = i[4])
    	

    return HttpResponseRedirect('/test')
