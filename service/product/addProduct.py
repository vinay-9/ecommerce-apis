from dataclasses import asdict
from enum import unique
from flask_jwt_extended.utils import get_jwt_identity
from sqlalchemy.orm import relation
from models.dbconn import Session
from models.entities import  Product
from service.JsonResponse import JsonResponse
from sqlalchemy import and_, select, desc
import logConfig



def AddProduct(req_obj):
    response = JsonResponse()
    session = Session() 

    try:
        data= []
        if int(req_obj.get('quantity')) < 0 :
            raise ValueError("negative quantity not allowed")
        product= Product(
            name = req_obj.get('name'),
            category_name = req_obj.get('category_name'),
            description = req_obj.get('description'),
            buy_price = int(req_obj.get('buy_price')),
            sell_price = int(req_obj.get('sell_price')),
            quantity = int(req_obj.get('quantity'))
        )
        session.add(product)
        print({**asdict(product)})
        response.set_data({**asdict(product)})
        response.set_code(201)
        response.set_status("successful")
        response.set_reason("")
        session.commit()


    except ValueError as ve:
        response.set_code(416)
        response.set_status("failed")
        response.set_reason(str(ve))
        logConfig.logError("Error in adding a negative quantity product => " + str(e))

    except Exception as e:
        response.set_code(400)
        response.set_status("failed")
        response.set_reason(str(e))
        logConfig.logError("Error in adding a profile  => " + str(e))
    finally:
        session.close()
        return response.returnResponse()