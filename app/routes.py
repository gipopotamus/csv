import os
from flask import Blueprint, request, jsonify
from app import db
from .models import UploadedFile
from .serializers import UploadedFileSchema
import pandas as pd


bp = Blueprint('api', __name__)


@bp.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file provided'}), 400

    filename = file.filename
    columns = []  # Parse the columns from the file if needed

    # Save the file to the 'uploads' directory
    file_path = os.path.join('uploads', filename)
    file.save(file_path)

    uploaded_file = UploadedFile(filename=filename, columns=columns)
    db.session.add(uploaded_file)
    db.session.commit()

    return jsonify({'message': 'File uploaded successfully'}), 201


@bp.route('/files', methods=['GET'])
def get_files_list():
    files = UploadedFile.query.all()
    schema = UploadedFileSchema(many=True)
    return jsonify(schema.dump(files))


@bp.route('/files/<filename>', methods=['GET'])
def get_file_data(filename):
    file = UploadedFile.query.filter_by(filename=filename).first()
    if not file:
        return jsonify({'error': 'File not found'}), 404

    # Load the CSV file using pandas
    df = pd.read_csv(os.path.join('uploads', filename))

    # Handle optional filters
    filters = request.args.get('filters')
    if filters:
        filters = filters.split(',')
        filtered_df = df.copy()
        for f in filters:
            column, value = f.split(':')
            filtered_df = apply_filter(filtered_df, column, value)

        df = filtered_df

    # Handle optional sorting
    sort_by = request.args.get('sort_by')
    if sort_by:
        sort_columns = sort_by.split(',')
        df.sort_values(by=sort_columns, inplace=True)

    return df.to_json(orient='records'), 200

def apply_filter(df, column, value):
    try:
        converted_value = pd.to_numeric(value)
    except ValueError:
        converted_value = value

    return df[df[column].astype(str) == str(converted_value)]




@bp.route('/files/<filename>', methods=['DELETE'])
def delete_file(filename):
    file = UploadedFile.query.filter_by(filename=filename).first()
    if not file:
        return jsonify({'error': 'File not found'}), 404

    # Remove the file from the database and the file system
    db.session.delete(file)
    db.session.commit()
    return jsonify({'message': f'File {filename} deleted successfully'}), 200
