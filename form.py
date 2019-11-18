from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SelectField,DateTimeField
from wtforms.validators import DataRequired,Length,Email,EqualTo




class RegistrationForm(FlaskForm):
   username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
   email=StringField('Email',validators=[DataRequired(),Email()])
   password=PasswordField('Password',validators=[DataRequired()])
   confirm_password=PasswordField('Confirm_Password ',validators=[DataRequired(),EqualTo('password')])

   submit=SubmitField('Sign Up')


class LoginForm(FlaskForm):
   
   email=StringField('Email',validators=[DataRequired(),Email()])
   password=PasswordField('Password',validators=[DataRequired()])
   remember=BooleanField('Remember Me')
   submit=SubmitField('Login') 


class UserForm(FlaskForm):
  	name=StringField('full name',validators=[DataRequired(),name(),Length(min=2,max=20)])
 	title=StringField('title',validataors=[DataRequried(),title()])
    FirstName=StringField('FirstName',validators=[DataRequried(),Length(min=2,max=20)])
    middlename=StringField('MiddleName',validators=[DataRequried(),Length(min=2,max=10)])
    Lastname=StringField('LastName',validators=[DataRequried(),Length(min=2,max=10)])
    suffix=StringField('SuffixName',validators=[DataRequried(),Length(min=2,max=15)])
    nickname=StringField('NickName',validators=[DataRequried(),Length(min=2,max=20)])
    birthday= DateTimeField('Your Birthday', format='%m/%d/%y')
    gender=SelectField('', choices=['male','female'])
    company=StringField('company',validators=[DataRequried(),company()])
    department=StringField('department',validators=[DataRequried(),department()]
    job title=StringField('department',validators=[DataRequried(),jobtitle()]
    business fax=StringField('business fax')
    mobile =FormField(TelephoneForm)
    email=StringField('Email',validators=[DataRequired(),Email()]
    business Adress=StringField('business Adress',validators=[DataRequired(),business adress()]
    website business phone=StringField()
    personal website=StringField()
    home phone=TextField(TelephoneForm)
    home fax=TextField(home fax_TelephoneForm)
    home adress=StringField('home Adress',validators=[DataRequired(),home adress()]
    street=StringField('Street name/no.',validators=[DataRequired(),street adress()]
    city=StringField('City name',validators=[DataRequired(),city name()]
    state=StringField('statename','state_code',validators=[DataRequired(),business adress()]
    postal code=StringField('postalcode',validators=[DataRequired(),business adress()]
    country Region= IntegerField('/Exchange', [validators.required()])
   


class TelephoneForm(Form):
	country_code = IntegerField('Country Code', [validators.required()])
    area_code    = IntegerField('Area Code/Exchange', [validators.required()])
    number       = StringField('Number')

class ContactForm(Form):
    first_name   = StringField()
    last_name    = StringField()
    mobile_phone = FormField(TelephoneForm)
    office_phone = FormField(TelephoneForm)
