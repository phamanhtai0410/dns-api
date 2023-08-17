# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from flask_restful import Resource
from pydash import get

from connect import security
from models import SocialsModel
from schemas.social.one_account import OneAccountLinkedSocialFormData
from schemas.social.accounts_linked_with_domains import AccountsLinkedWithDomainsResponseSchema
from services.social.social import SocialServices

class LinkedWithOneAddressResource(Resource):

    @security.http(
        response=AccountsLinkedWithDomainsResponseSchema()
    )
    def get(self, wallet_address):
        _res = SocialServices.get_social_linked_of_one_wallet(wallet_address=wallet_address)
        return _res   
        
        
    
    @security.http(
        form_data=OneAccountLinkedSocialFormData()
    )
    def post(self, form_data, wallet_address):
        _wallet_address = wallet_address
        _social_name = get(form_data, 'social_name')
        _social_account = get(form_data, 'social_account')
        return SocialServices.submit_social_linked_account(
            _wallet_address,
            _social_name,
            _social_account
        )
