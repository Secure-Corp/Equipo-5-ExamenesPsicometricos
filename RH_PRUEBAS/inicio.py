from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')

def home():
    return render_template("home.html")

#area
@app.route('/area')
def area():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area order by idArea')
    datos = cursor.fetchall()
    return render_template("area.html", comentarios = datos)

@app.route('/area_editar/<string:id>')
def area_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area where idArea = %s', (id))
    dato  = cursor.fetchone()
    return render_template("area_edi.html", comentar=dato)

@app.route('/area_fedita/<string:id>',methods=['POST'])
def area_fedita(id):
    if request.method == 'POST':
        desc=request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update area set descripcion=%s where idArea=%s', (desc,id))
        conn.commit()
    return redirect(url_for('area'))

@app.route('/area_borrar/<string:id>')
def area_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from area where idArea = {0}'.format(id))
    conn.commit()
    return redirect(url_for('area'))

@app.route('/area_agregar')
def area_agregar():
    return render_template("area_agr.html")

@app.route('/area_fagrega', methods=['POST'])
def area_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
        cursor = conn.cursor()
        cursor.execute('insert into area (descripcion) values (%s)',(desc))
        conn.commit()
    return redirect(url_for('area'))

#carrera

@app.route('/carrera')
def carrera():
    conn=pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor=conn.cursor()
    cursor.execute('select idCarrera, descripcion from carrera order by idCarrera')
    datos = cursor.fetchall()
    return render_template('carrera.html', comentarios=datos)

@app.route('/carrera_agregar')
def carrera_agregar():
    return render_template('carrera_agr.html')

@app.route('/carrera_fagrega', methods=['POST'])
def carrera_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn=pymysql.connect(host="localhost", user="root", passwd="", db="rh3")
        cursor= conn.cursor()
        cursor.execute("INSERT INTO carrera (descripcion) values (%s)",(desc) )
        conn.commit()
    return redirect(url_for("carrera"))

@app.route('/carrera_editar/<string:id>')
def carrera_editar(id):
    conn =pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor=conn.cursor()
    cursor.execute('select idCarrera, descripcion from carrera where idCarrera=%s', (id))
    dato=cursor.fetchone()
    return render_template('carrera_edi.html', comentar=dato)

@app.route('/carrera_fedita/<string:id>', methods=['POST'])
def carrera_fedita(id):
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute("update carrera set descripcion=%s where idCarrera=%s", (desc, id))
        conn.commit()
    return redirect(url_for('carrera'))

@app.route('/carrera_borrar/<string:id>')
def carrera_borrar(id):
    conn= pymysql.connect(host="Localhost", user="root", passwd="", db="rh3")
    cursor=conn.cursor()
    cursor.execute("delete from carrera where idCarrera = {0}".format(id))
    conn.commit()
    return redirect(url_for("carrera"))

#escolaridad

@app.route('/escolaridad')
def escolaridad():
    conn=pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor=conn.cursor()
    cursor.execute('select idEscolaridad, descripcion from escolaridad order by idEscolaridad')
    datos = cursor.fetchall()
    return render_template('escolaridad.html', comentarios=datos)

@app.route("/escolaridad_agregar")
def escolaridad_agregar():
    return render_template('escolaridad_agr.html')

@app.route("/escolaridad_fagrega", methods=['POST'])
def escolaridad_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn=pymysql.connect(host="localhost", user="root", passwd="", db="rh3")
        cursor= conn.cursor()
        cursor.execute("insert into escolaridad (descripcion) values (%s)", (desc))
        conn.commit()
    return redirect(url_for("escolaridad"))

@app.route('/escolaridad_editar/<string:id>')
def escolaridad_editar(id):
    conn =pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor=conn.cursor()
    cursor.execute('select idEscolaridad, descripcion from escolaridad where idEscolaridad=%s', (id)) 
    dato=cursor.fetchone()
    return render_template('escolaridad_edi.html', comentar=dato)

@app.route('/escolaridad_fedita/<string:id>', methods=['POST'])
def escolaridad_fedita(id):
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute("update escolaridad set descripcion=%s where idEscolaridad=%s", (desc, id))
        conn.commit()
    return redirect(url_for("escolaridad"))

@app.route('/escolaridad_borrar/<string:id>')
def escolaridad_borrar(id):
    conn= pymysql.connect(host="Localhost", user="root", passwd="", db="rh3")
    cursor=conn.cursor()
    cursor.execute("delete from escolaridad where idEscolaridad = {0}".format(id))
    conn.commit()
    return redirect(url_for("escolaridad"))

#estado civil

@app.route('/estado')
def estado():
    conn=pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor=conn.cursor()
    cursor.execute('select idEstadoCivil, descripcion from estado_civil order by idEstadoCivil')
    datos = cursor.fetchall()
    return render_template('estado.html', comentarios=datos)

@app.route("/estado_agregar")
def estado_agregar():
    return render_template('estado_ag.html')

@app.route("/estado_fagrega", methods=['POST'])
def estado_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn=pymysql.connect(host="localhost", user="root", passwd="", db="rh3")
        cursor= conn.cursor()
        cursor.execute("insert into estado_civil (descripcion) values (%s)", (desc))
        conn.commit()
    return redirect(url_for("estado"))

@app.route('/estado_editar/<string:id>')
def estado_editar(id):
    conn =pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor=conn.cursor()
    cursor.execute('select idEstadoCivil, descripcion from estado_civil where idEstadoCivil=%s', (id))
    dato=cursor.fetchone()
    return render_template('estado_edi.html', comentar=dato)

@app.route('/estado_fedita/<string:id>', methods=['POST'])
def estado_fedita(id):
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update estado_civil set descripcion=%s where idEstadoCivil=%s', (desc, id))
        conn.commit()
    return redirect(url_for('estado'))

@app.route('/estado_borrar/<string:id>')
def estado_borrar(id):
    conn= pymysql.connect(host="Localhost", user="root", passwd="", db="rh3")
    cursor=conn.cursor()
    cursor.execute('delete from estado_civil where idEstadoCivil={0}'.format(id))
    conn.commit()
    return redirect(url_for('estado'))

#Grado de avance

@app.route('/grado')
def grado():
    conn=pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor=conn.cursor()
    cursor.execute('select idGradoAvance, descripcion from grado_avance order by idGradoAvance')
    datos = cursor.fetchall()
    return render_template('grado.html', comentarios=datos)

@app.route('/grado_agregar')
def grado_agregar():
    return render_template('grado_ag.html')

@app.route('/grado_fagrega', methods=['POST'])
def grado_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn=pymysql.connect(host="localhost", user="root", passwd="", db="rh3")
        cursor= conn.cursor()
        cursor.execute("insert into grado_avance (descripcion) values (%s)", (desc))
        conn.commit()
    return redirect(url_for("grado"))

@app.route("/grado_editar/<string:id>")
def grado_editar(id):
    conn =pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor=conn.cursor()
    cursor.execute('select idGradoAvance, descripcion from grado_avance where idGradoAvance=%s', (id))
    dato=cursor.fetchone()
    return render_template("grado_edi.html", comentar=dato)

