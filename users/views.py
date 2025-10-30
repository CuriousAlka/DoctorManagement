from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from .models import User
from .forms import UserForm


# ✅ User List with Search + Pagination
def user_list(request):
    query = request.GET.get('q', '')

    # Base queryset
    base_users = User.objects.all().order_by('-id')

    # 🔹 Filter first (for name + email)
    # if query:
    #     base_users = base_users.filter(
    #         Q(first_name__icontains=query) |
    #         Q(last_name__icontains=query) |
    #         Q(email__icontains=query)
    #     )

    # 🔹 Annotate full name (for combined search like "Eve Brown")
    users = base_users.annotate(
        full_name=Concat('first_name', Value(' '), 'last_name')
    )
    # print(users)
    # 🔹 Filter again to support full name match
    if query:
        users = users.filter(
            Q(full_name__icontains=query) | Q(email__icontains=query)
        )

    # 🔹 Pagination (10 per page)
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'users/list.html', {
        'users': page_obj,
        'query': query,
        'page_obj': page_obj
    })


# ✅ Create User
def user_create(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Add User'})


# ✅ Update User
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form, 'title': 'Edit User'})


# ✅ Delete User
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST":
        user.delete()
        return redirect('user_list')
    return render(request, 'users/confirm_delete.html', {'user': user})


# ✅ User Detail
def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'users/user_detail.html', {'user': user})
