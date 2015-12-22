__author__ = 'Ahmed Nour eldeen'

import uuid
import binascii
import base64
import hashlib
import time

from models import Token

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
User = get_user_model()

from ..json_response_utils import JsonResponse, JsonPResponse

# token validation period in milliseconds
TOKEN_VALIDATION_PERIOD = 24 * 60 * 60 * 1000


@csrf_exempt
def generate_token(request):
    token_json = {}
    if 'username' in request.REQUEST:
        user = User.objects.get(username__exact=request.REQUEST['username'])
        if user.check_password(request.REQUEST['password']):
            token_obj = Token.objects.create(user=user, token=get_token(user), expiration_date=get_expiration_date())
            token_obj.save()
            token_json = {
                "token": token_obj.token,
                "expires": token_obj.expiration_date,
                "ssl": False
            }
        else:
            token_json = {"error": {
                "code": 400,
                "message": "Unable to generate token.",
                "details": ["'username' must be specified.",
                            "'password' must be specified.",
                            "'referer' must be specified."]
            }}
    else:
        token_json = {"error": {
            "code": 400,
            "message": "Unable to generate token.",
            "details": ["'username' must be specified.",
                        "'password' must be specified.",
                        "'referer' must be specified."]
        }}
    print token_json
    if 'callback' in request.REQUEST:
        return JsonPResponse(content=token_json, callback=request.REQUEST["callback"])
    else:
        return JsonResponse(content=token_json)


from httplib import HTTPConnection, HTTPSConnection
from django.http import HttpResponse
import requests
@csrf_exempt
def tokens(request):
    return proxy_view(request, "sharing/rest/p")

    url = "http://ao82912.maps.arcgis.com/sharing/rest/tokens"

    params = dict(password="cart0l0gic",
                  _servicesUrl=1,
                  clientid="ref.ArcGIS_AndroidSDK",
                  username="ao82912",request="gettoken")
    r = requests.post(url,data=params)
    # print r.status_code
    # print r.text
    token_json = {}
    if 'username' in request.POST:
        user = User.objects.get(username__exact=request.POST['username'])
        if user.check_password(request.POST['password']):
            token_obj = Token.objects.create(user=user, token=get_token(user), expiration_date=get_expiration_date())
            token_obj.save()
            token_json = {'ssl': False,
                          'token': '0DPiKuNIrrVmD8IUCuw1hQxNqZc=4d9dbbb7-3006-4d78-a9d4-a6d1ded0ff67',
                          'expires': 1449496817421.0}
    print token_json
    if 'callback' in request.REQUEST:
        return JsonPResponse(content=token_json, callback=request.REQUEST["callback"])
    else:
        return JsonResponse(content=token_json)


import requests
from django.http import HttpResponse
from django.http import QueryDict

@csrf_exempt
def proxy_view(request, url, requests_args=None):
    """
    Forward as close to an exact copy of the request as possible along to the
    given url.  Respond with as close to an exact copy of the resulting
    response as possible.
    If there are any additional arguments you wish to send to requests, put
    them in the requests_args dictionary.
    """
    requests_args = (requests_args or {}).copy()
    headers = get_headers(request.META)
    params = request.GET.copy()

    if 'headers' not in requests_args:
        requests_args['headers'] = {}
    if 'data' not in requests_args:
        requests_args['data'] = request.body
    if 'params' not in requests_args:
        requests_args['params'] = QueryDict('', mutable=True)

    # Overwrite any headers and params from the incoming request with explicitly
    # specified values for the requests library.
    headers.update(requests_args['headers'])
    params.update(requests_args['params'])

    # If there's a content-length header from Django, it's probably in all-caps
    # and requests might not notice it, so just remove it.
    for key in headers.keys():
        if key.lower() == 'content-length':
            del headers[key]

    requests_args['headers'] = headers
    requests_args['params'] = params
    url = "https://ao82912.maps.arcgis.com" if url == "" else "https://ao82912.maps.arcgis.com/" + url
    print url
    response = requests.request(request.method, url, **requests_args)

    proxy_response = HttpResponse(
        response.content,
        status=response.status_code)

    excluded_headers = set([
        # Hop-by-hop headers
        # ------------------
        # Certain response headers should NOT be just tunneled through.  These
        # are they.  For more info, see:
        # http://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html#sec13.5.1
        'connection', 'keep-alive', 'proxy-authenticate',
        'proxy-authorization', 'te', 'trailers', 'transfer-encoding',
        'upgrade',

        # Although content-encoding is not listed among the hop-by-hop headers,
        # it can cause trouble as well.  Just let the server set the value as
        # it should be.
        'content-encoding',

        # Since the remote server may or may not have sent the content in the
        # same encoding as Django will, let Django worry about what the length
        # should be.
        'content-length',
    ])
    for key, value in response.headers.iteritems():
        if key.lower() in excluded_headers:
            continue
        proxy_response[key] = value

    return proxy_response


def get_headers(environ):
    """
    Retrieve the HTTP headers from a WSGI environment dictionary.  See
    https://docs.djangoproject.com/en/dev/ref/request-response/#django.http.HttpRequest.META
    """
    headers = {}
    for key, value in environ.iteritems():
        # Sometimes, things don't like when you send the requesting host through.
        if key.startswith('HTTP_') and key != 'HTTP_HOST':
            headers[key[5:].replace('_', '-')] = value
        elif key in ('CONTENT_TYPE', 'CONTENT_LENGTH'):
            headers[key.replace('_', '-')] = value

    return headers

def get_token(user):
    # TODO: salt must be generated randomly.
    # return binascii.b2a_base64(hashlib.pbkdf2_hmac('sha1', user.username, b'salt', 1000)).rstrip() + str(uuid.uuid4())
	#### Updated by Mohamed Gamal because pbkdf2_hmac is not allowed in python 7.2.2
    return base64.b64encode(hashlib.sha1(user.username).digest()) + str(uuid.uuid4())


def is_valid_token(token):
    try:
        return Token.objects.get(token=token).expiration_date > time.time()
    except:
        return False


def validate_token(request):
    if 'token' in request.REQUEST:
        if is_valid_token(request.REQUEST['token']):
            return True
    else:
        return True


def get_expiration_date():
    return time.time() * 1000 + TOKEN_VALIDATION_PERIOD
