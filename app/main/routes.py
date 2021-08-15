from app.main import bp
from flask import (render_template, redirect, session)


@bp.route('/', methods=['GET', 'POST'])
def index():
    if session.get('samlNameId', None) is None:
        return redirect('/auth/?sso', code=307)

    displayname = 'http://schemas.microsoft.com/identity/claims/displayname'
    if session.get('samlUserdata', None) is not None:
        if len(session['samlUserdata']) > 0:
            if session['samlUserdata'].get(displayname, None) is not None:
                username = session['samlUserdata'].get(displayname)[0]
            else:
                username = session.get('samlNameId')

    return render_template(
        'index.html',
        username=username
    )
