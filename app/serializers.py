from marshmallow import Schema, fields


class UploadedFileSchema(Schema):
    id = fields.Int(dump_only=True)
    filename = fields.String()
    columns = fields.List(fields.String())
