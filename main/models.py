from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Network(models.Model):
    """Модель поставщика"""
    NAME_CHOICES = (
        ('Factory', 'Завод'),
        ('Retail', 'Розничная сеть'),
        ('Entrepreneur', 'Индивидуальный предприниматель'),
    )

    name = models.CharField(max_length=100, choices=NAME_CHOICES, verbose_name='тип сети')
    email = models.EmailField()
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=100, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица/проспект')
    house_number = models.CharField(max_length=10, verbose_name='номер дома')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=100, verbose_name='название продукта')
    model = models.CharField(max_length=100, verbose_name='модель')
    release_date = models.DateField(verbose_name='дата релиза')
    supplier = models.ForeignKey(Network, on_delete=models.CASCADE, related_name='supplied_products',
                                 verbose_name='поставщик')
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='долг поставщику')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
