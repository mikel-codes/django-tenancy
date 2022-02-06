from django.db import models
from django.contrib.auth.models import User
# Create your models
class Tenant(models.Model):
    """Model definition for Tenant."""
    name = models.CharField(max_length=255)
    subdomain=models.CharField(max_length=255, unique=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Tenant."""

        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'


class TenantAwareMixin(models.Model):
    """Model definition for TenantAwareModel."""
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, blank=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for TenantAwareModel."""
        abstract=True

class Member(TenantAwareMixin):
    """Model definition for Member."""
    name = models.CharField(max_length=255, blank=True, null=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Member."""

        verbose_name = 'Member'
        verbose_name_plural = 'Members'


