from flask_restful import Resource

# Criar os endpoints de Funcionario: GET, POST, PUT, DELETE
class Cliente(Resource):

    def get(self, id):
        return {"msg": "get executado com suceso"}, 200

    def post(self, id):
        return {"msg": "post executado com sucesso"}, 201

    def put(self, id):
        return {"msg": "put executado  com sucesso"}, 201
        
    def delete(self, id):
        return {"msg": "delete executado com sucesso"}, 201