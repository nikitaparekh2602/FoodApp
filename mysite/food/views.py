from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
# from django.contrib.auth.models import User
# Create your views here.

def index(request):
    item_list = Item.objects.all()
    # template = loader.get_template('index.html')
    context = {
        'item_list': item_list,
    }
    # return HttpResponse(template.render(context,request))
    return render(request, 'food/index.html', context)

class IndecClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'

    # pagination and search item
    paginate_by = 3  # 3 items per page

    def get_queryset(self):
        query = self.request.GET.get('search')
        items = Item.objects.all()

        if query:
            items = items.filter(item_name__icontains=query)

        return items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        return context
    

def item(request):
    return HttpResponse("<h1>This is an Item Page</h1>")

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)
    # return HttpResponse("<h1>Details of item: %s</h1>" % item_id)

class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'


def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'food/item-form.html',{'form':form})

class CreateItem(CreateView):
    model = Item
    fields = ['item_name','item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)



def edit_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('index')
    context = {
        'form': form,
        'item': item,
    }
    return render(request, 'food/item-form.html',context)

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'food/item-delete.html', context)
    

# def food_list(request):
#     query = request.GET.get('search')
#     items = Item.objects.all()
#     if query:
#         items = items.filter(name__icontains=query)
#     paginator = Paginator(items, 3)  # 5 items per page
#     page = request.GET.get('page')
#     items = paginator.get_page(page)
#     return render(request, 'food/detail.html', {'items': items})
