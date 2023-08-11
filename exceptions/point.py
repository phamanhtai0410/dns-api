class UserNotFoundEx(Exception):
    def __init__(self, msg='User Not Found', *args: object, **kwargs) -> None:
        super().__init__(*args)
        self.status_code = 400
        self.msg = msg
        self.errors = kwargs.get('errors', [])
        self.error_code = 'E_USER_NOT_FOUND'

    pass

class WaitingTimeEx(Exception):
    def __init__(self, waitingtime, msg='Claim after', *args: object, **kwargs) -> None:
        super().__init__(*args)
        self.status_code = 400
        self.msg = msg+' '+str(waitingtime)
        self.errors = kwargs.get('errors', [])
        self.error_code = 'WAITING_TIME'

    pass

class ReferralAddressError(Exception):
    def __init__(self, msg='Error referral address', *args: object, **kwargs) -> None:
        super().__init__(*args)
        self.status_code = 400
        self.msg = msg
        self.errors = kwargs.get('errors', [])
        self.error_code = 'E_USER_NOT_FOUND'

    pass
