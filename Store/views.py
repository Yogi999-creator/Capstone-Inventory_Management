from django.shortcuts import render, HttpResponseRedirect
from .forms import ItemsRegistration
from .models import User
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
# Create your views here.

# This Class Will Add new Item and Show All Items.
class UserAddShowView(TemplateView):
    template_name = 'Store/addandshow.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = ItemsRegistration()
        item = User.objects.all()
        context = {'ite':item, 'form':fm}
        return context
    def post(self, request):
         fm = ItemsRegistration(request.POST)
         if fm.is_valid():
            ch = fm.cleaned_data['choose'] 
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ad = fm.cleaned_data['address']
            pr = fm.cleaned_data['products']
            qq = fm.cleaned_data['quantity']
            pk = fm.cleaned_data['packaging']
           
            reg = User(choose=ch, name=nm, email=em, address=ad , products=pr, quantity=qq, packaging=pk)
            reg.save()
         return HttpResponseRedirect('/')

# This Class Will Update/Edit.
class UserUpdateView(View):
    def get(self, request, id):
         pi = User.objects.get(pk=id)
         fm = ItemsRegistration(instance=pi)
         return render(request,'Store/update.html', {'form':fm})
    
    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = ItemsRegistration(request.POST, instance=pi)
        if fm.is_valid():
           fm.save()
        return HttpResponseRedirect('/')

# This Class will delete.
class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
