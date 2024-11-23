from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Organization, CustomUser, Role
from .forms import OrganizationForm, CustomUserForm

@login_required
def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organizations/list.html', {'organizations': organizations})


@login_required
def organization_create(request):
    if request.method == "POST":
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organization_list')
    else:
        form = OrganizationForm()
    return render(request, 'organizations/form.html', {'form': form})


@login_required
def organization_edit(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    if request.method == "POST":
        form = OrganizationForm(request.POST, instance=organization)
        if form.is_valid():
            form.save()
            return redirect('organization_list')
    else:
        form = OrganizationForm(instance=organization)
    return render(request, 'organizations/form.html', {'form': form})

@login_required
def organization_delete(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    organization.delete()
    return redirect('organization_list')

@login_required
def user_list(request):
    users = CustomUser.objects.filter(organization=request.user.organization)
    return render(request, 'users/list.html', {'users': users})


@login_required
def user_create(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.organization = request.user.organization
            user.save()
            form.save_m2m()
            return redirect('user_list')
    else:
        form = CustomUserForm()
    return render(request, 'users/form.html', {'form': form})


@login_required
def assign_role(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id, organization=request.user.organization)
    if request.method == "POST":
        roles = request.POST.getlist('roles')
        user.roles.set(Role.objects.filter(id__in=roles))
        return redirect('user_list')
    all_roles = Role.objects.all()
    return render(request, 'users/assign_role.html', {'user': user, 'roles': all_roles})

def user_page(request, user_id):
    # Retrieve the user object by ID
    user = get_object_or_404(CustomUser, id=user_id)
    # Render a template with the user object
    return render(request, 'users/user_page.html', {'user': user})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id, organization=request.user.organization)

    # Check if the current user is allowed to delete the user
    if request.user == user:
        # Prevent self-deletion
        return redirect('user_list')

    user.delete()
    return redirect('user_list')