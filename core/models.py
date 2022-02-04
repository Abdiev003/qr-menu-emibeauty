from django.db import models


class Service(models.Model):
    # information's
    name = models.CharField(verbose_name='Xidmet adı', max_length=100,
                            db_index=True, help_text='Xidmetin adını daxil edin')

    # moderation's
    is_active = models.BooleanField(
        verbose_name='Aktiv', default=True, help_text='Xidmetin aktiv olmasını seçin')
    created_at = models.DateTimeField(
        verbose_name='Yaradılma tarixi', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Yenilənmə tarixi', auto_now=True)

    class Meta:
        verbose_name = 'Xidmət'
        verbose_name_plural = 'Xidmətlər'
        ordering = ['created_at']

    def __str__(self) -> str:
        return self.name


class ServiceItem(models.Model):
    # relation's
    service = models.ForeignKey(Service, verbose_name='Xidmət',
                                on_delete=models.CASCADE, related_name='service_items')

    # information's
    name = models.CharField(verbose_name='Alt xidmet adı',
                            max_length=100, help_text='Alt xidmetin adını daxil edin')

    # moderation's
    is_active = models.BooleanField(
        verbose_name='Aktiv', default=True, help_text='Xidmetin aktiv olmasını seçin')
    created_at = models.DateTimeField(
        verbose_name='Yaradılma tarixi', auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name='Yenilənmə tarixi', auto_now=True)

    class Meta:
        verbose_name = 'Alt Xidmət'
        verbose_name_plural = 'Alt Xidmətlər'
        ordering = ['created_at']

    def __str__(self) -> str:
        return self.name
