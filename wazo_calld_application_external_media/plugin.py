# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from wazo_auth_client import Client as AuthClient

from .resources import ExternalMediaResource
from .services import ExternalMediaService


class Plugin(object):

    def load(self, dependencies):
        api = dependencies['api']
        config = dependencies['config']
        ari = dependencies['ari']

        service = ExternalMediaService(ari.client)

        api.add_resource(ExternalMediaResource, '/applications/<application_uuid>/calls/<call_id>/externalMedia', resource_class_args=[service])
