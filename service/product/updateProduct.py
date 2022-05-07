from dataclasses import asdict
from enum import unique
from flask_jwt_extended.utils import get_jwt_identity
from sqlalchemy.orm import relation
from models.dbconn import Session
from models.entities import  Product
from service.JsonResponse import JsonResponse
from sqlalchemy import and_, select, desc
import logConfig



def UpdateProduct(req_params, req_obj):
    response = JsonResponse()
    session = Session() 
    product= {}
    try:
        print(req_obj)
        product= (session.query(Product).filter(Product.id == int(req_params.get('product_id')))
        .first())
        print(product)
      
        if product is None:
            # response.set_code(404)
            raise ValueError("Product not found")
         
        product.name = req_obj.get('name')
        product.category_name = req_obj.get('category_name');
        product.description = req_obj.get('description');
        product.buy_price = req_obj.get('buy_price');
        product.sell_price= req_obj.get('sell_price');
        product.quantity = req_obj.get('quantity');

        session.add(product)
        
        print(product)
        print({**asdict(product)})

        print("hello")
        response.set_data({**asdict(product)})
        response.set_code(200)
        response.set_status("success")
        response.set_reason("")
        session.commit()

    except ValueError as ve:
        response.set_code(400)
        response.set_status("failed")
        response.set_reason(str(ve))
        logConfig.logError(str(ve))

   
    except Exception as e:
          # Internal error
        response.set_code(400)
        response.set_status("failed")
        response.set_reason(str(e))
        logConfig.logError("Error in  fetching a profile  => " + str(e))
    finally:
        session.close()
        return response.returnResponse()
