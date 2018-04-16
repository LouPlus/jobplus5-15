from flask import Blueprint,render_template,flash,redirect,url_for
from flask_login import login_required,current_user
from jobplus.forms import UserProfileForm
