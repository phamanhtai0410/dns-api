
class InvalidWalletAddressEx(Exception):
    def __init__(self, msg='Invalid wallet address', *args: object, **kwargs) -> None:
        super().__init__(*args)
        self.status_code = 400
        self.msg = msg
        self.errors = kwargs.get('errors', [])
        self.error_code = 'E_INVALID_WALLET_ADDRESS'

    pass