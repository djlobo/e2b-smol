```python
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Extend the base User model to add additional fields if needed
    pass
```