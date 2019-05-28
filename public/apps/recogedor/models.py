from django.db import models
from apps.common.models import CommonStructure
from django.utils import timezone

# Create your models here.


class Estados(CommonStructure):
    descripcion = models.CharField(max_length=200, null=False, blank=False,)
    estado = models.IntegerField(null=False, default=1, blank=False)
    username = None
    username_modif = None

    class Meta:
        verbose_name = "Estados"
        get_latest_by = ["fhregistro", ]
        ordering = ["fhregistro", ]
        indexes = [
            models.Index(fields=['descripcion'],),
        ]

    def __str__(self):
        return self.descripcion

    def save(self, *args, **kwargs):
        if not self.id is None:
            self.fhmodificacion = datetime.now()
        super().save(*args, **kwargs)

    @property
    def username(self):
        raise AttributeError("'Manager' object has no attribute 'username'")

    @property
    def username_modif(self):
        raise AttributeError(
            "'Manager' object has no attribute 'username_modif'")


class Departamentos(CommonStructure):
    descripcion = models.CharField(max_length=200,
                                   default=None, null=False, blank=False,)
    estado = models.ForeignKey(
        'recogedor.Estados', on_delete=models.SET_NULL, null=True,)

    class Meta:
        verbose_name = "Departamentos"
        get_latest_by = ["-fhregistro", ]
        ordering = ["-fhregistro", ]
        indexes = [
            models.Index(fields=['descripcion'],),
            models.Index(fields=['fregistro'],),
            models.Index(fields=['fhregistro'],),
            models.Index(fields=['fhmodificacion'],),
        ]

    def __str__(self):
        return self.descripcion


class Provincias(CommonStructure):
    descripcion = models.CharField(max_length=200,
                                   default=None, null=False, blank=False,)
    estado = models.ForeignKey(
        'recogedor.Estados', on_delete=models.SET_NULL, null=True,)
    departamento = models.ForeignKey(
        'recogedor.Departamentos', on_delete=models.SET_NULL, null=True,)

    class Meta:
        verbose_name = "Provincias"
        get_latest_by = ["-fhregistro", ]
        ordering = ["-fhregistro", ]
        indexes = [
            models.Index(fields=['descripcion'],),
            models.Index(fields=['fregistro'],),
            models.Index(fields=['fhregistro'],),
            models.Index(fields=['fhmodificacion'],),
        ]

    def __str__(self):
        return self.descripcion


class Distritos(CommonStructure):
    descripcion = models.CharField(max_length=200,
                                   default=None, null=False, blank=False,)
    ubigeo = models.CharField(max_length=25,
                              default=None, null=True, blank=True,)
    latitud = models.CharField(max_length=200,
                               default=None, null=False, blank=False,)
    longitud = models.CharField(max_length=200,
                                default=None, null=False, blank=False,)
    estado = models.ForeignKey(
        'recogedor.Estados', on_delete=models.SET_NULL, null=True,)
    provincia = models.ForeignKey(
        'recogedor.Provincias', on_delete=models.SET_NULL, null=True,)
    departamento = models.ForeignKey(
        'recogedor.Departamentos', on_delete=models.SET_NULL, null=True,)

    class Meta:
        verbose_name = "Distritos"
        get_latest_by = ["-fhregistro", ]
        ordering = ["-fhregistro", ]
        indexes = [
            models.Index(fields=['descripcion'],),
            models.Index(fields=['fregistro'],),
            models.Index(fields=['fhregistro'],),
            models.Index(fields=['fhmodificacion'],),
            models.Index(fields=['ubigeo'],),
            # models.Index(fields=['provincia'],),
            # models.Index(fields=['departamento'],),
        ]

    def __str__(self):
        return self.descripcion


class PuntosAcopio(CommonStructure):
    descripcion = models.CharField(max_length=200,
                                   default=None, null=False, blank=False,)
    estado = models.ForeignKey(
        'recogedor.Estados', on_delete=models.SET_NULL, null=True,)
    horarios = models.ManyToManyField(
        'recogedor.Horarios',
        verbose_name=('Horarios por Punto de Acopio'),
        blank=True,
        help_text=('Horarios especificos por P.Acopio.'),
    )

    class Meta:
        verbose_name = "Puntos Acopio"
        get_latest_by = ["-fhregistro", ]
        ordering = ["-fhregistro", ]
        indexes = [
            models.Index(fields=['descripcion'],),
            models.Index(fields=['fregistro'],),
            models.Index(fields=['fhregistro'],),
            models.Index(fields=['fhmodificacion'],),
        ]

    def __str__(self):
        return self.descripcion


class Horarios(CommonStructure):
    descripcion = models.CharField(max_length=200,
                                   default=None, null=False, blank=False,)
    hora_desde = models.TimeField(null=False, default=timezone.now)
    hora_hasta = models.TimeField(null=False, default=timezone.now)
    estado = models.ForeignKey(
        'recogedor.Estados', on_delete=models.SET_NULL, null=True,)

    class Meta:
        verbose_name = "Horarios"
        get_latest_by = ["-fhregistro", ]
        ordering = ["-fhregistro", ]
        indexes = [
            models.Index(fields=['descripcion'],),
            models.Index(fields=['fregistro'],),
            models.Index(fields=['fhregistro'],),
            models.Index(fields=['fhmodificacion'],),
            models.Index(fields=['hora_desde'],),
            models.Index(fields=['hora_hasta'],),
        ]


class TipoReclamo(CommonStructure):
    descripcion = models.CharField(max_length=200,
                                   default=None, null=False, blank=False,)
    estado = models.ForeignKey(
        'recogedor.Estados', on_delete=models.SET_NULL, null=True,)

    class Meta:
        verbose_name = "Tipo Reclamo"
        get_latest_by = ["-fhregistro", ]
        ordering = ["-fhregistro", ]
        indexes = [
            models.Index(fields=['descripcion'],),
            models.Index(fields=['fregistro'],),
            models.Index(fields=['fhregistro'],),
            models.Index(fields=['fhmodificacion'],),
        ]

    def __str__(self):
        return self.descripcion


class Alertas(CommonStructure):
    descripcion = models.CharField(max_length=200,
                                   default=None, null=False, blank=False,)
    estado = models.ForeignKey(
        'recogedor.Estados', on_delete=models.SET_NULL, null=True,)

    class Meta:
        verbose_name = "Alertas"
        get_latest_by = ["-fhregistro", ]
        ordering = ["-fhregistro", ]
        indexes = [
            models.Index(fields=['descripcion'],),
            models.Index(fields=['fregistro'],),
            models.Index(fields=['fhregistro'],),
            models.Index(fields=['fhmodificacion'],),
        ]

    def __str__(self):
        return self.descripcion
