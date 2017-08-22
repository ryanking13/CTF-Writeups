import hashlib
from flask.sessions import TaggedJSONSerializer, SecureCookieSessionInterface
from flask import Flask, session
from itsdangerous import URLSafeTimedSerializer

def decode_flask_cookie(secret_key, cookie_str):
    salt = 'cookie-session'
    serializer = TaggedJSONSerializer()
    signer_kwargs = {
        'key_derivation': 'hmac',
        'digest_method': hashlib.sha1
    }
    s = URLSafeTimedSerializer(secret_key, salt=salt, serializer=serializer, signer_kwargs=signer_kwargs)
    return s.loads(cookie_str)

def encode_flask_cookie(dic):
    app = Flask("app")
    app.secret_key = "v3ry_v3ry_s3cr37_k3y"

    session_serializer = SecureCookieSessionInterface().get_signing_serializer(app)

    return session_serializer.dumps(dic)

key = "v3ry_v3ry_s3cr37_k3y"
cookie = "eyJ1cmwiOiJodHRwOi8vbG9jYWxob3N0L2ZsYWcifQ.DHs5gg.wQS8Gv5D42piFitJKlOV8ivQ9ks"
d = decode_flask_cookie(key, cookie)

print(d)

dic = {u'url': u'https://localhost'}

e = encode_flask_cookie(dic)

print(e)

print(decode_flask_cookie(key, e))