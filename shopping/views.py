from django.shortcuts import render, redirect
from .models import Item

def shopping_list(request):
    items = Item.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")

        Item.objects.create(
            name=name,
            quantity=quantity
        )
        return redirect("shopping_list")

    return render(request, "shopping/list.html", {"items": items})


def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect("shopping_list")


def toggle_purchased(request, item_id):
    item = Item.objects.get(id=item_id)
    item.purchased = not item.purchased
    item.save()
    return redirect("shopping_list")
