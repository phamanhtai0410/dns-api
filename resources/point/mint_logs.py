from flask_restful import Resource
from connect import security
from pydash import get
import pydash as py_
from services.point.point import POINTsService
from schemas.point.mint_logs import MintLogsSchema
class MintLogsResource(Resource):
    @security.http(
            login_required=False,
            form_data=MintLogsSchema()
        )
    def post(self,form_data):
        POINTsService.mint_processing(self,form_data=form_data)    
        return {}
