```python
from django.test import TestCase
from .models import MyModel

class MyModelTestCase(TestCase):
    def setUp(self):
        MyModel.objects.create(name="Test1")
        MyModel.objects.create(name="Test2")

    def test_my_model_name(self):
        model1 = MyModel.objects.get(name="Test1")
        model2 = MyModel.objects.get(name="Test2")
        self.assertEqual(model1.name, 'Test1')
        self.assertEqual(model2.name, 'Test2')
```