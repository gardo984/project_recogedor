from django.contrib import admin
from apps.recogedor import models as mdl

# Register your models here.


class AdminEstados(admin.ModelAdmin):
    list_display = [
        "id", "descripcion",
        "_format_fhregistro", "_format_fhmodificacion",
        "estado",
    ]
    list_display_links = ["id", "descripcion"]
    fields = [
        "id", "descripcion",
        "fhregistro", "fhmodificacion",
        "estado",
    ]
    readonly_fields = ["id", "fhregistro", "fhmodificacion"]
    search_fields = ["id", "descripcion", "estado"]
    ordering = ["-fhregistro"]
    list_per_page = 20
    empty_value_display = ""

    def _format_fhregistro(self, obj):
        wvalue = None
        if not obj.fhregistro is None:
            wvalue = obj.fhregistro.strftime("%Y-%m-%d %H:%M:%S")
        return wvalue
    _format_fhregistro.short_description = "Fecha Creacion"
    _format_fhregistro.admin_order_field = "-fhregistro"

    def _format_fhmodificacion(self, obj):
        wvalue = None
        if not obj.fhmodificacion is None:
            wvalue = obj.fhmodificacion.strftime("%Y-%m-%d %H:%M:%S")
        return wvalue
    _format_fhmodificacion.short_description = "Fecha Modificacion"
    _format_fhmodificacion.admin_order_field = "-fhmodificacion"


class AdminDistritos(admin.ModelAdmin):
    list_display = [
        "id", "descripcion", "provincia", "departamento",
        "_format_fhregistro", "_format_fhmodificacion",
        "estado",
    ]
    list_display_links = ["id", "descripcion"]
    fields = [
        "id", "descripcion",
        "provincia", "departamento",
        "fhregistro", "fhmodificacion",
        "estado",
    ]
    readonly_fields = ["id", "fhregistro", "fhmodificacion"]
    search_fields = [
        "id", "descripcion", "estado__descripcion",
        "provincia__descripcion", "departamento__descripcion",
    ]
    ordering = ["-fhregistro"]
    list_per_page = 20
    empty_value_display = ""

    def _format_fhregistro(self, obj):
        wvalue = None
        if not obj.fhregistro is None:
            wvalue = obj.fhregistro.strftime("%Y-%m-%d %H:%M:%S")
        return wvalue
    _format_fhregistro.short_description = "Fecha Creacion"
    _format_fhregistro.admin_order_field = "-fhregistro"

    def _format_fhmodificacion(self, obj):
        wvalue = None
        if not obj.fhmodificacion is None:
            wvalue = obj.fhmodificacion.strftime("%Y-%m-%d %H:%M:%S")
        return wvalue
    _format_fhmodificacion.short_description = "Fecha Modificacion"
    _format_fhmodificacion.admin_order_field = "-fhmodificacion"


class AdminPuntosAcopio(admin.ModelAdmin):
    list_display = [
        "id", "descripcion",
        "_format_fhregistro", "_format_fhmodificacion",
        "estado",
    ]
    list_display_links = ["id", "descripcion"]
    fields = [
        "id", "descripcion",
        "fhregistro", "fhmodificacion",
        "estado",
    ]
    readonly_fields = ["id", "fhregistro", "fhmodificacion"]
    search_fields = [
        "id", "descripcion", "estado__descripcion",
    ]
    ordering = ["-fhregistro"]
    list_per_page = 20
    empty_value_display = ""

    def _format_fhregistro(self, obj):
        wvalue = None
        if not obj.fhregistro is None:
            wvalue = obj.fhregistro.strftime("%Y-%m-%d %H:%M:%S")
        return wvalue
    _format_fhregistro.short_description = "Fecha Creacion"
    _format_fhregistro.admin_order_field = "-fhregistro"

    def _format_fhmodificacion(self, obj):
        wvalue = None
        if not obj.fhmodificacion is None:
            wvalue = obj.fhmodificacion.strftime("%Y-%m-%d %H:%M:%S")
        return wvalue
    _format_fhmodificacion.short_description = "Fecha Modificacion"
    _format_fhmodificacion.admin_order_field = "-fhmodificacion"


