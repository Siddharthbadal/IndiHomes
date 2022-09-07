from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from product.models import Product, Category
from .forms import SignUpForm 
from django.core.paginator import Paginator


def frontpage(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)   
    context = {'page_obj':page_obj}
    return render(request, 'core/frontpage.html', context)



def shop(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    active_category = request.GET.get('category','')
    if active_category:
        products =products.filter(category__slug=active_category)

    query = request.GET.get('query','')
    if query:
        products =products.filter(Q(name__icontains=query)|Q(description__icontains=query))
        

    context= {
        'categories': categories,
        'products':products,
        'active_category': active_category
        }
    return render(request, 'core/shop.html', context)



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form=SignUpForm()
    return render(request, 'core/signup.html', {'form':form})

@login_required
def myaccount(request):
    return render(request, 'core/myaccount.html')


@login_required
def editmyaccount(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')

        user = request.user
        user.first_name=first_name
        user.last_name=last_name
        user.email=email
        user.save()
        return redirect('myaccount')
    return render(request, 'core/edit_myaccount.html')

