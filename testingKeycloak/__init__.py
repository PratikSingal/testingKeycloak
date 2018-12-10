import requests
import jwt
from .helperFunctions import convertToPEM

def verifyToken(token,publicKey,algo,audience):
    publicKeyInPEMFormat = convertToPEM(publicKey)
    algorithmUsed = [];
    algorithmUsed.append(algo);
    try:
        payload = jwt.decode(token, publicKeyInPEMFormat, algorithms=algorithmUsed,audience=audience)
        return payload
    except Exception as e:
        raise Exception

def getUserDetails(payload):
    obj = {
        'name': None,
        'email': None
    }

    if "name" in payload:
        obj['name'] = payload['name'];
    if "email" in payload:
            obj['email'] = payload['email'];

    return obj;

def validateRole(clientName,roleToValidate,payLoadData):
    clientRoles = payLoadData['resource_access']['account']['roles']
    if not roleToValidate and not roleToValidate.issubset(clientRoles):
        raise Exception("ROLE_NOT_AUTHORIZED")
    return True

def doBasicAuthentication(keycloakServerAddress,realm,username,password,clientId,grantType):
    requestObj = {
        'url':"http://"+keycloakServerAddress+"/auth/realms/"+realm+"/protocol/openid-connect/token",
        'headers': {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        'body': {
            "username": username,
            "password": password,
            "client_id": clientId,
            "grant_type": grantType
        }

    }
    responseObj = {
        "statusCode":"",
        "data":""
    }
    try:
        response = requests.post(requestObj['url'], data=requestObj['body'], headers=requestObj['headers'])
        if response.status_code == 200:
            responseObj['statusCode'] = response.status_code
            responseObj['data'] = response.json()
            return responseObj
        else:
            if "error" in response.json():
                responseObj['statusCode'] = response.status_code
                responseObj['data'] = response.json().get('error',None)
                print(response.json())
            else:
                responseObj['statusCode'] = response.status_code
                responseObj['data'] = "Error"
                print(response.json())

        return responseObj
    except Exception as e:
        raise  Exception

'''
if __name__ == '__main__':
    a = doBasicAuthentication('localhost:8080','pmss','pmss@test.com','admin','pmss','password')
    print(a)
    publicKey ="" 
    token=a['data']['refresh_token']
    payload = verifyToken(token,publicKey,'RS256','pmss')
    print(payload)
    validateRole('pmss',None,payload)
'''

