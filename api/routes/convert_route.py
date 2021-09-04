from flask import Blueprint, request, send_file, after_this_request
import pypandoc
import os

bp = Blueprint('convert', __name__, url_prefix='/api')


@bp.route('/convert', methods=['POST'])
def convert():
    @after_this_request
    def cleanup(response):
        os.remove(os.path.join(os.getcwd(), input_file.filename))
        os.remove(os.path.join(os.getcwd(), output_file))
        return response

    input_file = request.files['file']

    input_file.save(os.path.join(os.getcwd(), input_file.filename))

    output_file = input_file.filename.split('.')[0]
    output_file = output_file + '.pdf'

    pypandoc.convert_file(input_file.filename,
                          to='pdf',
                          format='md',
                          outputfile=os.path.join(os.getcwd(), output_file))

    return send_file(os.path.join(os.getcwd(), output_file),
                     as_attachment=True), 200
