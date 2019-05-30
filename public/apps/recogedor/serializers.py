#! /usr/bin/env python
#-*- encoding:utf-8 -*-

from rest_framework import serializers
from apps.recogedor import models as mdl


class EstadosSerializers(serializers.ModelSerializer):

    class Meta:
        model = mdl.Estados
        fields = '__all__'


class DepartamentosSerializers(serializers.ModelSerializer):

    estado = EstadosSerializers(
        read_only=True, required=False, many=False,)

    class Meta:
        model = mdl.Departamentos
        fields = '__all__'


class ProvinciasSerializers(serializers.ModelSerializer):

    estado = EstadosSerializers(
        read_only=True, required=False, many=False,)
    departamento = DepartamentosSerializers(
        read_only=True, required=False, many=False,
    )

    class Meta:
        model = mdl.Provincias
        fields = '__all__'


class DistritosSerializers(serializers.ModelSerializer):

    estado = EstadosSerializers(
        read_only=True, required=False, many=False,)
    departamento = DepartamentosSerializers(
        read_only=True, required=False, many=False,
    )
    provincia = ProvinciasSerializers(
        read_only=True, required=False, many=False,
    )

    class Meta:
        model = mdl.Distritos
        fields = '__all__'
