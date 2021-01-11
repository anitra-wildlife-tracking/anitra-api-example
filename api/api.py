from .apiwrapper import AnitraApiWrapper
from .apiwrapper import ApiScrollError



class ScrollResponse():

    def __init__(self, api_wrapper, token, device_id, from_date = None, to_date = None, updates_after = None, mapping = None):
        self.api_wrapper = api_wrapper
        self.token = token
        self.device_id = device_id
        self.from_date = from_date
        self.updates_after = updates_after
        self.to_date = to_date
        self.scroll_id = None
        self.header = None
        self.data_after = True
        self.mapping = mapping

    def fetch_positions(self):
        try:
            if (self.scroll_id == None):
                data = self.api_wrapper.get_devicedata(
                    self.token,
                    self.device_id,
                    None,
                    self.from_date,
                    self.to_date,
                    self.updates_after,
                    self.mapping
                )

                self.scroll_id = data['scroll_id']
                self.data_after = data['continue']
                self.header = data['header']
                return data['data']
        
            data = self.api_wrapper.get_devicedata(
                self.token,
                self.device_id,
                self.scroll_id,
                None,
                None,
                None,
                self.mapping
            )

            self.data_after = data['continue']

            return data['data']
        except ApiScrollError as identifier:
            self.data_after = False
            return []

    def get_positions(self):
        first = True
        while (self.data_after):
            positions_dict = {}

            positions_dict = self.fetch_positions()

            if (first):
                yield self.header

            for pos in positions_dict:
                yield pos


class AnitraApi(object):
    def __init__(self, client_id, client_key, api_url, debug = False):
        self.client_id = client_id
        self.client_key = client_key
        self.api_url = api_url
        self.debug = debug
        self.logged = False
        self.api_wrapper = AnitraApiWrapper(api_url)
        self.token = ''
    
    def login(self):
        login_info = self.api_wrapper.login(
            self.client_id,
            self.client_key
        )

        self.token = login_info["token"]

        pass

    def get_devices(self):

        if not self.logged:
            self.login()

        res = self.api_wrapper.get_devices(
            self.token
        )

        return res

    def get_devicedata(self, device_id, date_from = None, date_to = None, updates_after = None, mapping = None):

        if not self.logged:
            self.login()

        return ScrollResponse(self.api_wrapper, self.token, device_id, date_from, date_to, updates_after, mapping)