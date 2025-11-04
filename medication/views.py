from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Medication
from users.models import User  # only if you need user info

# ✅ List + Search
def index(request):
    query = request.GET.get('q')
    medications = Medication.objects.all().select_related('user').order_by('-created_at')

    if query:
        medications = medications.filter(
            Q(name__icontains=query) |
            Q(dosage__icontains=query) |
            Q(description__icontains=query) |
            Q(user__first_name__icontains=query) |
            Q(user__last_name__icontains=query)
        )

    return render(request, "medication/index.html", {"medications": medications})


# ✅ Create
def create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        dosage = request.POST.get("dosage")
        description = request.POST.get("description")
        user_id = request.POST.get("user")

        user = User.objects.get(id=user_id) if user_id else None

        Medication.objects.create(
            name=name, dosage=dosage, description=description, user=user
        )
        return redirect("medication_list")

    users = User.objects.all()
    return render(request, "medication/create.html", {"users": users})


# ✅ View
def view(request, medication_id):
    medication = get_object_or_404(Medication, id=medication_id)
    return render(request, "medication/view.html", {"medication": medication})


# ✅ Edit
def edit(request, medication_id):
    medication = get_object_or_404(Medication, id=medication_id)

    if request.method == "POST":
        medication.name = request.POST.get("name")
        medication.dosage = request.POST.get("dosage")
        medication.description = request.POST.get("description")

        user_id = request.POST.get("user")
        medication.user = User.objects.get(id=user_id) if user_id else None

        medication.save()
        return redirect("medication_list")

    users = User.objects.all()
    return render(request, "medication/edit.html", {"medication": medication, "users": users})


# ✅ Delete
def delete(request, medication_id):
    medication = get_object_or_404(Medication, id=medication_id)

    if request.method == "POST":
        medication.delete()
        return redirect("medication_list")

    return render(request, "medication/delete.html", {"medication": medication})
