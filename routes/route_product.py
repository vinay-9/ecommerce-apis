from flask import request, jsonify
from flask_restx import Resource, fields, reqparse
from werkzeug.datastructures import FileStorage
from service.Validatefunction import validateParamsFromCheckList
from flask_jwt_extended import jwt_required, get_jwt_identity
from swaggerConfig import api

from service.product.getProduct import GetProduct
from service.product.addProduct import AddProduct
from service.product.updateProduct import UpdateProduct
from service.product.deleteProduct import DeleteProduct

product = api.namespace("products", description="product Apis")

get_product_model = reqparse.RequestParser()
get_product_model.add_argument(
    "product_id", type=int, required=True, help="unique id of the product", location="args"
)
delete_product_model = get_product_model.copy()


add_product_model= reqparse.RequestParser()

# {
# "name": "",
# "category_name": "",
# "description": "",
# "buy_price": ,
# "sell_price": ,
# "quantity":
# }

add_product_model = reqparse.RequestParser()
add_product_model.add_argument(
    "name", type=str, required=True, help="unique name of product", location="form"
)
add_product_model.add_argument(
    "category_name", type=str, help="unique name of category", location="form"
)
add_product_model.add_argument(
    "description", type=str, required=True, help="description of the product", location="form"
)
add_product_model.add_argument(
    "buy_price", type=int, required=True, help="buying price of product", location="form"
)
add_product_model.add_argument(
    "sell_price", type=int, required=True, help="selling price of product", location="form"
)
add_product_model.add_argument(
    "quantity", type=int, required=True, help="quantity to be added", location="form"
)


update_product_model = add_product_model.copy()
# .RequestParser()
update_product_model.add_argument(
    "product_id", type=int, required=True, help="id of the product to be updated", location="args"
)
# update_product_model.add_argument(
#     "name", type=str, required=True, help="unique name of product", location="form"
# )
# update_product_model.add_argument(
#     "category_name", type=str, help="unique name of category", location="form"
# )
# update_product_model.add_argument(
#     "description", type=str, required=True, help="description of the product", location="form"
# )
# update_product_model.add_argument(
#     "buy_price", type=int, required=True, help="buying price of product", location="form"
# )
# update_product_model.add_argument(
#     "sell_price", type=int, required=True, help="selling price of product", location="form"
# )
# update_product_model.add_argument(
#     "quantity", type=int, required=True, help="quantity to be added", location="form"
# )



@product.route("/")
class ProductApi(Resource):

    @api.doc(responses={200: "OK"})
    @api.expect(add_product_model)
    def post(self):
        request_body= validateParamsFromCheckList(request.form, [
            "name",
            "category_name",
            "description",
            "buy_price",
            "sell_price",
            "quantity"
        ])
        output = AddProduct(request_body)
        return jsonify(output)
    
    @api.doc(responses={200: "OK"})
    @api.expect(delete_product_model)
    def delete(self):
        request_params= validateParamsFromCheckList(request.args, [
           "product_id"
        ])
        output = DeleteProduct(request_params)
        return jsonify(output)


    @api.doc(responses={200: "OK"})
    @api.expect(update_product_model)
    def put(self):
        request_body= validateParamsFromCheckList(request.form, [
            "name",
            "category_name",
            "description",
            "buy_price",
            "sell_price",
            "quantity"
        ])
        request_params= validateParamsFromCheckList(request.args, [
            "product_id",
        ])

        output = UpdateProduct(request_params, request_body)
        return jsonify(output)



    @api.doc(responses={200: "OK"})
    @api.expect(get_product_model)
    def get(self):
        print(request)
        request_params= validateParamsFromCheckList(request.args, [
           "product_id"
        ])
        output = GetProduct(request_params)
        return jsonify(output)

