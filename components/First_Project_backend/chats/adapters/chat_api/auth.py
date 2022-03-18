import json
import base64
import hashlib
import falcon

from components.First_Project_backend.chats.adapters.database.tables import users_log



def check_password(data: dict):
    if data in users_log:
        return True
    return False

class AddHeaderComponent:
    def process_response(self, req, resp, resource, req_succeeded):
        resp.set_header('X-Request-Name', '*')
        resp.set_header('Content-Type', 'application/json')
        resp.set_header('Access-Control-Max-Age', '86400')

class Middleware:
    def process_request(self, req, resp): pass

    def process_resource(self, req, resp, resource, params):
        if req.path != '/login/':
            auth_hashed_data = req.headers.get('AUTHORIZATION')
            auth_hashed_data = auth_hashed_data.split()[1]
            auth_data = base64.b64decode(auth_hashed_data).decode('utf-8')
            auth_data = auth_data.split(':')
            auth_data_dict = {
                'login': auth_data[0],
                'password': auth_data[1]
            }
            if check_password(auth_data_dict):
                pass
            else:
                raise falcon.HTTPUnauthorized



