from flask import Blueprint, jsonify, make_response, request
from nltk.tokenize import sent_tokenize, word_tokenize
import string

bp = Blueprint('statistics', __name__, url_prefix='/api')


@bp.route('/avg_sentence_length/', methods=['GET'])
def get_average_sentence_length():
    """
    example: GET: host/api/avg_sentence_length?text=This is a sentence. This is one too! How about this one?
    """
    text = request.args.get('text', default=None, type=str)

    if text is None or "":
        return jsonify({'success': False}), 400, {'ContentType': 'application/json'}

    tokenized_text = sent_tokenize(text)
    sentence_count = len(tokenized_text)

    word_count = 0
    for sentence in tokenized_text:
        # remove punctuation symbols as they are counted as separate tokens
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        tokenized_word = word_tokenize(sentence)
        word_count += len(tokenized_word)

    if word_count is 0:
        return jsonify({'success': False}), 400, {'ContentType': 'application/json'}

    avg_sentence_length = word_count / sentence_count

    return jsonify(avg_sentence_length), 200
