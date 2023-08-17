# -*- coding: utf-8 -*-
"""
   Description:
        -
        -
"""
from resources.social.accounts_linked_with_domains import AccountsLinkedWithDomainsResource
from resources.social.check_account_linked_with_domain import CheckAccountLinkedWithDomainResource
from resources.social.linked_with_one_address import LinkedWithOneAddressResource

social_resources = {
    '/accounts_linked/all': AccountsLinkedWithDomainsResource,
    '/check_account_linked': CheckAccountLinkedWithDomainResource,
    '/accounts_linked/<wallet_address>': LinkedWithOneAddressResource
}
