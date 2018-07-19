from django.shortcuts import render, get_object_or_404
from .forms import ClientForm
from .models import ClientsDatabase
from django.http import HttpResponseRedirect
from  .models import ClientsDatabase
from django.db.models import fields
# Create your views here.



def products_calculator(request):
    ist_clients = ClientsDatabase.objects

    return render(request, 'agent_aid/productscalculator.html',{'list_clients' : ist_clients})



def clients_entry (request):
    st_clients = ClientsDatabase.objects

    if request.method == 'POST':
        form = ClientForm(request.POST,request.FILES)
        save_form = form.save(commit=False)
        save_form.save()
        success = '<h1 style="text-align: center; color: green">success</h1> <br/> <a style="text-align: center; color: green"href="http://127.0.0.1:8000/agentaid/clientsentry/"> back</a>'
        return HttpResponseRedirect('', success)

    else:
        form = ClientForm()



    return render(request,'agent_aid/clientsentry.html', {'form': form}, {'list_clients' : st_clients})







def clients_id(request, client_id):

    client_info = get_object_or_404(ClientsDatabase, pk=client_id)
    return render(request, 'agent_aid/clientinfo.html', {'client_info': client_info})
