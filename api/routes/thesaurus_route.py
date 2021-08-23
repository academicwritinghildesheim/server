from flask import Blueprint, jsonify, request
from odenet import hypernyms_word, synonyms_word, meronyms_word, holonyms_word, antonyms_word, hyponyms_word


bp = Blueprint('thesaurus', __name__, url_prefix='/api')


@bp.route('/synonyms', methods=['GET'])
def get_synonyms():
    """
    example: GET: host/api/synonyms?word=zeigen
    """
    word = request.args.get('word', default='', type=str)
    synonyms = synonyms_word(word)
    return jsonify(synonyms), 200


@bp.route('/hypernyms', methods=['GET'])
def get_hypernyms():
    """
    example: GET: host/api/hypernyms?word=zeigen
    """
    word = request.args.get('word', default='', type=str)
    hypernyms = hypernyms_word(word)
    return jsonify(hypernyms), 200


@bp.route('/hyponyms', methods=['GET'])
def get_hyponyms():
    """
    example: GET: host/api/hyponyms?word=zeigen
    """
    word = request.args.get('word', default='', type=str)
    hyponyms = hyponyms_word(word)
    return jsonify(hyponyms), 200


@bp.route('/meronyms', methods=['GET'])
def get_meronyms():
    """
    example: GET: host/api/meronyms?word=zeigen
    """
    word = request.args.get('word', default='', type=str)
    meronyms = meronyms_word(word)
    return jsonify(meronyms), 200


@bp.route('/holonyms', methods=['GET'])
def get_holonyms():
    """
    example: GET: host/api/holonyms?word=zeigen
    """
    word = request.args.get('word', default='', type=str)
    holonyms = holonyms_word(word)
    return jsonify(holonyms), 200


@bp.route('/antonyms', methods=['GET'])
def get_antonyms():
    """
    example: GET: host/api/antonyms?word=zeigen
    """
    word = request.args.get('word', default='', type=str)
    antonyms = antonyms_word(word)
    return jsonify(antonyms), 200
