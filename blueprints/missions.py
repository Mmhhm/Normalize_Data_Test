from os import abort
from db import db
from flask import Blueprint, request, jsonify, abort
from models import source_missions
from models.source_missions import SourceMissions
from models.normalized_missions import Mission

missions_bp = Blueprint('missions', __name__)


@missions_bp.route('/api/mission', methods=['GET'])
def get_missions():
    mission = Mission.query.filter_by(country="GREAT BRITAIN")
    if not mission:
        abort(404, description="Team not found")
    return jsonify([mission.to_dict() for mission in mission])


@missions_bp.route('/api/mission/<int:m_id>', methods=['GET'])
def get_mission(m_id):
    mission = Mission.query.filter_by(mission_id=m_id).first()
    if not mission:
        abort(404, description="Team not found")
    return jsonify(mission.to_dict())





































