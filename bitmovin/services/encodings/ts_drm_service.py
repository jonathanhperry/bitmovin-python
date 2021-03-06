from .drm_service import DRMService
from .fairplay_drm_service import FairPlayDRM
from .aes_drm_service import AESDRM


class TSDRMService(DRMService):

    MUXING_TYPE_URL = 'ts'

    def __init__(self, http_client):
        super().__init__(http_client=http_client)
        self.FairPlay = FairPlayDRM(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
        self.AES = AESDRM(http_client=http_client, muxing_type_url=self.MUXING_TYPE_URL)
