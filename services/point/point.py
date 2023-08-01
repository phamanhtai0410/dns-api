import datetime
import traceback

import pydash as py_
import bson
from bson import ObjectId

from models import TotalPointModel, HistoryPointModel

# from lib import dt_utcnow
from datetime import datetime, timedelta
from connect import redis_cluster
from worker import worker

from exceptions.point import UserNotFoundEx, WaitingTimeEx

class POINTsService :

    @classmethod
    def get_point_by_address(
        cls,
        user_address,
    ):

        _detail = TotalPointModel.find_one({
            'user_address': user_address
        })
        if _detail is None:
            raise UserNotFoundEx
        return py_.get(_detail, 'total_point')

    
    @classmethod
    def update_point(
        cls, 
        user_address
    ):
        obj = TotalPointModel.find_one({
            'user_address': user_address
        }) 

        
        if(obj):
            # check time to update point
            # Get the current UTC time
            current_utc_time = datetime.utcnow()
            # Get the updated time
            if py_.get(obj, 'updated_time') is None:
                updated_at = datetime.now().date().replace(hour=0, minute=0, second=0, microsecond=0)
            else:
                updated_at = py_.get(obj, 'updated_time')
        
            waiting_time = current_utc_time - updated_at #seconds
            remaining_waiting_time = (24*3600 - waiting_time.total_seconds())/3600 # datetime

            print('remaining_waiting_time: ',remaining_waiting_time)
            if(remaining_waiting_time>=0):
                raise WaitingTimeEx(remaining_waiting_time)
            
            # check if user is already, update data in TotalPoint Collection
            new_total_point = py_.get(obj, 'total_point') + 1000
            TotalPointModel.update_one(
                {'user_address': user_address},
                {
                    'total_point': new_total_point,
                    'updated_by': 'dns-api:services:POINTsService:update_point'
                },
            )
        else:
            # if not, add new data to TotalPoint Collection
            TotalPointModel.insert_one({
                'user_address': user_address,
                'total_point': 1000,
                'created_by': 'dns-api:services:POINTsService:update_point',
                'updated_by': ''
            })

    @staticmethod
    def claim_point(user_address:str):
        _log_data = {
            'user_address': user_address,
            'point': 1000
        }

        HistoryPointModel.insert_one({
            'user_address': py_.get(_log_data, 'user_address'),
            'point': py_.get(_log_data, 'point'),
            'created_by': 'dns-api:services:POINTsService:claim_point',
        })

        POINTsService.update_point(py_.get(_log_data, 'user_address'))
        return {}



        