class AdminHorarios(admin.ModelAdmin):
    list_display = [
        "id", "descripcion", "hora_desde", "hora_hasta",
        "_format_fhregistro", "_format_fhmodificacion",
        "estado",
    ]
    list_display_links = ["id", "descripcion"]
    fields = [
        "id", "descripcion", "hora_desde", "hora_hasta",
        "fhregistro", "fhmodificacion",
        "estado",
    ]
    readonly_fields = ["id", "fhregistro", "fhmodificacion"]
    search_fields = [
        "id", "descripcion", "estado__descripcion",
    ]
    ordering = ["-fhregistro"]
    list_per_page = 20
    empty_value_display = ""

    def _format_fhregistro(self, obj):
        wvalue = None
        if not obj.fhregistro is None:
            wvalue = obj.fhregistro.strftime("%Y-%m-%d %H:%M:%S")
        return wvalue
    _format_fhregistro.short_description = "Fecha Creacion"
    _format_fhregistro.admin_order_field = "-fhregistro"

    def _format_fhmodificacion(self, obj):
        wvalue = None
        if not obj.fhmodificacion is None:
            wvalue = obj.fhmodificacion.strftime("%Y-%m-%d %H:%M:%S")
        return wvalue
    _format_fhmodificacion.short_description = "Fecha Modificacion"
    _format_fhmodificacion.admin_order_field = "-fhmodificacion"


class AdminTipoReclamo(admin.ModelAdmin):
    list_display = [
        "id", "descripcion",
        "_format_fhregistro", "_format_fhmodificacion",
        "estado",
    ]
    list_display_links = ["id", "descripcion"]
    fields = [
        "id", "descripcion",
        "fhregistro", "fhmodificacion",
        "estado",
    ]
    readonly_fields = ["id", "fhregistro", "fhmodificacion"]
    search_fields = [
        "id", "descripcion", "estado__descripcion",
    ]
    ordering = ["-fhregistro"]
    list_per_page = 20
    empty_value_display = ""

    def _format_fhregistro(self, obj):
        wvalue = None
        if not obj.fhregistro is None:
            wvalue = obj.fhregistro.strftime("%Y-%m-%d %H:%M:%S")
        return wvalue
    _format_fhregistro.short_description = "Fecha Creacion"
    _format_fhregistro.admin_order_field = "-fhregistro"

    def _format_fhmodificacion(self, obj):
        wvalue = None
        if not obj.fhmodificacion is None:
            wvalue = obj.fhmodificacion.strftime("%Y-%m-%d %H:%M:%S")
        return wvalue
    _format_fhmodificacion.short_description = "Fecha Modificacion"
    _format_fhmodificacion.admin_order_field = "-fhmodificacion"


class AdminAlertas(admin.ModelAdmin):
    list_display = [
        "id", "descripcion",
        "_format_fhregistro", "_format_fhmodificacion",
        "estado",
    ]
    list_display_links = ["id", "descripcion"]
    fields = [
        "id", "descripcion",
        "fhregistro", "fhmodificacion",
        "estado",
    ]
    readonly_fields = ["id", "fhregistro", "fhmodificacion"]
    search_fields = [
        "id", "descripcion", "estado__descripcion",
    ]
    ordering = ["-fhregistro"]
    list_per_page = 20
    empty_value_display = ""

    def _format_fhregistro(self, obj):
        wvalue = None
        if not obj.fhregistro is None:
            wvalue = obj.fhregistro.strftime("%Y-%m-%d %H:%M:%S")
        return wvalue
    _format_fhregistro.short_description = "Fecha Creacion"
    _format_fhregistro.admin_order_field = "-fhregistro"

    def _format_fhmodificacion(self, obj):
        wvalue = None
        if not obj.fhmodificacion is None:
            wvalue = obj.fhmodificacion.strftime("%Y-%m-%d %H:%M:%S")
        return wvalue
    _format_fhmodificacion.short_description = "Fecha Modificacion"
    _format_fhmodificacion.admin_order_field = "-fhmodificacion"

wmodels = [
    mdl.Estados,
    mdl.Distritos,
    mdl.PuntosAcopio,
    mdl.Horarios,
    mdl.TipoReclamo,
    mdl.Alertas,
]
winterfaces = [
    AdminEstados,
    AdminDistritos,
    AdminPuntosAcopio,
    AdminHorarios,
    AdminTipoReclamo,
    AdminAlertas,
]
for windex, witem in enumerate(wmodels):
    admin.site.register(wmodels[windex], winterfaces[windex])
