from django.shortcuts import render

# Create your views here.
from .models import Member
from .utilites import get_tenant

def our_team(request):
    tenant = get_tenant(request)
    members = Member.objects.filter(tenant=tenant)
    return render(request, 'tenant/team.html', {tenant, members})