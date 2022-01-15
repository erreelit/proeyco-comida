from flask import Blueprint, render_template, request, flash
from werkzeug.utils import redirect

from models.comidaDB import  usuarioAD
from utiles.db import db

pedidos = Blueprint('dbpediddos', __name__)


@pedidos.route('/')
def index():
    return render_template('cliente.html')


@pedidos.route('/estadoUPdate/<id>',methods=['POST', 'GET'])
def EStadoAc(id):
    estados = db.session.query(usuarioAD).filter_by(id=id).first()
    print(estados)
    if request.method == "POST":

        estados.estado = request.form["estado"]
        estados.FechaP = request.form["fecha"]
        db.session.commit()
        flash('Pedido actualizado')
        return redirect('/verestado')

    return render_template('actualizar.html',estados=estados)

@pedidos.route('/delete/<id>')
def delete(id):
    usu = usuarioAD.query.get(id)
    db.session.delete(usu)
    db.session.commit()
    print(usu)
    flash('eliminado')
    
    return redirect('/verestado')

@pedidos.route('/estados/<nombreC>', methods=['POST', 'GET'])
def pedido(nombreC):

    usu = db.session.query(usuarioAD).filter_by(nombreC=nombreC).first()
    print(usu)

    if request.method == "POST":

        usu.nombre = request.form['nameP']
        usu.valor = request.form['valorP']
        db.session.commit()
        flash('Pedido guardado')

    return redirect('/verestado')


@pedidos.route('/verestado')
def estados():
    
    usuario = db.session.query(usuarioAD).all()
    print(usuario)
    data = []
    if not usuario:
    
        return redirect('/')
    return render_template('estados.html', usuario=usuario)


@pedidos.route('/pedido', methods=['POST'])
def pedidoC():
    nombreC = request.form['nameC']
    direccion = request.form['direccion']
    ciudad = request.form['ciudad']
    telefonoC = request.form['telefonoC']
    FechaP = request.form['FechaP']
    estado = "EN ESPERA"
    nombre = ""
    valor = ""

    new_usuario = usuarioAD(nombreC, direccion, ciudad,
                            telefonoC, FechaP, estado, nombre, valor)
    db.session.add(new_usuario)
    db.session.commit()

    flash('usuario guardado')
    return render_template('comida.html', nombreC=nombreC)
