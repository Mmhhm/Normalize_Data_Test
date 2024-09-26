from os import abort
from db import db
from flask import Blueprint, request, jsonify, abort
from models import source_missions
from models.source_missions import SourceMissions

missions_bp = Blueprint('missions', __name__)

@missions_bp.route('/missions/<int:m_id>', methods=['GET'])
def get_mission(m_id):
    mission = SourceMissions.query.filter_by(mission_id=m_id).first()
    if not mission:
        abort(404, description="Team not found")
    return jsonify(mission.mission_date)






































