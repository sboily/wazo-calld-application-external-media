# Copyright 2023 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0+

from marshmallow import (
    fields,
    Schema,
)
from marshmallow.validate import Length


class ExternalMediaSchema(Schema):
    app = fields.Str(validate=Length(min=1))
    external_host = fields.Str(validate=Length(min=1))
    format = fields.Str(validate=Length(min=1))

    class Meta:
        strict = True

external_media_schema = ExternalMediaSchema()
