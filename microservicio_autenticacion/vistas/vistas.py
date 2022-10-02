from flask import request
from microservicio_autenticacion.modelos.modelos import Usuario
from ..modelos import db, UsuarioSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token
usuario_schema = UsuarioSchema()

class VistaLogIn(Resource):

    def post(self):
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"], Usuario.contrasena == request.json["contrasena"]).first()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            if(Usuario.ip_autorizada == request.remote_addr and  Usuario.habilitado == True):
                token_de_acceso = create_access_token(identity=usuario.id)
                return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso}
            return "El usuario está autorizado", 401