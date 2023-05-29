from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from products.subscribe_form import SubscribeForm

# Create your views here.
def create_new_subscriber(request):
    if request.method == "POST":
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
    else:
        form = SubscribeForm()
    context = {
        "form": form,
    }
    return render(request, "details/subscribe.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        "product_object" : product,
    }
    return render(request, "details/individual_product.html", context)


def product_list(request):
    products = Product.objects.all()
    context = {
        "product_list": products
    }
    return render(request, "details/product_list.html", context)

def home_page(request):
    return render(request, "details/home_page.html")

def contact(request):
    return render(request, "details/contact_us.html")

def story(request):
    return render(request, "details/story.html")
