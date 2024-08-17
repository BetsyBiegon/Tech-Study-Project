from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..models import Content, Comment, User, db

bp = Blueprint('content', __name__)

@bp.route('/content', methods=['POST'])
@jwt_required()
def create_content():
    data = request.get_json()
    title = data.get('title')
    body = data.get('body')
    content_type = data.get('type')
    category = data.get('category')
    current_user = get_jwt_identity()
    author = User.query.filter_by(email=current_user['email']).first()

    content = Content(title=title, body=body, type=content_type, category=category, author_id=author.id)
    db.session.add(content)
    db.session.commit()

    return jsonify({"msg": "Content created successfully"}), 201

@bp.route('/content', methods=['GET'])
@jwt_required()
def get_contents():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    contents = Content.query.paginate(page=page, per_page=per_page)
    data = [{
        'id': content.id,
        'title': content.title,
        'body': content.body,
        'type': content.type,
        'category': content.category,
        'author_id': content.author_id,
        'created_at': content.created_at
    } for content in contents.items]
    
    return jsonify(data), 200

@bp.route('/content/<int:content_id>/comment', methods=['POST'])
@jwt_required()
def comment_on_content(content_id):
    data = request.get_json()
    body = data.get('body')
    current_user = get_jwt_identity()
    author = User.query.filter_by(email=current_user['email']).first()

    comment = Comment(body=body, content_id=content_id, author_id=author.id)
    db.session.add(comment)
    db.session.commit()

    return jsonify({"msg": "Comment added successfully"}), 201
