#cria os formularios do site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import Usuario

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    senha = PasswordField("Senha",validators=[DataRequired()])
    botao_confirmacao= SubmitField("Fazer Login")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if not usuario:
            raise ValidationError("Este usuario nao existe, crie uma conta para continuar")



class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuario",validators=[DataRequired()])
    senha = PasswordField("Senha",validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField("Confirmacao de Senha", validators=[DataRequired(), EqualTo("senha")])
    botao_confirmacao = SubmitField("Criar Conta")

    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError("E-mail ja cadastrado, faca login para continuar")


class FormPhoto(FlaskForm):
    photo = FileField("Photo",validators=[DataRequired()])
    botao_confirmacao = SubmitField("Enviar")