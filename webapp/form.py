from wtforms import Form, StringField, TextAreaField, validators, RadioField
from wtforms import HiddenField, PasswordField

strip_filter = lambda x: x.strip() if x else None


# class BlogCreateForm(Form):
#     title = StringField('Title', [validators.Length(min=1, max=255)],
#                         filters=[strip_filter])
#     body = TextAreaField('Contents', [validators.Length(min=1)],
#                          filters=[strip_filter])
#
#
# class BlogUpdateForm(BlogCreateForm):
#     id = HiddenField()


class RegistrationForm(Form):
    # username = StringField('username', [validators.Length(min=1, max=255)], filters=[strip_filter])
    email =    StringField('email', [validators.Length(min=1, max=255)], filters=[strip_filter])
    password = PasswordField('password', [validators.Length(min=3)])
    confirm_password = PasswordField('confirm_password', [validators.Length(min=3)])
    # sex = RadioField('Sex', choices=[('male', 'male'), ('female', 'female')])


class LoginForm(Form):
    username = StringField('username', [validators.Length(min=1, max=255)], filters=[strip_filter])
    password = PasswordField('password', [validators.Length(min=3)])


class PaymentForm(Form):
    amount = StringField('amount', [validators.Length(min=1, max=10)], filters=[strip_filter])
    email  = StringField('email', [validators.Length(min=1, max=255)], filters=[strip_filter])
    card   = StringField('card', [validators.Length(min=16, max=16)], filters=[strip_filter])