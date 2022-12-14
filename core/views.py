from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect
from product.models import Product, Category
from .models import ContactForm, SocialMedia
from .forms import SignUpForm, Contact
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.db.models import Min, Max
from decimal import Decimal as D

def frontpage(request):
    products = Product.objects.all()
    paginator = Paginator(products, 8)
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
        'active_category': active_category,
        
        }
    return render(request, 'core/shop.html', context)


@csrf_exempt  
def price_filter(request): 

    price1 = D(request.GET.get('min_price', '')) 
    price2 = D(request.GET.get('max_price', ''))
    
    if price1 is None:
        my_products=Product.objects.all()
    if price2 is None:
        my_products=Product.objects.all()
        

    my_products = Product.objects.filter(price__range=(price1, price2))
   
    context = { "products":my_products}
    return render(request,"core/shop.html",context)
    


    



@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account Created!" )
            return redirect('/')
    else:
        form=SignUpForm()
    return render(request, 'core/signup.html', {'form':form})



@csrf_exempt
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

        messages.success(request, "Account Updated!" )
        return redirect('myaccount')
    return render(request, 'core/edit_myaccount.html')


@csrf_exempt
def contactForm(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, "Message Sent!")
            return redirect('frontpage')
    else:
        form = Contact()
        
        
       
      
    return render(request, 'core/contactForm.html', {'form':form} )
    

def socialmedia(request):
    obj = SocialMedia.objects.all()[0]
    context={'obj':obj}
    
    return render(request, 'core/footer.html',context)