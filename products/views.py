
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404, JsonResponse
from django.forms.utils import ErrorList
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import urllib
import requests
from .models import Product
from .forms import ProductCreate


def home(request):
    return render(request ,'products/home.html')


@login_required
def AddProduct(request):
    if request.user.is_company:
        if request.method=="POST":
            if equest.POST['title'] and request.POST['description'] and  request.FILES['image']and  request.FILES['cost']:
                form=ProductCreate()
                new_product=Product
                new_product.title=request.POST['title']
                new_product.description=request.POST['description']
                new_product.image=request.FILES['image']
                new_product.cost=request.POST['cost']
                new_product.user=request.user
                product.pub_date=timezone.datetime.now()
                new_product.save()
            else:
                return render(request, 'products/create.html' ,{'error':'All fields are required to be filled','form': form})
        else:
            return render(request, 'products/create.html')


@login_required
def upvote(request, product_id):
	if request.method=="POST":
		product=get_object_or_404(Product, pk=product_id)
		product.votes_total+=1
		product.save()
		return redirect('/products/'+str(product.id))


class DetailProduct(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'


@login_required
class DeleteProduct(LoginRequiredMixin, generic.DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        product = super(DeleteProduct, self).get_object()
        if request.user.is_company:
            raise Http404
        return video
