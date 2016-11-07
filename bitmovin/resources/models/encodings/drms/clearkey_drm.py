from .drm import DRM


class ClearKeyDRM(DRM):

    def __init__(self, key, kid, outputs=None, id_=None, custom_data=None):

        super().__init__(id_=id_, custom_data=custom_data, outputs=outputs)
        self.key = key
        self.kid = kid

    @classmethod
    def parse_from_json_object(cls, json_object):
        drm = super().parse_from_json_object(json_object=json_object)
        id_ = drm.id
        custom_data = drm.customData
        outputs = drm.outputs
        key = json_object['key']
        kid = json_object['kid']

        clearkey_drm = ClearKeyDRM(key=key, kid=kid, outputs=outputs, id_=id_, custom_data=custom_data)

        return clearkey_drm
