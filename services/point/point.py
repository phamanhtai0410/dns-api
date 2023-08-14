import datetime
import traceback
import pydash as py_
import bson
from bson import ObjectId
from pymongo import MongoClient
from models import TotalPointModel, HistoryPointModel,DefaultPointModel, MintLogsModel

# from lib import dt_utcnow
from datetime import datetime, timedelta
from connect import redis_cluster
from worker import worker

from exceptions.point import UserNotFoundEx,ReferralAddressError,WaitingTimeEx

class POINTsService :

    @classmethod
    def get_point_by_address(
        cls,
        user_address,
    ):

        _detail = TotalPointModel.find_one({
            'user_address': user_address
        })
        _ = {
            'total_point':0,
            'referral':0,
            'user_address': user_address
        }
        print(_detail)
        if _detail is None:
           return _ 
        return _detail

    
    @classmethod
    def update_point(
        cls, 
        user_address,rule
    ):
        obj = TotalPointModel.find_one({
            'user_address': user_address
        })
        claim = rule['default']
        if(obj):
            bonus = 0
            _referral = py_.get(obj,'referral')
            if _referral >= rule['level4']:
                bonus = rule['point4']
            elif _referral >= rule['level3']:
                bonus = rule['point3']
            elif _referral >= rule['level2']:
                bonus = rule['point2']
            elif _referral >= rule['level1']:
                bonus = rule['point1']           
            bonus = rule['default']*(1+bonus/100)
            claim = round(bonus)
            total_point = obj['total_point']
            new_total_point=total_point + claim

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
                'total_point': rule['default'],
                'referral':0,
                'created_by': 'dns-api:services:POINTsService:update_point',
                'updated_by': 'dns-api:services:POINTsService:update_point'
            })
        HistoryPointModel.insert_one({
                'user_address': user_address,
                'point_type':'daily',
                'point': claim,
                'created_by': 'dns-api:services:POINTsService:claim_point',
            })    

    @staticmethod
    def claim_point(user_address):
        _rule = DefaultPointModel.find({})[0]
        print(_rule)
        pipeline = [
            {"$match": {"user_address": user_address,"point_type":"daily"}},
            {"$sort": {"created_time": -1}},
            {"$limit": 1}
        ]
        last = list(HistoryPointModel.col.aggregate(pipeline))
        print(last)
        if not last:
            POINTsService.update_point(user_address, _rule)
        else:           
            _last = last[0]["created_time"]
            print(_last)
            _current = datetime.utcnow()
            time_difference = _current - _last
            time_difference_seconds = time_difference.days * 24 * 60 * 60 + time_difference.seconds
            print(time_difference_seconds)

            if time_difference_seconds > 1 * 24 * 60 * 60:
                POINTsService.update_point(user_address, _rule)
            else:
                wait = 1 * 24 * 60 * 60 - time_difference_seconds
                raise WaitingTimeEx(wait)

        return {}
    @classmethod
    def set_default_point(self,form_data):
        _level1 = py_.get(form_data,'level1')
        _level2 = py_.get(form_data,'level2')
        _level3 = py_.get(form_data,'level3')
        _level4 = py_.get(form_data,'level4')
        _point1 = py_.get(form_data,'point1')
        _point2 = py_.get(form_data,'point2')
        _point3 = py_.get(form_data,'point3')
        _point4 = py_.get(form_data,'point4')
        _point4 = py_.get(form_data,'point4')
        _default =py_.get(form_data,'default')
        _three = py_.get(form_data,'three')
        _four = py_.get(form_data,'four')
        _five = py_.get(form_data,'five')
        print(form_data)
        default=DefaultPointModel.update_one(
                {
                },
                {
                    # 'updated_by': get(login_info, 'user.username') or 'ADMIN',
                    'created_by': 'admin',
                    'updated_by': 'admin',
                    'deleted': False,
                    'level1':_level1,
                    'level2':_level2,
                    'level3':_level3,
                    'level4':_level4,
                    'point1':_point1,
                    'point2':_point2,
                    'point3':_point3,
                    'point4':_point4,
                    'default':_default,
                    'three':_three,
                    'four':_four,
                    'five':_five
                },
                upsert=True   
            )
        return {}
    
    @classmethod
    def get_default(self):
        _default=DefaultPointModel.find_one({})
        print(_default)
        return _default
    
    @staticmethod
    def mint_processing(self,form_data):
        user_address = py_.get(form_data,'user_address')
        referral = py_.get(form_data,'ref_address')
        if referral == user_address:
            raise ReferralAddressError
        MintLogsModel.update_one(
            {
                **form_data,
            },
            {
               'updated_by':'PointService',
               'created_by':'user_on_dapp',
            },
            upsert=True
        )
        return
    # @staticmethod
    # def mint_done(self,user_address,domain_name):
        
    #     _mint = MintLogsModel.find_one({
    #             'user_address':user_address,
    #             'domain_name':domain_name
    #     })
    #     _rule = DefaultPointModel.find({})[0]
    #     if _mint['letter'] == 3:
    #         claim = _rule['three']
    #     elif _mint['letter'] == 4:
    #         claim = _rule['four']
    #     else:
    #         claim = _rule['five']    
    #     HistoryPointModel.insert_one({
    #             'user_address': user_address,
    #             'point_type':'daily',
    #             'point': claim,
    #             'created_by': 'dns-api:services:POINTsService:claim_point',
    #         })
         
            
        