@app.route('/grado_fedita/<string:id>', methods=['POST'])
def grado_fedita(id):
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update grado_avance set descripcion=%s where idGradoAvance=%s', (desc, id))
        conn.commit()
    return redirect(url_for('grado'))

@app.route('/grado_borrar/<string:id>')
def grado_borrar(id):
    conn= pymysql.connect(host="Localhost", user="root", passwd="", db="rh3")
    cursor=conn.cursor()
    cursor.execute('delete from grado_avance where idGradoAvance={0}'.format(id))
    conn.commit()
    return redirect(url_for('grado'))

#Habilidades

@app.route('/habilidades')
def habilidades():
    conn=pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor=conn.cursor()
    cursor.execute('select idHabilidad, descripcion from habilidad order by idHabilidad')
    datos = cursor.fetchall()
    return render_template('hablidades.html', comentar=datos)

@app.route('/habilidades_agregar')
def habilidades_agregar():
    return render_template('habilidades_ag.html')

@app.route('/habilidades_fagrega', methods=['POST'])
def habilidades_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn=pymysql.connect(host="localhost", user="root", passwd="", db="rh3")
        cursor= conn.cursor()
        cursor.execute("insert into habilidad (descripcion) values (%s)", (desc))
        conn.commit()
    return redirect(url_for("habilidades"))

@app.route("/habilidades_editar/<string:id>")
def habilidades_editar(id):
    conn =pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor=conn.cursor()
    cursor.execute('select idHabilidad, descripcion from habilidad where idHabilidad=%s',(id))
    dato=cursor.fetchone()
    return render_template("habilidades_edi.html", comentar=dato)

@app.route('/habilidades_fedita/<string:id>', methods=['POST'])
def habilidades_fedita(id):
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update habilidad set descripcion=%s where idHabilidad=%s', (desc, id))
        conn.commit()
    return redirect(url_for('habilidades'))

@app.route('/habilidades_borrar/<string:id>')
def habilidades_borrar(id):
    conn= pymysql.connect(host="Localhost", user="root", passwd="", db="rh3")
    cursor=conn.cursor()
    cursor.execute('delete from habilidad where idHabilidad={0}'.format(id))
    conn.commit()
    return redirect(url_for('habilidades'))

#Idiomas

@app.route('/idioma')
def idioma():
    conn=pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor=conn.cursor()
    cursor.execute('select idIdioma, descripcion from idioma order by idIdioma')
    datos = cursor.fetchall()
    return render_template('idioma.html', comentarios=datos)

@app.route('/idioma_agregar')
def idioma_agregar():
    return render_template('idioma_ag.html')

@app.route('/idioma_fagrega', methods=['POST'])
def idioma_fagrega():
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn=pymysql.connect(host="localhost", user="root", passwd="", db="rh3")
        cursor= conn.cursor()
        cursor.execute("insert into idioma (descripcion) values (%s)", (desc))
        conn.commit()
    return redirect(url_for("idioma"))

@app.route("/idioma_editar/<string:id>")
def idioma_editar(id):
    conn =pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor=conn.cursor()
    cursor.execute('select idIdioma, descripcion from idioma where idIdioma=%s', (id))
    dato=cursor.fetchone()
    return render_template("idioma_edi.html", comentar=dato)

@app.route('/idioma_fedita/<string:id>', methods=['POST'])
def idioma_fedita(id):
    if request.method == 'POST':
        desc = request.form['descripcion']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('update idioma set descripcion=%s where idIdioma=%s', (desc, id))
        conn.commit()
    return redirect(url_for('idioma'))

@app.route('/idioma_borrar/<string:id>')
def idioma_borrar(id):
    conn= pymysql.connect(host="Localhost", user="root", passwd="", db="rh3")
    cursor=conn.cursor()
    cursor.execute('delete from idioma where idIdioma={0}'.format(id))
    conn.commit()
    return redirect(url_for('idioma'))

@app.route('/puesto')
def puesto():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3' )
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    return render_template("puesto.html", pue = datos, dat='   ', catArea = '   ', catEdoCivil = '   ', catEscolaridad = '   ',
                           catGradoAvance = '    ', catCarrera = '    ', catIdioma = ' ', catHabilidad = ' ')


@app.route('/puesto_fdetalle/<string:idP>', methods=['GET'])
def puesto_fdetalle(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto, nomPuesto from puesto order by idPuesto')
    datos = cursor.fetchall()

    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
            'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
            'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
    datos1 = cursor.fetchall()

    cursor.execute('select a.idEstadoCivil, a.descripcion from estado_civil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s', (idP))
    datos2 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s', (idP))
    datos3 = cursor.fetchall()

    cursor.execute('select a.idGradoAvance, a.descripcion from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s', (idP))
    datos4 = cursor.fetchall()

    cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idP))
    datos5 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos6 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
    datos7 = cursor.fetchall()
    return render_template("puesto.html", pue = datos, dat=dato[0], catArea=datos1[0], catEdoCivil=datos2[0], catEscolaridad=datos3[0],
                           catGradoAvance=datos4[0], catCarrera=datos5[0], catIdioma=datos6, catHabilidad=datos7)

@app.route('/puesto_borrar/<string:idP>')
def puesto_borrar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('delete from puesto where idPuesto = %s',(idP))
    conn.commit()
    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
    conn.commit()
    return redirect(url_for('puesto'))


@app.route('/puesto_agrOp2')
def puesto_agrOp2():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute('select idIdioma, descripcion from idioma ')
    datos6 = cursor.fetchall()

    cursor.execute('select idHabilidad, descripcion from habilidad ')
    datos7 = cursor.fetchall()

    return render_template("puesto_agrOp2.html", catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                           catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7)


@app.route('/puesto_fagrega2', methods=['POST'])
def puesto_fagrega():
    if request.method == 'POST':

        if  'idArea' in request.form:
            idAr = request.form['idArea']
        else:
            idAr = '1'
        if 'idEstadoCivil' in request.form:
            idEC = request.form['idEstadoCivil']
        else:
            idEC = '1'
        if 'idEscolaridad' in request.form:
            idEs = request.form['idEscolaridad']
        else:
            idEs = '1'
        if 'idGradoAvance' in request.form:
            idGA = request.form['idGradoAvance']
        else:
            idGA = '1'
        if 'idCarrera' in request.form:
            idCa = request.form['idCarrera']
        else:
            idCa = '1'
        if 'sexo' in request.form:
            sex = request.form['sexo']
        else:
            sex = '1'
        codP = request.form['codPuesto']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']


    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute(
    'insert into puesto (codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
    'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
    'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
    (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda, sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF,
     reqP, resp, conT))
    conn.commit()

    cursor.execute('select idPuesto from puesto where idPuesto=(select max(idPuesto) from puesto) ')
    dato = cursor.fetchall()
    idpue = dato[0]
    idP = idpue[0]

    cursor.execute('select count(*) from idioma ')
    dato = cursor.fetchall()
    nidio = dato[0]
    ni = nidio[0] + 1

    for i in range(1, ni):
        idio = 'i' + str(i)
        if idio in request.form:
            cursor.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,%s)', (idP, i))
            conn.commit()

    cursor.execute('select count(*) from habilidad ')
    dato = cursor.fetchall()
    nhab = dato[0]
    nh =nhab[0]+1

    for i in range(1,nh):
        habi = 'h' + str(i)
        if habi in request.form:
            cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)', (idP,i))
            conn.commit()

    return redirect(url_for('puesto'))



