# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

import logging


class ExternalMediaService:

    def __init__(self, ari):
        self._ari = ari

    def external_media(self, call_id, request):
        channel = self._ari.channels.get(channelId=call_id)
        return channel.externalMedia(**request)
