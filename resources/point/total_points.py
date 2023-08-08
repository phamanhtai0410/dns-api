from flask_restful import Resource
from connect import security
from pydash import get
import pydash as py_

from services.point.point import POINTsService 
from schemas.point.total_point import TotalPointSchema,TotalPointResponseSchema

class PointServiceResource(Resource):

    @security.http(
        params=TotalPointSchema(),
        login_required=False,
        response=TotalPointResponseSchema()
    )
    def get(self, params):
        _address = get(params, 'user_address')

        _point = POINTsService.get_point_by_address(user_address=_address)

        return _point