@app.route('/puesto_editar/<string:idP>')
def puesto_editar(idP):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idPuesto,codPuesto,idArea,nomPuesto,puestoJefeSup,jornada,remunMensual,prestaciones,descripcionGeneral,'
        'funciones,edad,sexo,idEstadoCivil,idEscolaridad,idGradoAvance,idCarrera,experiencia,conocimientos,manejoEquipo,'
        'reqFisicos,reqPsicologicos,responsabilidades,condicionesTrabajo from puesto where idPuesto = %s', (idP))
    dato = cursor.fetchall()

    cursor.execute('select idArea, descripcion from area ')
    datos1 = cursor.fetchall()

    cursor.execute('select idEstadoCivil, descripcion from estado_civil ')
    datos2 = cursor.fetchall()

    cursor.execute('select idEscolaridad, descripcion from escolaridad ')
    datos3 = cursor.fetchall()

    cursor.execute('select idGradoAvance, descripcion from grado_avance ')
    datos4 = cursor.fetchall()

    cursor.execute('select idCarrera, descripcion from carrera ')
    datos5 = cursor.fetchall()

    cursor.execute('select idIdioma, descripcion from idioma ')
    datos6 = cursor.fetchall()

    cursor.execute('select idHabilidad, descripcion from habilidad ')
    datos7 = cursor.fetchall()

    cursor.execute('select a.idArea, a.descripcion from area a, puesto b where a.idArea = b.idArea and b.idPuesto = %s', (idP))
    datos11 = cursor.fetchall()

    cursor.execute('select a.idEstadoCivil, a.descripcion from estado_civil a, puesto b where a.idEstadoCivil = b.idEstadoCivil and b.idPuesto = %s',(idP))
    datos12 = cursor.fetchall()

    cursor.execute('select a.idEscolaridad, a.descripcion from escolaridad a, puesto b where a.idEscolaridad = b.idEscolaridad and b.idPuesto = %s',(idP))
    datos13 = cursor.fetchall()

    cursor.execute('select a.idGradoAvance, a.descripcion from grado_avance a, puesto b where a.idGradoAvance = b.idGradoAvance and b.idPuesto = %s',(idP))
    datos14 = cursor.fetchall()

    cursor.execute('select a.idCarrera, a.descripcion from carrera a, puesto b where a.idCarrera = b.idCarrera and b.idPuesto = %s', (idP))
    datos15 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idIdioma, b.descripcion from puesto a, idioma b, puesto_has_idioma c '
                   'where a.idPuesto = c.idPuesto and b.idIdioma = c.idIdioma and a.idPuesto = %s', (idP))
    datos16 = cursor.fetchall()

    cursor.execute('select a.idPuesto, b.idHabilidad, b.descripcion from puesto a, habilidad b, puesto_has_habilidad c '
                   'where a.idPuesto = c.idPuesto and b.idHabilidad = c.idHabilidad and a.idPuesto = %s', (idP))
    datos17 = cursor.fetchall()


    return render_template("puesto_edi.html", dat=dato[0], catArea=datos1, catEdoCivil=datos2, catEscolaridad=datos3,
                           catGradoAvance=datos4, catCarrera=datos5, catIdioma=datos6, catHabilidad=datos7,
                           Area=datos11[0], EdoCivil=datos12[0], Escolaridad=datos13[0], GradoAvance=datos14[0],
                           Carrera=datos15[0], Idioma=datos16, Habilidad=datos17)


@app.route('/puesto_fedita/<string:idP>', methods=['POST'])
def puesto_fedita(idP):
    if request.method == 'POST':
        codP = request.form['codPuesto']
        idAr = request.form['idArea']
        nomP = request.form['nomPuesto']
        pueJ = request.form['puestoJefeSup']
        jorn = request.form['jornada']
        remu = request.form['remunMensual']
        pres = request.form['prestaciones']
        desc = request.form['descripcionGeneral']
        func = request.form['funciones']
        eda = request.form['edad']
        sex = request.form['sexo']
        idEC = request.form['idEstadoCivil']
        idEs = request.form['idEscolaridad']
        idGA = request.form['idGradoAvance']
        idCa = request.form['idCarrera']
        expe = request.form['experiencia']
        cono = request.form['conocimientos']
        manE = request.form['manejoEquipo']
        reqF = request.form['reqFisicos']
        reqP = request.form['reqPsicologicos']
        resp = request.form['responsabilidades']
        conT = request.form['condicionesTrabajo']

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('update puesto set codPuesto = %s, idArea = %s, nomPuesto = %s, puestoJefeSup = %s, jornada = %s, '
                   'remunMensual = %s, prestaciones = %s, descripcionGeneral = %s, funciones = %s, edad = %s, sexo = %s, '
                   'idEstadoCivil = %s, idEscolaridad = %s, idGradoAvance = %s, idCarrera = %s, experiencia = %s, '
                   'conocimientos = %s, manejoEquipo = %s, reqFisicos = %s, reqPsicologicos = %s, responsabilidades = %s, '
                   'condicionesTrabajo = %s where idPuesto = %s', (codP, idAr, nomP, pueJ, jorn, remu, pres, desc, func, eda,
                   sex, idEC, idEs, idGA, idCa, expe, cono, manE, reqF, reqP, resp, conT, idP))
    conn.commit()
    cursor.execute('delete from puesto_has_habilidad where idPuesto =%s ', (idP))
    conn.commit()
    cursor.execute('delete from puesto_has_idioma where idPuesto =%s ', (idP))
    conn.commit()

    cursor.execute('select count(*) from idioma ')
    dato = cursor.fetchall()
    nidio = dato[0]
    ni = nidio[0] + 1

    for i in range(1, ni):
        idio = 'i' + str(i)
        if idio in request.form:
            cursor.execute('insert into puesto_has_idioma(idPuesto,idIdioma) values (%s,%s)', (idP, i))
            conn.commit()

    cursor.execute('select count(*) from habilidad ')
    dato = cursor.fetchall()
    nhab = dato[0]
    nh = nhab[0] + 1

    for i in range(1, nh):
        habi = 'h' + str(i)
        if habi in request.form:
            cursor.execute('insert into puesto_has_habilidad(idPuesto,idHabilidad) values (%s,%s)', (idP, i))
            conn.commit()
    return redirect(url_for('puesto'))

#requisicion

@app.route('/requisicion')
def requisicion():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idRequisicion, motivoRequisicion from requisicion order by idRequisicion')
    datos = cursor.fetchall()
    return render_template("requisicion.html", req=datos, folio="", elab="", recluta="", inicvac="",
                           motivo="", motes="", tipo="", nomsoli="", nomauto="", nomrevi="")

