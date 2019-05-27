#! /usr/bin/env python
# -*- encoding: utf8 -*-

import re
import os
from datetime import datetime
import hashlib

import xlsxwriter as xls
# django settings info
from django.conf import settings


class Validators(object):
    """docstring for Validators"""

    def __init__(self, arg):
        super(Validators, self).__init__()
        self.arg = arg

    def isNumber(value):
        try:
            result = re.match("^([0-9]+)$", value)
            status = False if result is None else True
            return status
        except Exception as e:
            return False

    def isString(value):
        try:
            result = re.match("^([a-zA-Z]+)$", value)
            status = False if result is None else True
            return status
        except Exception as e:
            return False

    def isDate(wvalue, wformat):
        result = None
        status = True
        try:
            result = datetime.strptime(wvalue, wformat)
            if type(result) is datetime:
                status = True
            else:
                status = False
        except Exception as e:
            status = False
        return [result, status]

    def validateType(value, options=[]):
        try:
            if len(options) == 0:
                return False
            if type(value) in options:
                return True
        except Exception as e:
            return False

    def ifDirectoryExists(wpath):
        error = None
        try:
            if not os.path.exists(wpath):
                os.makedirs(wpath)
        except Exception as e:
            error = str(e)
        return error

    def removeKeys(wdata, wvalues=[]):
        new_result = dict(wdata)
        try:
            for x in wvalues:
                del new_result[x]
        except Exception as e:
            error = str(e)
            print(error)
        return new_result

    def getDatetimeHash():
        whash = None
        try:
            whash = datetime.now().strftime("%Y%m%d%H%M%S%f")
        except Exception as e:
            error = str(e)
            print(error)
        return whash

    def getMd5Hash(value, length=12):
        whash = None
        try:
            obj = hashlib.md5()
            obj.update(value.encode("utf8"))
            whash = obj.hexdigest()[-length:]
        except Exception as e:
            error = str(e)
            print(error)
        return whash

    def getPageParameters():
        return {
            "total": 0,
            "size": 10,
            "count": 21,
        }

    def getContentFile(wpath='', wencoding='utf8'):
        wcontent, werror = None, None
        try:
            if not os.path.exists(wpath):
                raise ValueError(str('path {} doesnt exists.'.format(wpath)))
            wfile = open(wpath, 'r', encoding=wencoding)
            wcontent = wfile.readlines()
            wfile.close()
        except Exception as e:
            werror = str(e)
        return [wcontent, werror]


class ExportToExcel(object):

    _excel_row = 0
    _excel_title = ''
    _excel_default_width = 0
    _headers = []
    _details = []
    _excel_wb = None
    _excel_ws = None
    _request = None
    _date_format = "%d/%m/%Y %H:%M:%S"

    def __init__(self, **kwargs):
        super(ExportToExcel, self).__init__()
        self._excel_row = kwargs.get("start_from") or 4
        self._excel_default_width = kwargs.get("default_width") or 12
        self._excel_title = kwargs.get("title") or ''
        self._request = kwargs.get("request") or None
        self._headers = kwargs.get("headers") or []
        self._details = kwargs.get("details") or []

    def generateFile(self):
        error = None
        data = {"filepath": ""}
        try:
            directory = settings.MEDIA_ROOT
            filename = 'invoice_report/xls_{}.xlsx'.format(
                Validators.getDatetimeHash())
            filepath = '{}/{}'.format(directory, filename)
            urlpath = self.get_request.build_absolute_uri('{}{}'.format(
                settings.MEDIA_URL,
                filename,
            ))
            data["filepath"] = urlpath
            self._excel_wb = xls.Workbook(filepath)
            self._excel_ws = self.get_wb.add_worksheet()
            self.write_title()
            self.write_headers()
            self.write_rows()
            self.get_wb.close()
        except Exception as e:
            error = str(e)
        return [data, error]

    def write_title(self):
        label_date = 'Fecha : {}'.format(
            datetime.now().strftime(self._date_format))
        self.get_ws.merge_range("A1:B1", label_date)
        formatTitle = self.get_wb.add_format({
            'bold': 1,
            'align': 'center',
        })
        self.get_ws.merge_range("C3:G3", self.get_excel_title, formatTitle)

    def write_headers(self):
        formatHeaders = self.get_wb.add_format({
            'bold': 1,
            'align': 'center',
            'bg_color': 'yellow',
            'border': 1,
        })
        for row_column, z in enumerate(self.get_headers):
            if z.get("bold"):
                self.get_ws.write(self._excel_row, row_column,
                                  z.get("value"), formatHeaders)
            else:
                self.get_ws.write(self._excel_row, row_column, z.get("value"))
            width = z.get("w") if z.get("w") else self.get_default_width
            self.get_ws.set_column(row_column, row_column, width)
            row_column += 1
        pass

    def write_rows(self):
        # write rows
        self._excel_row += 1
        for y in self.get_rows:
            for nposition, x in enumerate(self.get_headers):
                value = y.get(x.get("field"))
                if x.get("format_in") and not value is None:
                    value = datetime.strptime(
                        y.get(x.get("field")), x.get("format_in")) \
                        .strftime(x.get("format_out"))
                self.get_ws.write(self._excel_row, nposition, value)
            self._excel_row += 1

    @property
    def get_excel_title(self):
        return self._excel_title

    @property
    def get_request(self):
        return self._request

    @property
    def get_ws(self):
        return self._excel_ws

    @property
    def get_wb(self):
        return self._excel_wb

    @property
    def get_default_width(self):
        return self._excel_default_width

    @property
    def get_headers(self):
        return self._headers

    @property
    def get_rows(self):
        return self._details
