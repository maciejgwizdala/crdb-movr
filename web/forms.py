"""
Defines forms used by various web pages.

Each class is a form.
"""

from flask_wtf import FlaskForm
from wtforms import (DecimalField, IntegerField, StringField, SubmitField,
                     SelectField)
from wtforms.validators import data_required, input_required, number_range


class LoginForm(FlaskForm):
    """Login form class.
    """
    email = StringField('Email: ', validators=[data_required()])
    submit = SubmitField('Sign In')


class StartRideForm(FlaskForm):
    """
    Creates a "Start ride" button.
    """
    submit = SubmitField('Start ride')


class ViewRideForm(FlaskForm):
    """Creates a 'View Ride' button"""
    submit=SubmitField('View ride')


class EndRideForm(FlaskForm):
    """
    End ride form for the user to fill out.
    """
    longitude = DecimalField(label='Longitude', validators=[
        input_required(),
        number_range(min=-180, max=180,
                     message="Longitude must be between -180 and 180.")])
    latitude = DecimalField(label='Latitude', validators=[
        input_required(),
        number_range(min=-90, max=90,
                     message="Latitude must be between -90 and 90.")])
    battery = IntegerField(label='Battery (percent)', validators=[
        input_required(),
        number_range(min=0, max=100,
                     message="Battery (percent) must be between 0 and 100.")])
    submit = SubmitField('End ride')


class SeeVehicleForm(FlaskForm):
    """
    Button to see information on a single vehicle.
    """
    submit = SubmitField('See Vehicle')


class VehicleForm(FlaskForm):
    """
    Register a new vehicle.
    """
    vehicle_type = SelectField(label='Type',
                       choices=[('bike', 'Bike'), ('scooter', 'Scooter'),
                                ('skateboard', 'Skateboard')])
    longitude = DecimalField(label='Longitude', validators=[
        input_required(),
        number_range(min=-180, max=180,
                     message="Longitude must be between -180 and 180.")])
    latitude = DecimalField(label='Latitude', validators=[
        input_required(),
        number_range(min=-90, max=90,
                     message="Latitude must be between -90 and 90.")])
    battery = IntegerField(label='Battery (percent)', validators=[
        input_required(),
        number_range(min=0, max=100,
                     message="Battery (percent) must be between 0 and 100.")])
    color = StringField(label="Color", validators=[input_required()])
    manufacturer = StringField(label="Manufacturer", validators=[])
    serial_number = StringField(label="Serial Number", validators=[])
    vehicle_wear = StringField(label="Vehicle Wear", validators=[])
    purchase_date = StringField(label="Purchase Date", validators=[])
    submit = SubmitField('Add vehicle')


class RemoveVehicleForm(FlaskForm):
    """
    Button to delete a vehicle.
    """
    submit = SubmitField('Remove vehicle')


class RegisterForm(FlaskForm):
    """User registration form class.
    """
    email = StringField('Email', validators=[data_required()])
    first_name = StringField('First name: ', validators=[data_required()])
    last_name = StringField('Last name: ', validators=[data_required()])
    phone_number = StringField('Phone number*', validators=[])
    submit = SubmitField('Register')


class DeletePhoneNumber(FlaskForm):
    """
    Deletes a phone number.
    """
    submit = SubmitField('Remove phone number')


class RemoveUserForm(FlaskForm):
    """Remove user form class.
    """
    submit = SubmitField('Delete my account')
