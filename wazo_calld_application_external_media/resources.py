# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+


from flask import request
from flask_restful import Resource

from wazo_calld.auth import required_acl
from wazo_calld.http import AuthResource

from .schema import external_media_schema


class ExternalMediaResource(AuthResource):

    def __init__(self, service):
        self._service = service

    @required_acl('calld.applications.{application_uuid}.calls.{call_id}.read')
    def post(self, application_uuid, call_id):
        request_body = external_media_schema.load(request.get_json(force=True))
        result = self._service.external_media(call_id, request_body)

        return result, 204
