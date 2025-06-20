import uuid
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager



class Organization(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gst_in = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True)
    template_id = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    module_id = models.CharField(max_length=100, blank=True)
    zipcode = models.CharField(max_length=20)
    industry = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[
        ('Pending', 'Pending'),
        ('Verified', 'Verified'),
        ('Suspended', 'Suspended'),
    ], default='Pending')
    parent_org = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='child_organizations'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        organization = extra_fields.pop('organization', None)
        if organization is None:
            raise ValueError('Users must have an organization')
        if not isinstance(organization, Organization):

            organization = Organization.objects.get(pk=organization)
        email = self.normalize_email(email)
        user = self.model(email=email, organization=organization, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('role', 'admin')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if 'organization' not in extra_fields:

            default_org = Organization.objects.first()
            extra_fields['organization'] = default_org
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=50)
    permissions = models.CharField(max_length=255, blank=True)
    organization = models.ForeignKey(
        Organization,
        null=True,
        on_delete=models.PROTECT,
        related_name='users'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role', 'organization']

    objects = UserManager()

    def __str__(self):
        return self.email


