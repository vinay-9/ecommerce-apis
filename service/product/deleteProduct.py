from dataclasses import asdict
from enum import unique
from flask_jwt_extended.utils import get_jwt_identity
from sqlalchemy.orm import relation
from models.dbconn import Session
from models.entities import  Product
from service.JsonResponse import JsonResponse
from sqlalchemy import and_, select, desc
import logConfig



def DeleteProduct(req_params):
    response = JsonResponse()
    session = Session() 
    product= {}
    try:
        product= (session.query(Product).filter(Product.id == int(req_params['product_id'])).first())
        print(req_params)
        
        session.add(product)
        session.delete(product)
        session.flush();

        print("deleted successfully")
        # response.set_data({**asdict(product)})
        response.set_code(204)
        response.set_status("successful")
        response.set_reason("")
        session.commit()

    except Exception as e:
          # Internal error
        response.set_code(400)
        response.set_status("failed")
        response.set_reason(str(e))
        logConfig.logError("Error in  fetching a profile  => " + str(e))
    finally:
        session.close()
        return response.returnResponse()
