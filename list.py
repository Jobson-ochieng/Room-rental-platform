from django.contrib.auth.models import User
for s in User.objects.filter(is_superuser=True):
 print(s.username,s.email)
