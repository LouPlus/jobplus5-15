from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField,ValidationError,
from wtforms.validators import Required,Length,Email,EqualTo
from wtforms import ValidationError

class LoginForm(Form):        #登录页面的内容  
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('提交')

    def validate_email(self,field):
        if field.data and not User.query.filter_by(email=field.data).first()
            raise ValidationError('email has not register')

    def validate_password(self,field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('passwrod error')


class Register(Form):    #求职者注册页面内容
    username = StringField('用户名',validators=[Required(),Length(1,64)])
    email = StringField('邮箱',validators=[Required(),Email()])
    password = PasswordField('密码',validators=[Required(),Length(6,24)])
    repear_password = PasswordField('重复密码',validators=[Requried(),Length(6,24),EqualTo('password',message = '密码要一致')])
    submit = SubmitField('注册')


    def validate_email(self,field):        
        if User.query.filter_by(email=field.data).first()
            raise ValidationError('邮箱已经被注册')

    def validate_name(self,field):
        if User.query.filter_by(name=field.data).first()
            raise ValidationError('名已经被注册')

    def create_user(self):
        user = User(name=self.name.data,email=self.email.data,password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user
