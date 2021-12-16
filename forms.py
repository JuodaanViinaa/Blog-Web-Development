from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# Create Flask Form
class RegisterForm(FlaskForm):
    mail = StringField(label="Email", validators=[DataRequired(message="Must provide an email."),
                                                  Email(message="That does not look like a valid Email")])
    username = StringField(label="Username", validators=[DataRequired(message="Must provide an username.")])
    password = PasswordField(label="Password",
                             validators=[DataRequired(message="Whoopsie daisie. Password must not be empty."),
                                         Length(min=8, message="Password must be at least 8 characters long.")])
    submit = SubmitField(label="Register me")


class LoginForm(FlaskForm):
    mail = StringField(label="Email", validators=[DataRequired(message="Must provide an email."),
                                                  Email(message="That does not look like a valid Email")])
    password = PasswordField(label="Password",
                             validators=[DataRequired(message="Whoopsie daisie. Password must not be empty."),
                                         Length(min=8, message="Password must be at least 8 characters long.")])
    submit = SubmitField(label="Register me")


class CommentForm(FlaskForm):
    body = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
