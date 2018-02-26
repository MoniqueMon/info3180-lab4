from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    uploadfile = FileField('Image', validators=[FileRequired(),FileAllowed(['jpg','jpeg','png'], 'Images only!')])
