from app.admin import bp
from flask import (render_template, flash, url_for,
                   session, current_app, redirect)
from app.admin.forms import AdminLoginForm, SAMLSettingsForm
from app.models import SAMLsettings
from app import db


@bp.route('/admin/', methods=['GET', 'POST'])
def index():
    form = AdminLoginForm()
    if form.validate_on_submit():
        if form.admintoken.data == current_app.config['ADMIN_KEY']:
            session['isAdmin'] = True
            flash('Login succesful', 'success')
        else:
            flash('Invalid password', 'danger')

    return render_template(
        'admin/index.html',
        form=form
    )


@bp.route('/admin/saml', methods=['GET', 'POST'])
def saml():
    if session.get('isAdmin', False) is False:
        return redirect(url_for('admin.index'))

    dbsettings = SAMLsettings.query.filter_by(id=1).first()
    form = SAMLSettingsForm(obj=dbsettings)

    if form.validate_on_submit():
        form.populate_obj(dbsettings)
        db.session.add(dbsettings)
        db.session.commit()
        flash('SAML settings have been updated.', 'success')
        return redirect(url_for('admin.saml'))

    return render_template(
        'admin/saml.html',
        form=form
    )


@bp.route('/admin/logout', methods=['GET', 'POST'])
def logout():
    session['isAdmin'] = False
    return redirect(url_for('admin.index'))