@app.route('/requisicion_fdetalle/<string:id>', methods=['GET'])
def requisicion_fdetalle(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idRequisicion, motivoRequisicion from requisicion order by idRequisicion')
    datos = cursor.fetchall()

    cursor.execute('select folio from requisicion where idRequisicion= %s', (id))
    dato1 = cursor.fetchone()

    cursor.execute('select fechaElab from requisicion where idRequisicion= %s', (id))
    dato2 = cursor.fetchone()
    
    cursor.execute('select fechaRecluta from requisicion where idRequisicion= %s', (id))
    dato3 = cursor.fetchone()
    
    cursor.execute('select fechaInicVac from requisicion where idRequisicion= %s', (id))
    dato4 = cursor.fetchone()
    
    cursor.execute('select motivoRequisicion from requisicion where idRequisicion= %s', (id))
    dato5 = cursor.fetchone()
    
    cursor.execute('select motivoEspecifique from requisicion where idRequisicion= %s', (id))
    dato6 = cursor.fetchone()
    
    cursor.execute('select tipoVacante from requisicion where idRequisicion= %s', (id))
    dato7 = cursor.fetchone()
    
    cursor.execute('select nomSolicita from requisicion where idRequisicion= %s', (id))
    dato8 = cursor.fetchone()
    
    cursor.execute('select nomAutoriza from requisicion where idRequisicion= %s', (id))
    dato9 = cursor.fetchone()
    
    cursor.execute('select nomRevisa from requisicion where idRequisicion= %s', (id))
    dato10 = cursor.fetchone()
    
    cursor.execute('select idPuesto from requisicion where idRequisicion= %s', (id))
    dato11 = cursor.fetchone()
    
    cursor.execute('select idArea from requisicion where idRequisicion= %s', (id))
    dato12 = cursor.fetchone()
    return render_template("requisicion.html", req=datos, folio=dato1, elab=dato2, recluta=dato3, inicvac=dato4,
                           motivo=dato5, motes=dato6, tipo=dato7, nomsoli=dato8, nomauto=dato9, nomrevi=dato10)

@app.route('/requisicion_fedita/<string:id>')
def requisicion_editar(id): 
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idRequisicion, motivoRequisicion from requisicion order by idRequisicion')
    datos = cursor.fetchall()

    cursor.execute('select folio from requisicion where idRequisicion= %s', (id))
    dato1 = cursor.fetchone()

    cursor.execute('select fechaElab from requisicion where idRequisicion= %s', (id))
    dato2 = cursor.fetchone()
    
    cursor.execute('select fechaRecluta from requisicion where idRequisicion= %s', (id))
    dato3 = cursor.fetchone()
    
    cursor.execute('select fechaInicVac from requisicion where idRequisicion= %s', (id))
    dato4 = cursor.fetchone()
    
    cursor.execute('select motivoRequisicion from requisicion where idRequisicion= %s', (id))
    dato5 = cursor.fetchone()
    
    cursor.execute('select motivoEspecifique from requisicion where idRequisicion= %s', (id))
    dato6 = cursor.fetchone()
    
    cursor.execute('select tipoVacante from requisicion where idRequisicion= %s', (id))
    dato7 = cursor.fetchone()
    
    cursor.execute('select nomSolicita from requisicion where idRequisicion= %s', (id))
    dato8 = cursor.fetchone()
    
    cursor.execute('select nomAutoriza from requisicion where idRequisicion= %s', (id))
    dato9 = cursor.fetchone()
    
    cursor.execute('select nomRevisa from requisicion where idRequisicion= %s', (id))
    dato10 = cursor.fetchone()
    
    cursor.execute('select idPuesto from requisicion where idRequisicion= %s', (id))
    dato11 = cursor.fetchone()
    
    cursor.execute('select idArea from requisicion where idRequisicion= %s', (id))
    dato12 = cursor.fetchone()
    return render_template("requisicion_edi.html", req=datos, folio=dato1, elab=dato2, recluta=dato3, inicvac=dato4,
                           motivo=dato5, motes=dato6, tipo=dato7, nomsoli=dato8, nomauto=dato9, nomrevi=dato10)


@app.route('/requisicion_fedita2/<string:id>', methods=['POST'])
def requisicion_fedita(id):
    if request.method == 'POST':
        folio = request.form['folio']
        elab = request.form['fechaElab']
        recluta = request.form['fechaRecluta']
        inicvac = request.form['fechaInicVac']
        motivo = request.form['motivoRequisicion']
        motes = request.form['motivoEspesifique']
        tipo = request.form['tipoVacante']
        nomsoli = request.form['nomSolicita']
        nomauto = request.form['nomAutoriza']
        nomrevi = request.form['nomRevisa']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE requisicion SET folio = %s, fechaElab = %s, fechaRecluta = %s, fechaInicVac=%s,'
            'motivoRequisicion=%s, motivoEspecifique=%s, tipoVacante=%s, nomSolicita=%s,'
            'nomAutoriza=%s, nomRevisa=%s WHERE idRequisicion=%s',(folio, elab, recluta, inicvac,
            motivo, motes, tipo, nomsoli, nomauto, nomrevi, id))
        conn.commit()
    return redirect(url_for('requisicion'))

@app.route('/requisicion_agrega2')
def requisicion_agrOp2():
    return render_template("requisicion_agrOp2.html")

@app.route('/requisicion_fagrega2', methods=['POST'])
def requisicion_fagrega():
    if request.method == 'POST':
        folio = request.form['folio']
        elab = request.form['fechaElab']
        recluta = request.form['fechaRecluta']
        inicvac = request.form['fechaInicVac']
        motivo = request.form['motivoRequisicion']
        motes = request.form['motivoEspesifique']
        tipo = request.form['tipoVacante']
        nomsoli = request.form['nomSolicita']
        nomauto = request.form['nomAutoriza']
        nomrevi = request.form['nomRevisa']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO requisicion (folio, fechaElab, fechaRecluta, fechaInicVac, motivoRequisicion,'
            'motivoEspecifique, tipoVacante, nomSolicita, nomAutoriza, nomRevisa)'
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (folio, elab, recluta, inicvac, motivo, motes, tipo, nomsoli, nomauto, nomrevi))
        conn.commit()
        return redirect(url_for('requisicion'))
    
@app.route('/requisicion_borrar/<string:req>')
def requisicion_borrar(req):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM requisicion WHERE idRequisicion = %s', (req,))
    conn.commit()
    return redirect(url_for('requisicion'))

#vacante
@app.route('/vacantes')
def vacantes():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('SELECT idVacante, fuenteCandidato FROM vacante ORDER BY idVacante')
    datos = cursor.fetchall()
    return render_template("vacantes.html", vac=datos, NomP=" ", FuenteC=" ", FechaP=" ", FechaE=" ",
                           Pub=" ", Obs=" ", tipo=" ", SeleC=" ", FechaC=" ", idRe=" ",idPu=" ")

