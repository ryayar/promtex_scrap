from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User


class ScrapProduct(models.Model):
    query_id = models.IntegerField()
    query_date = models.DateTimeField(default=datetime.now())
    product_query_name = models.CharField(max_length=200)
    product_scrap_name = models.CharField(max_length=200)
    product_link = models.CharField(max_length=200)
    product_link_img = models.CharField(max_length=200)
    product_price = models.CharField(max_length=200)
    product_country = models.CharField(max_length=200)
    product_quality = models.CharField(max_length=200)
    user_name = models.CharField(max_length=70)
    product_platform = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.product_platform} — {self.product_query_name} — {self.product_price}'


#
# async def acreate_person():
#     person = await Person.objects.acreate(name="Tim", age=26)
#     print(person.name)
# # запускаем асинхронную функцию acreate_person
# asyncio.run(acreate_person())
#
# tom = Person(name="Tom", age=23)
# tom.save()
#
# people = Person.objects.bulk_create([
#     Person(name="Kate", age=24),
#     Person(name="Ann", age=21),
# ])
#
# for person in people:
#     print(f"{person.id}. {person.name}")
#
# tom = Person.objects.get(name="Tom")
# bob = Person.objects.get(age=23)

# people = Person.objects.all()[5:10]
# for person in people:
#     print(f"{person.id}.{person.name} - {person.age}")
