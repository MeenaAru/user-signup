from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too
@app.route("/welcome", methods=['post'])
def user_signup():

    name= request.form['user_name']
    pword= request.form['passwrd']
    vpword= request.form['vrfy_passwrd']
    email= request.form['email']
    if name =='':
        nmerror = "Please specify the username."
        return redirect("/?nmerror=" + nmerror)
    else:
        if len(name) < 3 or len(name) > 20:
            nmerror = "Name should contain more than 3 and less than 20 characters."
            return redirect("/?nmerror=" + nmerror)
        if  ' ' in name:
            nmerror = "Name should not contain spaces"
            return redirect("/?nmerror=" + nmerror)
        
    if pword=='':
        pwerror = "Not a valid password."
        return redirect("/?pwerror="+ pwerror +"&name=" +name )
    else:
        pwerror=''
        if len(pword) < 3 or len(pword) > 20:
            pwerror = "Password should contain more than 3 and less than 20 characters."
        if  ' ' in pword:
            pwerror = "Password should not contain spaces."
        if pwerror!='':
            return redirect("/?pwerror=" + pwerror +"&name=" +name )

    if pword != vpword :
        vpwerror = "Password doesn't match."
        return redirect("/?vpwerror=" + vpwerror+"&name=" +name)
    if email !='':
        emerror=''
        if len(email) < 3 or len(email) > 30:
            emerror = "Email should contain more than 3 and less than 30 characters."
        if '@' not in email or '.' not in email or ' ' in email:
            emerror = "Should be a valid email."
        if emerror!='':
            return redirect("/?emerror=" + emerror +"&name=" +name)
    
    return render_template('welcome.html',user_name=name)

@app.route("/")
def index():
    nm_error = request.args.get("nmerror")
    pw_error = request.args.get("pwerror")
    vpw_error = request.args.get("vpwerror")
    em_error = request.args.get("emerror")
    name = request.args.get("name")
    if not name:
        name=''
    return render_template('signup.html',nmerror=nm_error ,pwerror=pw_error,vpwerror=vpw_error,emerror=em_error,name=name)

app.run()