@app.route('/vacantes_fdetalle/<string:id>', methods=['GET'])
def vacante_fdetalle(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()

    cursor.execute('select idVacante, fuenteCandidato from vacante order by idVacante')
    dato = cursor.fetchall()

    cursor.execute('select fuenteCandidato from vacante where idVacante = %s', (id))
    dato1 = cursor.fetchone()

    cursor.execute('select inicioFechaPublic from vacante where idVacante = %s', (id))
    dato2 = cursor.fetchone()

    cursor.execute('select finFechaPublic from vacante where idVacante = %s', (id))
    dato3 = cursor.fetchone()

    cursor.execute('select publicada from vacante where idVacante = %s', (id))
    dato4 = cursor.fetchone()

    cursor.execute('select  observaciones from vacante where idVacante = %s', (id))
    dato5 = cursor.fetchone()

    cursor.execute('select  candidatoSelecc from vacante where idVacante = %s', (id))
    dato6 = cursor.fetchone()

    cursor.execute('select  fechaContratacion from vacante where idVacante = %s', (id))
    dato7 = cursor.fetchone()

    cursor.execute('select idRequisicion from vacante where idVacante = %s', (id))
    dato8 = cursor.fetchone()

    cursor.execute('select  idPuesto from vacante where idVacante = %s', (id))
    dato9 = cursor.fetchone()
    
    return render_template("vacantes.html", vac=dato, FuenteC=dato1, FechaP=dato2, FechaE=dato3,
                           Pub=dato4, Obs=dato5, SeleC=dato6, FechaC=dato7, idRe=dato8, idPu=dato9)

@app.route('/vacante_agrega2')
def vacante_agrOp2():
    return render_template("vacantes_agrOp2.html")

@app.route('/vacantes_fagrega2', methods=['POST'])
def vacante_fagrega():
    if request.method == 'POST':
        FuenteC = request.form['fuenteCandidato']
        FechaP = request.form['inicioFechaPublic']
        FechaE = request.form['finFechaPublic']
        Pub = request.form['publicada']
        Obs = request.form['observaciones']
        SeleC = request.form['candidactoSelecc']
        FechaC = request.form['fechaContratacion']
        idR = request.form['idRequisicion']
        idPu = request.form['idpuesto']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO vacante (fuenteCandidato, inicioFechaPublic, finFechaPublic,'
            'publicada, observaciones, candidatoSelecc, fechaContratacion, idRequisicion, idPuesto)'
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
            (FuenteC, FechaP, FechaE, Pub, Obs, SeleC, FechaC, idR, idPu))
        conn.commit()
        return redirect(url_for('vacantes'))
    
@app.route('/vacantes_fedita/<string:id>')
def vacante_editar(id): 
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idVacante, fuenteCandidato from vacante order by idVacante')
    dato = cursor.fetchall()

    cursor.execute('select fuenteCandidato from vacante where idVacante = %s', (id))
    dato1 = cursor.fetchone()

    cursor.execute('select inicioFechaPublic from vacante where idVacante = %s', (id))
    dato2 = cursor.fetchone()

    cursor.execute('select finFechaPublic from vacante where idVacante = %s', (id))
    dato3 = cursor.fetchone()

    cursor.execute('select publicada from vacante where idVacante = %s', (id))
    dato4 = cursor.fetchone()

    cursor.execute('select  observaciones from vacante where idVacante = %s', (id))
    dato5 = cursor.fetchone()

    cursor.execute('select  candidatoSelecc from vacante where idVacante = %s', (id))
    dato6 = cursor.fetchone()

    cursor.execute('select  fechaContratacion from vacante where idVacante = %s', (id))
    dato7 = cursor.fetchone()

    cursor.execute('select idRequisicion from vacante where idVacante = %s', (id))
    dato8 = cursor.fetchone()

    cursor.execute('select  idPuesto from vacante where idVacante = %s', (id))
    dato9 = cursor.fetchone()
    
    return render_template("vacantes_edi.html", vac=dato, FuenteC=dato1, FechaP=dato2, FechaE=dato3,
                           Pub=dato4, Obs=dato5, SeleC=dato6, FechaC=dato7, idRe=dato8, idPu=dato9)

@app.route('/vacantes_fedita2/<string:id>', methods=['POST'])
def vacante_fedita(id):
    if request.method == 'POST':
        FuenteC = request.form['fuenteCandidato']
        FechaP = request.form['inicioFechaPublic']
        FechaE = request.form['finFechaPublic']
        Pub = request.form['publicada']
        Obs = request.form['observaciones']
        SeleC = request.form['candidatoSelecc']
        FechaC = request.form['fechaContratacion']
        idR = request.form['idRequisicion']
        idPu = request.form['idPuesto']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE vacante SET fuenteCandidato=%s, inicioFechaPublic=%s, finFechaPublic=%s,'
            'publicada=%s, observaciones=%s, candidatoSelecc=%s, fechaContratacion=%s, idRequisicion=%s, idPuesto=%s where idVacante=%s',
            (FuenteC, FechaP, FechaE, Pub, Obs, SeleC, FechaC, idR, idPu, id))
        conn.commit()
    return redirect(url_for('vacantes'))
          
@app.route('/vacantes_borrar/<string:vac>')
def vacante_borrar(vac):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM vacante WHERE idVacante = %s', (vac))
    conn.commit()
    return redirect(url_for('vacantes'))

#candidato
@app.route('/candidatos')
def candidatos():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('SELECT idCandidato, nombre FROM candidato ORDER BY idCandidato')
    datos = cursor.fetchall()
    return render_template("candidatos.html", can=datos,idC=" ", idV=" ", idR=" ", Pjf=" ",
                          curp=" ", rfc=" ", nom=" ", calle=" ", numEI=" ", domC=" ",tel=" ",
                          tel2=" ",correoE=" ",edad=" ",sexo=" ",Ecivil=" ",GAva=" ",carrera=" ",
                          esr=" ",esP=" ",esR=" ",emR=" ",emP=" ",emr=" ",epR=" ",epP=" ",epr=" ",
                          epRe=" ",epPr=" ",epre=" ",etR=" ",etP=" ",etr=" ", ecR=" ",ecP=" ",ecr=" ",
                          efR=" ",efP=" ",efr=" ")

