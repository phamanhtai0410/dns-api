from web3 import Web3
from exceptions.social import InvalidWalletAddressEx
from models import SocialsModel
from services.point import point

class SocialServices:

    @staticmethod
    def get_social_linked_of_one_wallet(wallet_address):
        if not Web3.is_address(wallet_address):
            raise InvalidWalletAddressEx
        _wallet = wallet_address.lower()

        _check_exist_bonus = SocialsModel.find(
            filter={
                'address': _wallet,
                'bonus_points': 200
            }
        )
        print("_check_exist_bonus",_check_exist_bonus)
        if _check_exist_bonus == []:
            print("____________run______________")
            SocialsModel.update_one(
                filter={
                    'address': _wallet,
                    # 'bonus_points': 200
                },
                obj={
                    'bonus_points': 200,
                    'updated_by': 'scroll-api:services:social:update_bonus_social_linked_account'
                },
            )
        _linked_list = SocialsModel.find(
            filter={
                'address': _wallet
            }
        )
        print(_linked_list)
        return {
            'items': _linked_list
        }
    
    @staticmethod
    def submit_social_linked_account(_wallet_address, _social_name, _social_account):
        if not Web3.is_address(_wallet_address):
            raise InvalidWalletAddressEx
        _wallet_address = _wallet_address.lower()
        _check_exist = SocialsModel.find_one(
            {
                'address': _wallet_address,
                'social_name': _social_name
            }
        )
        if _check_exist:
            SocialsModel.update_one(
                filter={
                    'address': _wallet_address,
                    'social_name': _social_name
                },
                obj={
                    'social_account': _social_account,
                    'updated_by': 'scroll-api:services:social:submit_social_linked_account'
                },
            )
        else:
            SocialsModel.insert_one(
                {
                    'address': _wallet_address,
                    'social_name': _social_name,
                    'social_account': _social_account,
                    'bonus_points': 200,
                    'created_by': 'scroll-api:services:social:submit_social_linked_account'
                }
            )
        return {
            'result': 'done'
        }