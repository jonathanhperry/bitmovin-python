from . import AbstractInput


class FTPInput(AbstractInput):

    def __init__(self, host, username, password, port=None, passive=None, id_=None, custom_data=None):
        super().__init__(id_=id_, custom_data=custom_data)
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.passive = passive

    @classmethod
    def parse_from_json_object(cls, json_object):
        id_ = json_object['id']
        host = json_object['host']
        username = json_object.get('username')
        password = json_object.get('password')
        port = json_object.get('port')
        passive = json_object.get('passive')
        ftp_input = FTPInput(
            host=host, port=port, username=username, password=password, passive=passive, id_=id_)
        return ftp_input