@app.route('/candidato_fdetalle/<string:id>', methods=['GET'])
def candidato_fdetalle(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idCandidato, nombre from candidato order by idVacante')
    dato = cursor.fetchall()
    cursor.execute('select idCandidato from candidato where idCandidato = %s', (id))
    dato1 = cursor.fetchone()
    cursor.execute('select idVacante from candidato where idCandidato = %s', (id))
    dato2 = cursor.fetchone()
    cursor.execute('select idRequisicion from candidato where idCandidato = %s', (id))
    dato3 = cursor.fetchone()
    cursor.execute('select idPuesto from candidato where idCandidato = %s', (id))
    dato4 = cursor.fetchone()
    cursor.execute('select CURP from candidato where idCandidato = %s', (id))
    dato5 = cursor.fetchone()
    cursor.execute('select RFC from candidato where idCandidato = %s', (id))
    dato6 = cursor.fetchone()
    cursor.execute('select nombre from candidato where idCandidato = %s', (id))
    dato7 = cursor.fetchone()
    cursor.execute('select domCalle from candidato where idCandidato = %s', (id))
    dato8 = cursor.fetchone()
    cursor.execute('select domNumExtInt from candidato where idCandidato = %s', (id))
    dato9 = cursor.fetchone()
    cursor.execute('select domColonia from candidato where idCandidato = %s', (id))
    dato10 = cursor.fetchone()
    cursor.execute('select tel1 from candidato where idCandidato = %s', (id))
    dato11 = cursor.fetchone()
    cursor.execute('select tel2 from candidato where idCandidato = %s', (id))
    dato12 = cursor.fetchone()
    cursor.execute('select correoE from candidato where idCandidato = %s', (id))
    dato13 = cursor.fetchone()
    cursor.execute('select edad from candidato where idCandidato = %s', (id))
    dato14 = cursor.fetchone()
    cursor.execute('select sexo from candidato where idCandidato = %s', (id))
    dato15 = cursor.fetchone()
    cursor.execute('select idEstadoCivil from candidato where idCandidato = %s', (id))
    dato16 = cursor.fetchone()
    cursor.execute('select idGradoAvance from candidato where idCandidato = %s', (id))
    dato17 = cursor.fetchone()
    cursor.execute('select idCarrera from candidato where idCandidato = %s', (id))
    dato18 = cursor.fetchone()
    cursor.execute('select entrevSelecReq from candidato where idCandidato = %s', (id))
    dato19 = cursor.fetchone()
    cursor.execute('select entrevSelecPresen from candidato where idCandidato = %s', (id))
    dato20 = cursor.fetchone()
    cursor.execute('select entrevSelecResult from candidato where idCandidato = %s', (id))
    dato21 = cursor.fetchone()
    cursor.execute('select evalPsicolgReq from candidato where idCandidato = %s', (id))
    dato22 = cursor.fetchone()
    cursor.execute('select evalPsicologPresen from candidato where idCandidato = %s', (id))
    dato23 = cursor.fetchone()
    cursor.execute('select evalPsicologResult from candidato where idCandidato = %s', (id))
    dato24 = cursor.fetchone()
    cursor.execute('select evalMedicaReq from candidato where idCandidato = %s', (id))
    dato25 = cursor.fetchone()
    cursor.execute('select evalMedicaPresen from candidato where idCandidato = %s', (id))
    dato26 = cursor.fetchone()
    cursor.execute('select evalMedicaResult from candidato where idCandidato = %s', (id))
    dato27 = cursor.fetchone()
    cursor.execute('select evalPsicometReq from candidato where idCandidato = %s', (id))
    dato28 = cursor.fetchone()
    cursor.execute('select evalPsicometPresene from candidato where idCandidato = %s', (id))
    dato29 = cursor.fetchone()
    cursor.execute('select evalPsicometResult from candidato where idCandidato = %s', (id))
    dato30 = cursor.fetchone()
    cursor.execute('select evalTecnicaReq from candidato where idCandidato = %s', (id))
    dato31 = cursor.fetchone()
    cursor.execute('select evalTecnicaPresen from candidato where idCandidato = %s', (id))
    dato32 = cursor.fetchone()
    cursor.execute('select evalTecnicaResult from candidato where idCandidato = %s', (id))
    dato33 = cursor.fetchone()
    cursor.execute('select evalConocReq from candidato where idCandidato = %s', (id))
    dato34 = cursor.fetchone()
    cursor.execute('select evalConocPresen from candidato where idCandidato = %s', (id))
    dato35 = cursor.fetchone()
    cursor.execute('select evalConocResult from candidato where idCandidato = %s', (id))
    dato36 = cursor.fetchone()
    cursor.execute('select entrevFinalReq from candidato where idCandidato = %s', (id))
    dato37 = cursor.fetchone()
    cursor.execute('select entrevFinalPresen from candidato where idCandidato = %s', (id))
    dato38 = cursor.fetchone()
    cursor.execute('select entrevFinalResul from candidato where idCandidato = %s', (id))
    dato39 = cursor.fetchone()
    return render_template("candidatos.html", can=dato, idC=dato1, idV=dato2, idR=dato3, Pjf=dato4, curp=dato5,
                            rfc=dato6, nom=dato7, calle=dato8, numEI=dato9, domC=dato10, tel=dato11, tel2=dato12, 
                            correoE=dato13, edad=dato14, sexo=dato15, Ecivil=dato16, GAva=dato17, carrera=dato18,
                            esr=dato19, esP=dato20, esR=dato21, epR=dato22, epP=dato23, epr=dato24, emR=dato25,
                            emP=dato26,emr=dato27, epRe=dato28, epPr=dato29, epre=dato30, etR=dato31, etP=dato32,
                            etr=dato33,ecR=dato34, ecP=dato35, ecr=dato36, efR=dato37, efP=dato38, efr=dato39)

@app.route('/candidato_agrega2')
def candidato_agrOp2():
    return render_template("candidatos_agrOp2.html")

@app.route('/candidato_fagrega2', methods=['POST'])
def candidato_fagrega2():
    if request.method == 'POST':
        idV = request.form['idVacante']
        idR = request.form['idRequisicion']
        Pjf = request.form['idPuesto']
        curp = request.form['CURP']
        rfc = request.form['RFC']
        nom = request.form['nombre']
        calle = request.form['domCalle']
        numEI = request.form['domNumExtInt']
        domC = request.form['domColonia']
        tel = request.form['tel1']
        tel2 = request.form['tel2']
        correoE = request.form['correoE']
        edad = request.form['edad']
        sexo = request.form['sexo']
        Ecivil = request.form['idEstadoCivil']
        es = request.form['esco']
        GAva = request.form['idGradoAvance']
        carrera = request.form['idCarrera']
        esr = request.form['entrevSelecReq']
        esP = request.form['entrevSelecPresen']
        esR = request.form['entrevSelecResult']
        emR = request.form['evalMedicaReq']
        emP = request.form['evalMedicaPresen']
        emr = request.form['evalMedicaResult']
        epR = request.form['evalPsicolgReq']
        epP = request.form['evalPsicologPresen']
        epr = request.form['evalPsicologResult']
        epRe = request.form['evalPsicometReq']
        epPr = request.form['evalPsicometPresene']
        epre = request.form['evalPsicometResult']
        etR = request.form['evalTecnicaReq']
        etP = request.form['evalTecnicaPresen']
        etr = request.form['evalTecnicaResult']
        ecR = request.form['evalConocReq']
        ecP = request.form['evalConocPresen']
        ecr = request.form['evalConocResult']
        efR = request.form['entrevFinalReq']
        efP = request.form['entrevFinalPresen']
        efr = request.form['entrevFinalResul']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute(
    'INSERT INTO candidato (idVacante, idRequisicion, idPuesto, CURP, RFC, nombre, domCalle, domNumExtInt, domColonia, tel1, tel2, correoE, edad, sexo, idEstadoCivil, idEscolaridad, idGradoAvance, idCarrera, entrevSelecReq, entrevSelecPresen, entrevSelecResult, evalMedicaReq, evalMedicaPresen, evalMedicaResult, evalPsicolgReq, evalPsicologPresen, evalPsicologResult, evalPsicometReq, evalPsicometPresene, evalPsicometResult, evalTecnicaReq, evalTecnicaPresen, evalTecnicaResult, evalConocReq, evalConocPresen, evalConocResult, entrevFinalReq, entrevFinalPresen, entrevFinalResul) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
    (idV, idR, Pjf, curp, rfc, nom, calle, numEI, domC, tel, tel2, correoE, edad, sexo, Ecivil, es, GAva, carrera, 
     esr, esP, esR, emR, emP, emr, epR, epP, epr, epRe, epPr, epre, etR, etP, etr, ecR, ecP, ecr, efR, efP, efr)
)
        conn.commit()
    return redirect(url_for('candidatos'))
    
@app.route('/candidatos_fedita/<string:id>')
def candidato_editar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('select idCandidato, nombre from candidato order by idVacante')
    dato = cursor.fetchall()
    cursor.execute('select idCandidato from candidato where idCandidato = %s', (id))
    dato1 = cursor.fetchone()
    cursor.execute('select idVacante from candidato where idCandidato = %s', (id))
    dato2 = cursor.fetchone()
    cursor.execute('select idRequisicion from candidato where idCandidato = %s', (id))
    dato3 = cursor.fetchone()
    cursor.execute('select idPuesto from candidato where idCandidato = %s', (id))
    dato4 = cursor.fetchone()
    cursor.execute('select CURP from candidato where idCandidato = %s', (id))
    dato5 = cursor.fetchone()
    cursor.execute('select RFC from candidato where idCandidato = %s', (id))
    dato6 = cursor.fetchone()
    cursor.execute('select nombre from candidato where idCandidato = %s', (id))
    dato7 = cursor.fetchone()
    cursor.execute('select domCalle from candidato where idCandidato = %s', (id))
    dato8 = cursor.fetchone()
    cursor.execute('select domNumExtInt from candidato where idCandidato = %s', (id))
    dato9 = cursor.fetchone()
    cursor.execute('select domColonia from candidato where idCandidato = %s', (id))
    dato10 = cursor.fetchone()
    cursor.execute('select tel1 from candidato where idCandidato = %s', (id))
    dato11 = cursor.fetchone()
    cursor.execute('select tel2 from candidato where idCandidato = %s', (id))
    dato12 = cursor.fetchone()
    cursor.execute('select correoE from candidato where idCandidato = %s', (id))
    dato13 = cursor.fetchone()
    cursor.execute('select edad from candidato where idCandidato = %s', (id))
    dato14 = cursor.fetchone()
    cursor.execute('select sexo from candidato where idCandidato = %s', (id))
    dato15 = cursor.fetchone()
    cursor.execute('select idEstadoCivil from candidato where idCandidato = %s', (id))
    dato16 = cursor.fetchone()
    cursor.execute('select idEscolaridad from candidato where idCandidato = %s', (id))
    da=cursor.fetchone()
    cursor.execute('select idGradoAvance from candidato where idCandidato = %s', (id))
    dato17 = cursor.fetchone()
    cursor.execute('select idCarrera from candidato where idCandidato = %s', (id))
    dato18 = cursor.fetchone()
    cursor.execute('select entrevSelecReq from candidato where idCandidato = %s', (id))
    dato19 = cursor.fetchone()
    cursor.execute('select entrevSelecPresen from candidato where idCandidato = %s', (id))
    dato20 = cursor.fetchone()
    cursor.execute('select entrevSelecResult from candidato where idCandidato = %s', (id))
    dato21 = cursor.fetchone()
    cursor.execute('select evalPsicolgReq from candidato where idCandidato = %s', (id))
    dato22 = cursor.fetchone()
    cursor.execute('select evalPsicologPresen from candidato where idCandidato = %s', (id))
    dato23 = cursor.fetchone()
    cursor.execute('select evalPsicologResult from candidato where idCandidato = %s', (id))
    dato24 = cursor.fetchone()
    cursor.execute('select evalMedicaReq from candidato where idCandidato = %s', (id))
    dato25 = cursor.fetchone()
    cursor.execute('select evalMedicaPresen from candidato where idCandidato = %s', (id))
    dato26 = cursor.fetchone()
    cursor.execute('select evalMedicaResult from candidato where idCandidato = %s', (id))
    dato27 = cursor.fetchone()
    cursor.execute('select evalPsicometReq from candidato where idCandidato = %s', (id))
    dato28 = cursor.fetchone()
    cursor.execute('select evalPsicometPresene from candidato where idCandidato = %s', (id))
    dato29 = cursor.fetchone()
    cursor.execute('select evalPsicometResult from candidato where idCandidato = %s', (id))
    dato30 = cursor.fetchone()
    cursor.execute('select evalTecnicaReq from candidato where idCandidato = %s', (id))
    dato31 = cursor.fetchone()
    cursor.execute('select evalTecnicaPresen from candidato where idCandidato = %s', (id))
    dato32 = cursor.fetchone()
    cursor.execute('select evalTecnicaResult from candidato where idCandidato = %s', (id))
    dato33 = cursor.fetchone()
    cursor.execute('select evalConocReq from candidato where idCandidato = %s', (id))
    dato34 = cursor.fetchone()
    cursor.execute('select evalConocPresen from candidato where idCandidato = %s', (id))
    dato35 = cursor.fetchone()
    cursor.execute('select evalConocResult from candidato where idCandidato = %s', (id))
    dato36 = cursor.fetchone()
    cursor.execute('select entrevFinalReq from candidato where idCandidato = %s', (id))
    dato37 = cursor.fetchone()
    cursor.execute('select entrevFinalPresen from candidato where idCandidato = %s', (id))
    dato38 = cursor.fetchone()
    cursor.execute('select entrevFinalResul from candidato where idCandidato = %s', (id))
    dato39 = cursor.fetchone()
    return render_template("candidatos_edi.html", can=dato, ides=da,idC=dato1, idV=dato2, idR=dato3, Pjf=dato4, curp=dato5,
                            rfc=dato6, nom=dato7, calle=dato8, numEI=dato9, domC=dato10, tel=dato11, tel2=dato12, 
                            correoE=dato13, edad=dato14, sexo=dato15, Ecivil=dato16, GAva=dato17, carrera=dato18,
                            esr=dato19, esP=dato20, esR=dato21, emR=dato22, emP=dato23, emr=dato24, epR=dato25,
                            epP=dato26,epr=dato27, epRe=dato28, epPr=dato29, epre=dato30, etR=dato31, etP=dato32,
                            etr=dato33,ecR=dato34, ecP=dato35, ecr=dato36, efR=dato37, efP=dato38, efr=dato39)

@app.route('/candidatos_fedita2/<string:id>', methods=['POST'])
def candidatos_fedita2(id):
    if request.method == 'POST':
        idC = request.form['idCandidato']
        idV = request.form['idVacante']
        idR = request.form['idRequisicion']
        Pjf = request.form['idPuesto']
        curp = request.form['CURP']
        rfc = request.form['RFC']
        nom= request.form['nombre']
        calle = request.form['domCalle']
        numEI = request.form['domNumExtInt']
        domC = request.form['domColonia']
        tel = request.form['tel1']
        tel2= request.form['tel2']
        correoE = request.form['correoE']
        edad = request.form['edad']
        sexo= request.form['sexo']
        esc= request.form['esco']
        Ecivil = request.form['idEstadoCivil']
        GAva = request.form['idGradoAvance']
        carrera = request.form['idCarrera']
        esr = request.form['entrevSelecReq']
        esP = request.form['entrevSelecPresen']
        esR = request.form['entrevSelecResult']
        emR = request.form['evalMedicaReq']
        emP = request.form['evalMedicaPresen']
        emr = request.form['evalMedicaResult']
        epR = request.form['evalPsicolgReq']
        epP = request.form['evalPsicolgPresen']
        epr = request.form['evalPsicolgResult']
        epRe = request.form['evalPsicometReq']
        epPr = request.form['evalPsicometPresen']
        epre = request.form['evalPsicometResult']
        etR = request.form['evalTecnicaReq']
        etP = request.form['evalTecnicaPresen']
        etr = request.form['evalTecnicaResult']
        ecR = request.form['evalConocReq']
        ecP = request.form['evalConocPresen']
        ecr = request.form['evalConocResult']
        efR = request.form['entrevFinalReq']
        efP = request.form['entrevFinalPresen']
        efr = request.form['entrevFinalResul']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute(
            'UPDATE candidato SET idVacante=%s, idRequisicion=%s, idPuesto=%s, CURP=%s, RFC=%s, nombre=%s, domCalle=%s, domNumExtInt=%s, domColonia=%s, tel1=%s, tel2=%s, correoE=%s, edad=%s, sexo=%s, idEstadoCivil=%s, idEscolaridad=%s, idGradoAvance=%s, idCarrera=%s, entrevSelecReq=%s, entrevSelecPresen=%s, entrevSelecResult=%s, evalMedicaReq=%s, evalMedicaPresen=%s, evalMedicaResult=%s, evalPsicolgReq=%s, evalPsicologPresen=%s, evalPsicologResult=%s, evalPsicometReq=%s, evalPsicometPresene=%s, evalPsicometResult=%s, evalTecnicaReq=%s, evalTecnicaPresen=%s, evalTecnicaResult=%s, evalConocReq=%s, evalConocPresen=%s, evalConocResult=%s, entrevFinalReq=%s, entrevFinalPresen=%s, entrevFinalResul=%s WHERE idCandidato=%s',
            (idV, idR, Pjf, curp, rfc, nom, calle, numEI, domC, tel, tel2, correoE, edad, sexo, Ecivil, esc, GAva, carrera,
             esr, esP, esR, emR, emP, emr, epR, epP, epr, epRe, epPr, epre, etR, etP, etr, ecR, ecP, ecr, efR, efP, efr,id)
            )
        conn.commit()
    return redirect(url_for('candidatos'))

@app.route('/candidatos_borrar/<string:can>')
def candidato_borrar(can):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM candidato WHERE idCandidato = %s', (can))
    conn.commit()
    return redirect(url_for('candidatos'))    

#examen psicometrico
@app.route('/examen')
def examen():
    return render_template('examen.html')
 
@app.route('/examen_enviar', methods=['POST'])
def examen_enviar():
    if request.method == 'POST':
        nom=request.form['nombre']
        p1=request.form['p1']
        p2=request.form['p2']
        p3=request.form['p3']
        p4=request.form['p4']
        p5=request.form['p5']
        p6=request.form['p6']
        p7=request.form['p7']
        p8=request.form['p8']
        p9=request.form['p9']
        p10=request.form['p10']
        p11=request.form['p11']
        p12=request.form['p12']
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO examen (nombre, preg1, preg2, preg3, preg4, preg5, preg6, preg7, preg8, preg9, preg10, preg11, preg12) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)', (nom,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12))
        conn.commit()
    return redirect(url_for('crud_examen'))

