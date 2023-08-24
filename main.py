from flask import Flask, request, render_template, jsonify
import json
from jsonmerge import merge
app = Flask(__name__)

BaseDeDatosAnime = json.load(open('anime.json'))

@app.route("/anime")
def index():
    return BaseDeDatosAnime

@app.route("/anime/<int:Identificador>", methods=['GET']) #METODO GET
def ReadAnime(Identificador):
    for anime in BaseDeDatosAnime['anime']:
        if anime['id'] == Identificador:
            return anime
    #return (por si no se encuentra un anime)
    return "No se encontro el Anime"

#METODO POST (crear animes)
@app.route("/anime", methods=['POST'])
def CreateAnime():
    #New_product = request.json
    NuevoAnime = {
        "id": request.json['id'],
        "titulo": request.json['titulo'],
        "puntaje": request.json['puntaje'],
        "tipo": request.json['tipo'],
        "season": request.json['season'],
        "generos": request.json[
            'generos'
        ]
    }
    BaseDeDatosAnime['anime'].append(NuevoAnime)
    with open('anime.json', 'w') as DocumentosAnimes:
        json.dump(BaseDeDatosAnime, DocumentosAnimes, indent=4)
    return BaseDeDatosAnime

#METODO PUT (actualizar productos)

@app.route("/anime/<int:Identificador>", methods=['PUT'])
def EditAnime(Identificador):
    for anime in BaseDeDatosAnime['anime']:
        if anime['id'] == Identificador:
            anime['titulo'] = request.json['id']
            anime["puntaje"] = request.json['puntaje']
            anime['tipo'] = request.json['tipo']
            anime['season'] = request.json['season']
            anime['generos'] = request.json[
                'generos'
            ]
            with open('anime.json', 'w') as DocumentosAnimes:
                json.dump(BaseDeDatosAnime, DocumentosAnimes, indent=4)
            return BaseDeDatosAnime
    return "No existe el anime que esta buscando"

#METODO PATCH (actualizar una parde del anime)

@app.route("/anime/<int:Identificador>", methods=['PATCH'])
def EditParAnime(Identificador):
    i = 0
    for anime in BaseDeDatosAnime['anime']:
        if anime['id'] == Identificador:
            Formato_actualización = {
                "titulo": request.json['titulo']
            }
            anime = merge(anime,Formato_actualización)
            BaseDeDatosAnime['anime'][i] = anime
            with open('anime.json', 'w') as DocumentosAnimes:
                json.dump(BaseDeDatosAnime, DocumentosAnimes, indent=4)
            return anime
        i+=1
#METODO DELETE (eliminar anime)
@app.route("/anime/<int:Identificador>", methods=['DELETE'])
def DeleteAnime(Identificador):
    for anime in BaseDeDatosAnime['anime']:
        if anime['id'] == Identificador:
            BaseDeDatosAnime['anime'].remove(anime)
            with open('anime.json', 'w') as DocumentosAnimes:
                json.dump(BaseDeDatosAnime, DocumentosAnimes, indent=4)
            return BaseDeDatosAnime
    return "No se encontro el anime"


if __name__ == "__main__":
    app.run(debug=True)
