# app/routes/__init__.py
from flask import Blueprint
from .auth import auth_routes
from .content import content_routes


auth_bp = Blueprint('auth', __name__)
content_bp = Blueprint('content', __name__)

from . import auth, content
