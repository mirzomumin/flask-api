from flask import Blueprint, jsonify, request
from .models import Result
from .db import SessionLocal

bp = Blueprint('api', __name__)

@bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"}), 200

@bp.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    if not data or 'name' not in data or 'score' not in data:
        return jsonify({"error": "Invalid input"}), 400

    db = SessionLocal()
    try:
        result = Result(name=data['name'], score=int(data['score']))
        db.add(result)
        db.commit()
        return jsonify({"message": "Data saved successfully"}), 201
    except Exception as e:
        db.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        db.close()

@bp.route('/results', methods=['GET'])
def results():
    db = SessionLocal()
    try:
        results = db.query(Result).order_by(Result.timestamp.desc()).all()
        output = [
            {
                "id": r.id,
                "name": r.name,
                "score": r.score,
                "timestamp": r.timestamp.isoformat()
            } for r in results
        ]
        return jsonify(output), 200
    finally:
        db.close()
