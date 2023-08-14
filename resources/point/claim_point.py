from flask_restful import Resource
from connect import security
from pydash import get

from services.point.point import POINTsService 
from schemas.point.claim_point import ClaimPointSchema

class ClaimPointServiceResource(Resource):

    @security.http(
        form_data=ClaimPointSchema(),
        login_required=False
    )
    def post(self, form_data):
        _address = get(form_data, 'user_address')

        _point = POINTsService.claim_point(user_address=_address)

        return _point
