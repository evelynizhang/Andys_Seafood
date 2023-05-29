from django.urls import path
from products.views import show_product, product_list, home_page, contact, story, create_new_subscriber

urlpatterns = [
    path("products/<int:id>", show_product, name="show_individual_product"), #name is the name of the html
    path("products/", product_list, name="list_of_products"),
    path("home/", home_page, name="home_page"),
    path("contact/", contact, name="contact"),
    path("story/", story, name="story"),
    path("subscribe/", create_new_subscriber, name="create_new_subscriber")
]
