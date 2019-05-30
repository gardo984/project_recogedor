from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import (
    render, get_object_or_404,
)
from django.http import (
    JsonResponse,
)
from apps.recogedor import models as mdl
from apps.recogedor import serializers as srlz

# Create your views here.

defaultResponse = {
    "ok": 1,
    "result": {},
    "status": 200,
}

# without rest framework


def get_regions(request):
    wresponse = defaultResponse.copy()
    MAX_OBJECTS = 20
    lst_regions = mdl.Departamentos.objects.all()[:MAX_OBJECTS]
    lst_fields = ["id", "descripcion", ]
    wresponse["result"] = list(lst_regions.values(*lst_fields))
    return JsonResponse(wresponse, status=wresponse.get("status"))


def get_region(request, **kwargs):
    print("entra")
    wresponse = defaultResponse.copy()
    objprovince = get_object_or_404(
        mdl.Departamentos, pk=kwargs.get("pk"),
    )
    wresponse["result"] = {
        "id": objprovince.id,
        "descripcion": objprovince.descripcion,
        "created_date": objprovince.fhregistro,
    }
    return JsonResponse(wresponse, status=wresponse.get("status"))

# with rest framework


class GetRegions(APIView):

    def get(self, response):
        wresponse = defaultResponse.copy()
        MAX_OBJECTS = 20
        items = mdl.Departamentos.objects.all()[:MAX_OBJECTS]
        wresponse["result"] = srlz.DepartamentosSerializers(
            items, many=True).data
        return Response(wresponse, status=wresponse.get("status"))


class GetRegion(APIView):

    def get(self, response, **kwargs):
        wresponse = defaultResponse.copy()
        item = get_object_or_404(mdl.Departamentos, pk=kwargs.get("pk"))
        wresponse["result"] = srlz.DepartamentosSerializers(
            item, many=False).data
        return Response(wresponse, status=wresponse.get("status"))

# with rest framework generics


class RegionList(generics.ListCreateAPIView):
    queryset = mdl.Departamentos.objects.all()
    serializer_class = srlz.DepartamentosSerializers


class RegionItem(generics.RetrieveDestroyAPIView):
    queryset = mdl.Departamentos.objects.all()
    serializer_class = srlz.DepartamentosSerializers
