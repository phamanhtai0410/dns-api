from flask_restful import Resource
from connect import security
from pydash import get
import pydash as py_

from services.point.point import POINTsService 
from schemas.point.default_points import DefaultPointsSchema

class DefaultPointsResource(Resource):

    @security.http(
        login_required=False,
        form_data=DefaultPointsSchema(),
    )
    def put(self,form_data):
        POINTsService.set_default_point(form_data=form_data)
        return {}
    
    @security.http(
        login_required=False,
        response=DefaultPointsSchema(),
    )
    def get(self):    
        return POINTsService.get_default()
    