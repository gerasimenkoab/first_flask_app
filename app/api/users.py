from app.api import bp

@bp.route('/users/<int:id>', methods = ["GET"])
def get_user():
    pass

@bp.route('/users', methods = ["GET"])
def get_users():
    pass

@bp.route('/users/<int:id>/followers', methods = ["GET"])
def get_followers():
    pass

@bp.route('/users/<int:id>/followed', methods = ["GET"])
def get_followed():
    pass

@bp.route('/users', methods = ["POST"])
def create_user():
    pass

@bp.route('/users/<int:id>', methods = ["PUT"])
def modify_user():
    pass

@ bp.route('/users/<int:id>', methods = ["DELETE"])
def delete_user():
    pass