@app.route('/crud_examen')
def crud_examen():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('SELECT idExamen, nombre FROM examen order by idExamen')
    datos = cursor.fetchall()
    return render_template('examen_crudr.html', comentarios=datos)

@app.route('/examen_borrar/<string:id>')
def examen_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM examen WHERE idExamen={0}'.format(id))
    conn.commit()
    return redirect(url_for('crud_examen'))

@app.route('/examen_calificar/<string:id>')
def examen_calificar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute("SELECT idExamen, nombre, preg1, preg2, preg3, preg4, preg5, preg6, preg7, preg8, preg9, preg10, preg11, preg12 FROM examen WHERE idExamen=%s", (id))
    dato=cursor.fetchone()
    return render_template('califica_examen.html', com=dato)

@app.route('/examen_revisado/<string:id>', methods=['POST'])
def examen_revisado(id):
    if request.method == 'POST':
        cal1=int(request.form['preg1'])
        cal2=int(request.form['preg2'])
        cal3=int(request.form['preg3'])
        cal4=int(request.form['preg4'])
        cal5=int(request.form['preg5'])
        cal6 = int(request.form['preg6'])
        cal7=int(request.form['preg7'])
        cal8=int(request.form['preg8'])
        cal9=int(request.form['preg9'])
        cal10=int(request.form['preg10'])
        cal11=int(request.form['preg11'])
        cal12=int(request.form['preg12'])
        cali=cal1+cal2+cal3+cal4+cal5+cal6+cal7+cal8+cal9+cal10+cal11+cal12
        conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
        cursor = conn.cursor()
        cursor.execute('SELECT nombre, preg1, preg2, preg3, preg4, preg5, preg6, preg7, preg8, preg9, preg10, preg11, preg12 FROM examen WHERE idExamen=%s',(id))
        dato = cursor.fetchone()
        if dato:
            nombre, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12 = dato
            cursor.execute('DELETE FROM examen WHERE idExamen=%s',(id,))
            cursor.execute('INSERT INTO calificaciones (nombre, calificacion, preg1, preg2, preg3, preg4, preg5, preg6, preg7, preg8, preg9, preg10, preg11, preg12) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (nombre, cali, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12))
            conn.commit()
    return redirect(url_for('calificaciones'))

@app.route('/calificaciones')
def calificaciones():
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('SELECT idCalificacion, nombre, calificacion FROM calificaciones order by idCalificacion')
    datos=cursor.fetchall()
    return render_template('calificaciones.html', comentarios=datos)

@app.route('/calificacion_borrar/<string:id>')
def calificacion_borrar(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM calificaciones WHERE idCalificacion=%s', (id))
    conn.commit()
    return redirect(url_for('calificaciones'))

@app.route('/calificacion_detalles/<string:id>')
def calc_detalles(id):
    conn = pymysql.connect(host='localhost', user='root', passwd='', db='rh3')
    cursor = conn.cursor()
    cursor.execute('SELECT idCalificacion, nombre, preg1, preg2, preg3, preg4, preg5, preg6, preg7, preg8, preg9, preg10, preg11, preg12, calificacion FROM calificaciones WHERE idCalificacion=%s',(id))
    datos =cursor.fetchone()
    return render_template('detalle_cali.html', com=datos)

@app.route('/regreso')
def regreso():
    return redirect(url_for('calificaciones'))

if __name__ == "__main__":
    app.run(debug=True)

