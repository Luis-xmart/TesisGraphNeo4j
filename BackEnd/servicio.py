from flask import Flask,request,jsonify,render_template
from Neo4jService import Conexion
from flask_cors import CORS
import requests
from random import randint



neo4j = Conexion("bolt://localhost:7687", 'neo4j', "12345")

app=Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

url = 'https://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
headers ={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
datos = requests.get(url,headers=headers)
texto = datos.text
palabras = texto.split()
num_aleatorio = randint(0,len(palabras))
num_aleatorio2 = randint(0,len(palabras))

@app.route("/",methods=['GET'])
def index():
  return render_template("index.html")

@app.route("/",methods=[ "POST"])

def getPersonas():
  with neo4j._driver.session() as session:
    Name=request.json["Name"]
    Apell=request.json["Apell"]
    Age=request.json["Age"]
    TIden=request.json["TIden"]
    Genero=request.json["Genero"]
    
    Efec=request.json["Efec"]
    EPS=request.json["EPS"]
    Vacuna=request.json["Vacuna"]
    Dosis=request.json["Dosis"]
    LoteP=request.json["LoteP"]
    FechaDP=request.json["FechaDP"]
    LoteS=request.json["LoteS"]
    FechaDS=request.json["FechaDS"]
    TipVacunador=request.json["TipVacunador"]
    IPS=request.json["IPS"]
    Regimen=request.json["Regimen"]
    
    Empleo=request.json["Empleo"]
    Municipio=request.json["Municipio"]
    Barrio=request.json["Barrio"]
    Etnia=request.json["Etnia"]
    Discap=request.json["Discap"]
    Desplaz=request.json["Desplaz"]
    
    AreaR=request.json["AreaR"]

    dolorIn=request.json["dolorIn"]
    eritema=request.json["eritema"]
    fatiga =request.json["fatiga"]
    mialga =request.json["mialga"]
    nauseas=request.json["nauseas"]
    adenopatias=request.json["adenopatias"]
    diarrea=request.json["diarrea"]
    artralgia=request.json["artralgia"]
    escalofrio =request.json["escalofrio"]
    resfriado=request.json["resfriado"]
    fiebre=request.json["fiebre"]
    alergia =request.json["alergia"]
    cabeza=request.json["cabeza"]
    hinchazon=request.json["hinchazon"]
    enrojecimiento=request.json["enrojecimiento"]
    desmayo=request.json["desmayo"]
    problemas=request.json["problemas"]
    ninguno=request.json["ninguno"]
    cancer=request.json["cancer"]
    renal=request.json["renal"]
    epoc=request.json["epoc"]
    asma=request.json["asma"]
    pulmonar=request.json["pulmonar"]
    fibrosis=request.json["fibrosis"]
    hipertencion=request.json["hipertencion"]
    demencia=request.json["demencia"]
    diabetes=request.json["diabetes"]
    down=request.json["down"]
    insuficiencia=request.json["insuficiencia"]
    arteria=request.json["arteria"]
    miocardio=request.json["miocardio"]
    VIH =request.json["VIH"]
    inmunodepresion=request.json["inmunodepresion"]
    hepatica=request.json["hepatica"]
    sobrepeso=request.json["sobrepeso"]
    embarazo =request.json["embarazo"]
    celulas=request.json["celulas"]
    tabaco=request.json["tabaco"]
    transplante=request.json["transplante"]
    cerebrovascular=request.json["cerebrovascular"]
    transtorno=request.json["transtorno"]
    ninguno2=request.json["ninguno2"]
    
    covid=request.json["covid"]
    inmune=request.json["inmune"]
    virus=request.json["virus"]
    adn=request.json["adn"]
    dosDosis=request.json["dosDosis"]
    creencia=request.json["creencia"]
    ningunaCreencia=request.json["ningunaCreencia"]

    print (covid,inmune,virus,adn,dosDosis,creencia,ningunaCreencia)

    aleatVac= palabras[num_aleatorio]+" "+palabras[num_aleatorio2]+" "+str(num_aleatorio)

    session.write_transaction(neo4j.nodo,TIden,Genero,Efec,EPS,Vacuna,LoteP,FechaDP,LoteS,FechaDS,TipVacunador,IPS,Regimen,Empleo,Municipio,Barrio,Etnia,Discap,Desplaz,Name,Apell,Age)

    session.write_transaction(neo4j.vacunado,aleatVac,TIden,Name,Apell,Age,Genero,Efec,EPS,Vacuna,Dosis,LoteP,LoteS,FechaDP,FechaDS,TipVacunador,IPS,Regimen,Empleo,Municipio,Barrio,Etnia,Discap,Desplaz)

    session.write_transaction(neo4j.crear_relacion,Name,Apell,Age,TIden, Genero,Efec,EPS,Vacuna,Dosis,LoteP,FechaDP,LoteS,FechaDS,TipVacunador,IPS,Regimen,Empleo,Municipio,Barrio,Etnia,Discap,Desplaz,AreaR)

    session.write_transaction(neo4j.relaciones2,Efec,EPS,Vacuna,Dosis,FechaDP,LoteS,Empleo,LoteP,FechaDS,Regimen)
    
    x = "Asma (moderada a grave)"
    if(asma == True):
      session.write_transaction(neo4j.ASMA,x,aleatVac)

    doIn="Dolor en el sitio de la inyección"  
    if(dolorIn== True):
      session.write_transaction(neo4j.dolorIn,doIn,aleatVac)
      
    Eri="Eritema (enrojecimiento de la piel)"     
    if(eritema== True):      
      session.write_transaction(neo4j.eritema,Eri,aleatVac)
      
    Fat="Fatiga"     
    if(fatiga== True):    
      session.write_transaction(neo4j.fatiga,Fat,aleatVac)
      
    Mial="Mialgia (Dolor muscular)"     
    if(mialga== True):     
      session.write_transaction(neo4j.mialga,Mial,aleatVac)
      
    Naus="Náuseas"     
    if(nauseas== True):    
      session.write_transaction(neo4j.nauseas,Naus,aleatVac)
      
    Aden="Adenopatías (ganglios)"     
    if(adenopatias== True):      
      session.write_transaction(neo4j.adenopatias,Aden,aleatVac)

    Diarr="Diarrea"     
    if(diarrea== True):      
      session.write_transaction(neo4j.diarrea,Diarr,aleatVac)
      
    Art="Artralgia (dolor en las articulaciones)"     
    if(artralgia== True):      
      session.write_transaction(neo4j.artralgia,Art,aleatVac)

    Esca="Escalofrió"     
    if(escalofrio== True):     
      session.write_transaction(neo4j.escalofrio,Esca,aleatVac)
      
    Resf="Resfriado"     
    if(resfriado== True):     
      session.write_transaction(neo4j.resfriado,Resf,aleatVac)
      
    Fieb="Fiebre"     
    if(fiebre== True):   
      session.write_transaction(neo4j.fiebre,Fieb,aleatVac)

    Aler="Alergia leve"     
    if(alergia== True):      
      session.write_transaction(neo4j.alergia,Aler,aleatVac)

    Cabe="Dolor de Cabeza (Cefalea)"     
    if(cabeza== True):     
      session.write_transaction(neo4j.cabeza,Cabe,aleatVac) 
    
    Hinch="Hinchazón de cara, ojos, boca, lengua (alergia generalizada)"     
    if(hinchazon== True):     
      session.write_transaction(neo4j.hinchazon,Hinch,aleatVac)
      
    Enroj="Enrojecimiento de todo el brazo"     
    if(enrojecimiento== True):    
      session.write_transaction(neo4j.enrojecimiento,Enroj,aleatVac)
      
    Desm="Desmayos"     
    if(desmayo== True):     
      session.write_transaction(neo4j.desmayo,Desm,aleatVac)
      
    Problem="Problemas para respirar"     
    if(problemas== True):     
      session.write_transaction(neo4j.problemas,Problem,aleatVac)
      
    Ning="Ninguno"     
    if(ninguno== True):     
      session.write_transaction(neo4j.ninguno,Ning,aleatVac)
      
    Canc="Cáncer"     
    if(cancer== True):      
      session.write_transaction(neo4j.cancer,Canc,aleatVac)

    Ren="Enfermedad Renal Crónica"     
    if(renal== True):      
      session.write_transaction(neo4j.renal,Ren,aleatVac)
    
    Epoc="EPOC (enfermedad pulmonar obstructiva crónica)"     
    if(epoc== True):    
      session.write_transaction(neo4j.epoc,Epoc,aleatVac)

    Pulmo="Enfermedad pulmonar intersticial"     
    if(pulmonar== True):     
      session.write_transaction(neo4j.pulmonar,Pulmo,aleatVac)

    Fibr="Fibrosis quística"     
    if(fibrosis== True):     
      session.write_transaction(neo4j.fibrosis,Fibr,aleatVac)

    Hipert="Hipertensión pulmonar"     
    if(hipertencion== True):     
      session.write_transaction(neo4j.hipertencion,Hipert,aleatVac)

    Demen="Demencia u otras afecciones neurológicas"     
    if(demencia== True):   
      session.write_transaction(neo4j.demencia,Demen,aleatVac)
      
    Diab="Diabetes (tipo 1 o tipo 2)"     
    if(diabetes== True):     
      session.write_transaction(neo4j.diabetes,Diab,aleatVac)

    Down="Síndrome de Down"     
    if(down== True):    
      session.write_transaction(neo4j.down,Down,aleatVac)

    Insufi="Insuficiencia cardiaca"     
    if(insuficiencia== True):    
      session.write_transaction(neo4j.insuficiencia,Insufi,aleatVac)

    Arter="Enfermedad de la arteria coronaria"     
    if(arteria== True):     
      session.write_transaction(neo4j.arteria,Arter,aleatVac)

    Miocardio="Miocardiopatías o hipertensión"     
    if(miocardio== True):      
      session.write_transaction(neo4j.miocardio,Miocardio,aleatVac)

    Bih="VIH"     
    if(VIH== True):    
      session.write_transaction(neo4j.vih,Bih,aleatVac)

    Inmuno="Personas inmunodeprimidas (sistema inmunitario debilitado)"     
    if(inmunodepresion== True):      
      session.write_transaction(neo4j.inmunodepresion,Inmuno,aleatVac)

    Hepat="Enfermedad hepática"     
    if(hepatica== True):      
      session.write_transaction(neo4j.hepatica,Hepat,aleatVac)

    Sobrep="Sobrepeso y obesidad"     
    if(sobrepeso== True):      
      session.write_transaction(neo4j.sobrepeso,Sobrep,aleatVac)

    Embar="Embarazo"     
    if(embarazo== True):     
      session.write_transaction(neo4j.embarazo,Embar,aleatVac)

    Celul="Enfermedad de células falciformes o talasemia"     
    if(celulas== True):      
      session.write_transaction(neo4j.celulas,Celul,aleatVac)

    Taba="Consumo de tabaco, actual o pasado"     
    if(tabaco== True):     
      session.write_transaction(neo4j.tabaco,Taba,aleatVac)

    Transpl="Trasplante de órganos sólidos o células madre sanguíneas" 
    if(transplante== True):     
      session.write_transaction(neo4j.transplante,Transpl,aleatVac)

    Cerebrova="Accidentes cerebrovasculares o enfermedades cerebrovasculares, que afectan el flujo sanguíneo hacia el cerebro"     
    if(cerebrovascular== True):    
      session.write_transaction(neo4j.cerebrovascular,Cerebrova,aleatVac)

    Transto="Trastornos por uso de sustancias"     
    if(transtorno== True):      
      session.write_transaction(neo4j.transtorno,Transto,aleatVac)

    Ninguno2="Ninguno"     
    if(ninguno2== True):      
      session.write_transaction(neo4j.ninguno2,Ninguno2,aleatVac)
    
    covid1="Si ya has tenido la COVID-19, no necesitas vacunarte"
    if(covid== True): 
      print(covid)
      session.write_transaction(neo4j.covid,covid1,aleatVac)

    inmune1="Una vez que recibes la vacuna contra el coronavirus, eres inmune de por vida" 
    if(inmune== True):
      print(inmune)     
      session.write_transaction(neo4j.inmune,inmune1,aleatVac)

    virus1="Las vacunas contienen el virus vivo que causa el coronavirus"     
    if(virus== True):
      print(virus)    
      session.write_transaction(neo4j.virus,virus1,aleatVac)

    adn1="Las vacunas pueden alterar tu ADN"    
    if(adn== True): 
      print(adn)     
      session.write_transaction(neo4j.adn,adn1,aleatVac)

    dosDosis1="No necesitas ambas dosis de las vacunas de dos dosis"     
    if(dosDosis== True): 
      print(dosDosis1)     
      session.write_transaction(neo4j.dosDosis,dosDosis1,aleatVac)
    
    creencia1="No tengo ninguna creencia sobre la vacuna contra el Covid-19"     
    if(creencia== True): 
      print(creencia1)     
      session.write_transaction(neo4j.creencia,creencia1,aleatVac)
    
    Ninguna="Ninguna"     
    if(ningunaCreencia== True): 
      print(Ninguna)     
      session.write_transaction(neo4j.ningunaCreencia,Ninguna,aleatVac)


    print("                                                          ")
    print("----------------------------------------------------------")
    print(aleatVac)
    result=session.write_transaction(neo4j.similiaridadBelief,aleatVac)
    x=[str(result) for result in result]
    resultado=x[0]
    print("creencias_s: "+resultado)
    # session.write_transaction(neo4j.similaridad,resultado,aleatVac)

    result2=session.write_transaction(neo4j.similaridadSintoma,aleatVac)
    x1=[str(result2) for result2 in result2]
    resultados = x1[0]
    print("sintoma: "+resultados)
    # session.write_transaction(neo4j.similaridad2,resultados,aleatVac)
    
    resultadoPantalla=session.write_transaction(neo4j.consultaV)
    r1=[str(resultadoPantalla) for resultadoPantalla in resultadoPantalla]
    print (r1)
    for lista in r1:
      print("                                                          ")
      print("-----------------------SIMILARIDAD---------------------")
      
      print (lista) 
      w=session.write_transaction(neo4j.similiaridadBelief,lista)
      z=session.write_transaction(neo4j.similaridadSintoma,lista)
      w2=[str(w) for w in w]
      z2=[str(z) for z in z]
      resultadow=w2[0]
      resultadoz=z2[0]
      print("similaridad_creencia "+lista+": "+resultadow)
      print("similaridad_sintoma "+lista+": "+resultadoz)
      session.write_transaction(neo4j.similaridad,resultadow,lista)
      session.write_transaction(neo4j.similaridad2,resultadoz,lista)
      consul=session.write_transaction(neo4j.consulta_idSimi,lista)
      consul2=session.write_transaction(neo4j.consulta_idSimi2,lista)
      # con=[str(consul) for consul in consul]
      print(consul)
      print(consul2)
      print(len(consul))
      print(len(consul2))
      newconsul = []
      newconsul2 = []
      cont = 0
      cont2 = 0
      if(len(consul)>=2):
        for c in consul:
          print(c,cont)
          if(cont!=0):
            newconsul.append(c)
          cont = cont+1
        
      session.write_transaction(neo4j.actualizacionSimiC,lista,resultadow)
      print(newconsul)

      for nc in newconsul:  
        if(nc!=0):
          session.write_transaction(neo4j.borrarSimiC,nc)








      if(len(consul2)>=2):
        for c2 in consul2:
          print(c2,cont2)
          if(cont2!=0):
            newconsul2.append(c2)
          cont2 = cont2+1
        
      session.write_transaction(neo4j.actualizacionSimiC2,lista,resultadow)
      print(newconsul2)

      for nc2 in newconsul2:  
        if(nc2!=0):
          session.write_transaction(neo4j.borrarSimiC,nc2)

      session.write_transaction(neo4j.similaridad2,resultadoz,lista)
      
    return request.json

if  __name__== '__main__':
  app.run(debug=True,host='0.0.0.0', port=5000)  