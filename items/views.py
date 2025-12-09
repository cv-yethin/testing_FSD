from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

@login_required
def item_list(request):
    items = Item.objects.filter(owner=request.user).order_by("-created_at")
    return render(request, "items/item_list.html", {"items": items})

@login_required
def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect("item_list")
    else:
        form = ItemForm()
    return render(request, "items/item_form.html", {"form": form})

@login_required
def item_edit(request, pk):
    item = get_object_or_404(Item, pk=pk, owner=request.user)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item_list")
    else:
        form = ItemForm(instance=item)
    return render(request, "items/item_form.html", {"form": form})

@login_required
def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk, owner=request.user)
    if request.method == "POST":
        item.delete()
        return redirect("item_list")
    return render(request, "items/item_confirm_delete.html", {"item": item})