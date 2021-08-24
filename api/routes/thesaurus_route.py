from flask import Blueprint, jsonify, make_response, request
from odenet import *


bp = Blueprint('thesaurus', __name__, url_prefix='/api')


@bp.route('/synonyms', methods=['GET'])
def get_synonyms():
    """
    example: GET: host/api/synonyms?word=zeigen
    """
    word = request.args.get('word', default='', type=str)
    synonym_groups = synonyms_word(word)

    if(not synonym_groups):
        return jsonify([]), 204

    synonyms = []
    for synonym_group in synonym_groups:
        synonyms += synonym_group
    return jsonify(synonyms), 200


@bp.route('/hypernyms', methods=['GET'])
def get_hypernyms():
    """
    example: GET: host/api/hypernyms?word=zeigen
    """
    word = request.args.get('word', default='', type=str)
    hypernym_groups = hypernyms_word(word)

    if(not hypernym_groups):
        return jsonify([]), 204

    hypernyms = []
    for hypernym_group in hypernym_groups:
        hypernyms += hypernym_group[2]
    return jsonify(hypernyms), 200

@bp.route('/hyponyms', methods=['GET'])
def get_hyponyms():
    """
    example: GET: host/api/hyponyms?word=zeigen
    """
    word = request.args.get('word', default='', type=str)
    hyponym_groups = hyponyms_word(word)

    if(not hyponym_groups):
        return jsonify([]), 204

    hyponyms = []
    for hyponym_group in hyponym_groups:
        hyponyms += hyponym_group[2]
    return jsonify(hyponyms), 200

@bp.route('/meronyms', methods=['GET'])
def get_meronyms():
    """
    example: GET: host/api/meronyms?word=zeigen
    """
    word = request.args.get('word', default='', type=str)
    meronym_groups = meronyms_word(word)

    if(not meronym_groups):
        return jsonify([]), 204

    meronyms = []
    for meronym_group in meronym_groups:
        meronyms += meronym_group[2]
    return jsonify(meronyms), 200

    
@bp.route('/holonyms', methods=['GET'])
def get_holonyms():
    """
    example: GET: host/api/holonyms?word=zeigen
    """
    word = request.args.get('word', default='', type=str)
    holonym_groups = holonyms_word(word)

    if(not holonym_groups):
        return jsonify([]), 204

    holonyms = []
    for holonym_group in holonym_groups:
        holonyms += holonym_group[2]
    return jsonify(holonyms), 200
    
@bp.route('/antonyms', methods=['GET'])
def get_antonyms():
    """
    example: GET: host/api/antonyms?word=zeigen
    """
    word = request.args.get('word', default='', type=str)
    antonym_groups = antonyms_word(word)

    if(not antonym_groups):
        return jsonify([]), 204

    antonyms = []
    for antonym_group in antonym_groups:
        antonyms += antonym_group[2]
    return jsonify(antonyms), 200