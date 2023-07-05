```python
from django.shortcuts import render
from .models import DatabaseModel

# Create your views here.

def list_records(request):
    records = DatabaseModel.objects.all()
    return render(request, 'database/list.html', {'records': records})

def detail_record(request, id):
    record = DatabaseModel.objects.get(id=id)
    return render(request, 'database/detail.html', {'record': record})
```