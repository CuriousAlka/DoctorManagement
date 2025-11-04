from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from .models import User
from .forms import UserForm


# ✅ User List with Search + Pagination
def user_list(request):
    query = request.GET.get('q', '')

    # Base queryset
    users = User.objects.all().order_by('-id')

    # 🔹 Search filter (by name, email, mobile, membership ID)
    if query:
        users = users.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(mobile__icontains=query) |
            Q(membership_id__icontains=query)
        )

    # 🔹 Pagination (10 users per page)
    paginator = Paginator(users, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'users/list.html', {
        'users': page_obj,
        'query': query
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
    return render(request, 'users/user_form.html', {
        'form': form,
        'title': 'Add User'
    })


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
    return render(request, 'users/user_form.html', {
        'form': form,
        'title': 'Edit User'
    })


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
