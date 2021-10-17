from os import name
from neo4j import GraphDatabase

class Conexion(object):
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri,auth=(user, password))
    
    
    def nodo(self, tx,TIden,Genero,Efec,EPS,Vacuna,LoteP,FechaDP,LoteS,FechaDS,TipVacunador,IPS,Regimen,Empleo,Municipio,Barrio,Etnia,Discap,Desplaz,Name,Apell,Age): 
    
        tx.run("MERGE (:Type_of_identification{Type_of_identification:$TIden})",TIden=TIden)
        tx.run("MERGE (:Name{Name:$Name})",Name=Name)
        tx.run("MERGE (:Surname{Surname:$Apell})",Apell=Apell)
        tx.run("MERGE (:Age{Age:$Age})",Age=Age)
        tx.run("MERGE (:Residence_Area{Residence_Area:'Rural'}) MERGE (:Residence_Area{Residence_Area:'Urbano'})")
        tx.run("MERGE (:State{State:'Cauca'})")
        tx.run("MERGE (:Gender{Gender:$Genero})",Genero=Genero)
        tx.run("MERGE (:Confidence{Confidence:$Efec})",Efec=Efec)
        tx.run("MERGE (:Name_insurance_company{Name_insurance_company:$EPS})",EPS=EPS)
        tx.run("MERGE (:Name_Vaccine{Name_Vaccine:$Vacuna})",Vacuna=Vacuna)
        tx.run("MERGE (n:Dose_Number{Dose_Number:"+"1"+"}) MERGE(s:Dose_Number{Dose_Number:"+"2"+"})")
        tx.run("MERGE (:Lot{Lot:$LoteP})",LoteP=LoteP)
        tx.run("MERGE (:Vaccination_date{Vaccination_date:$FechaDP})",FechaDP=FechaDP)
        tx.run("MERGE (:Lot{Lot:$LoteS})",LoteS=LoteS)
        tx.run("MERGE (:Vaccination_date{Vaccination_date:$FechaDS})",FechaDS=FechaDS)
        tx.run("MERGE (:Profession{Profession:$TipVacunador})",TipVacunador=TipVacunador)
        tx.run("MERGE (:Name_company_org{Name_company_org:$IPS})",IPS=IPS)
        tx.run("MERGE (:Membership_regimen{Membership_regimen:$Regimen})",Regimen=Regimen)
        tx.run("MERGE (:Employment_group{Employment_group:$Empleo})",Empleo=Empleo)
        tx.run("MERGE (:Municipality{Municipality:$Municipio})",Municipio=Municipio)
        tx.run("MERGE (:Neighborhood{Neighborhood:$Barrio})",Barrio=Barrio)
        tx.run("MERGE (:Ethnic_group{Ethnic_group:$Etnia})",Etnia=Etnia)
        tx.run("MERGE (:Condition_of_disability{Condition_of_disability:$Discap})",Discap=Discap)
        tx.run("MERGE (:Condition_of_displacement{Condition_of_displacement:$Desplaz})",Desplaz=Desplaz)
        
   
    def crear_relacion(self, tx,Name,Apell,Age,TIden, Genero,Efec,EPS,Vacuna,Dosis,LoteP,FechaDP,LoteS,FechaDS,TipVacunador,IPS,Regimen,Empleo,Municipio,Barrio,Etnia,Discap,Desplaz,AreaR): 

        tx.run("MATCH (n:Type_of_identification ), (s:n4sch__Property) where n.Type_of_identification='"+TIden+"'  and s.n4sch__name='Type_of_identification' MERGE (n)-[:is]->(s)" ,TIden=TIden)
        tx.run("MATCH (n:Gender), (s:n4sch__Property) WHERE s.n4sch__name='Gender' and n.Gender='"+Genero+"' MERGE (n)-[:is]->(s)",Genero=Genero)
        tx.run("MATCH (n:Profession),(s:n4sch__Property) WHERE n.Profession='"+TipVacunador+"' AND  s.n4sch__name='Profession' MERGE (n)-[:is]->(s) ",TipVacunador=TipVacunador)
        tx.run("MATCH (n:Name_company_org),(s:n4sch__Property) WHERE n.Name_company_org='"+IPS+"' AND  s.n4sch__name='Name_company_org' MERGE (n)-[:is]->(s) ",IPS=IPS)
        tx.run("MATCH (n:Membership_regimen),(s:n4sch__Property) WHERE n.Membership_regimen='"+Regimen+"' AND  s.n4sch__name='Membership_regimen' MERGE (n)-[:is]->(s) ",Regimen=Regimen)
        
        tx.run("MATCH (n:Municipality),(s:n4sch__Property) WHERE n.Municipality='"+Municipio+"' AND  s.n4sch__name='Municipality' MERGE (n)-[:is]->(s)",Municipio=Municipio)
        tx.run("MATCH (n:Neighborhood),(s:n4sch__Property) WHERE n.Neighborhood='"+Barrio+"' AND  s.n4sch__name='Neighborhood' MERGE (n)-[:is]->(s)",Barrio=Barrio)
        tx.run("MATCH (n:Ethnic_group),(s:n4sch__Property) WHERE n.Ethnic_group='"+Etnia+"' AND  s.n4sch__name='Ethnic_group' MERGE (n)-[:is]->(s)",EtniaP=Etnia)
        tx.run("MATCH (n:Condition_of_disability),(s:n4sch__Property) WHERE n.Condition_of_disability='"+Discap+"' AND  s.n4sch__name='Condition_of_disability' MERGE (n)-[:is]->(s)",Discap=Discap)
        tx.run("MATCH (n:Condition_of_displacement),(s:n4sch__Property) WHERE n.Condition_of_displacement='"+Desplaz +"' AND  s.n4sch__name='Condition_of_displacement' MERGE (n)-[:is]->(s)",Desplaz=Desplaz)
        tx.run("MATCH (n:Neighborhood),(m:Municipality) WHERE m.Municipality='"+Municipio+"' AND n.Neighborhood='"+Barrio+"' MERGE (n)-[:from]->(m)",Municipio=Municipio,Barrio=Barrio)
        tx.run("MATCH (n:Residence_Area),(s:n4sch__Property) WHERE n.Residence_Area='"+AreaR+"' AND s.n4sch__name='Residence_area' MERGE (n)-[:is]->(s)",AreaR=AreaR)
        tx.run("MATCH (n:Neighborhood),(s:Residence_Area) WHERE n.Neighborhood='"+Barrio+"' AND  s.Residence_Area='"+AreaR+"' MERGE (n)-[:is]->(s)",Barrio=Barrio,AreaR=AreaR)
        tx.run("MATCH (n:State),(s:n4sch__Property) wHERE s.n4sch__name='State' MERGE (n)-[:is]->(s)")
        tx.run("MATCH (n:State),(s:Municipality) wHERE s.Municipality='"+Municipio+"' MERGE (s)-[:from]->(n)")
        tx.run("MATCH (n:Name),(s:n4sch__Property) wHERE n.Name='"+Name+"' AND s.n4sch__name='Name' MERGE (n)-[:is]->(s)",Name=Name)
        tx.run("MATCH (n:Surname),(s:n4sch__Property) wHERE n.Surname='"+Apell+"' AND s.n4sch__name='Last_name' MERGE (n)-[:is]->(s)",Apell=Apell)
        tx.run("MATCH (n:Age),(s:n4sch__Property) wHERE n.Age='"+Age+"' AND s.n4sch__name='Age' MERGE (n)-[:is]->(s)",Age=Age)
        tx.run("MATCH (n:Name),(s:Surname) WHERE n.Name='"+Name+"'AND s.Surname='"+Apell+"'MERGE (n)-[:has]->(s)",Name=Name,Apell=Apell)
        tx.run("MATCH (n:Name),(s:Age) WHERE n.Name='"+Name+"'AND s.Age='"+Age+"'MERGE (n)-[:has]->(s)",Name=Name,Age=Age)
        tx.run("MATCH (n:Age),(s:Surname) WHERE n.Age='"+Age+"'AND s.Surname='"+Apell+"'MERGE (s)-[:has]->(n)",Name=Name,Age=Age)
        tx.run("MATCH (n:Name),(s:Type_of_identification) WHERE n.Name='"+Name+"'AND s.Type_of_identification='"+TIden+"'MERGE (n)-[:has]->(s)",Name=Name,TIden=TIden)
        tx.run("MATCH (n:Type_of_identification),(s:Surname) WHERE n.Type_of_identification='"+TIden+"'AND s.Surname='"+Apell+"'MERGE (s)-[:has]->(n)",TIden=TIden,Apell=Apell)
    
    def relaciones2(self,tx,Efec,EPS,Vacuna,Dosis,FechaDP,LoteS,Empleo,LoteP,FechaDS,Regimen):

        tx.run("MATCH (n:Confidence), (s:n4sch__Property) WHERE s.n4sch__name='Confidence' AND n.Confidence='"+Efec+"' MERGE (n)-[:is]->(s)",Efec=Efec)

        tx.run("MATCH (n:Name_insurance_company),(s:n4sch__Property) where n.Name_insurance_company='"+EPS+"' and s.n4sch__name='Name_insurance_company' MERGE (n)-[:is]->(s)",EPS=EPS)
        tx.run("MATCH (n:Name_Vaccine),(s:n4sch__Property) WHERE n.Name_Vaccine='"+Vacuna+"' and s.n4sch__name='Name_Vaccine' MERGE (n)-[:is]->(s)",Vacuna=Vacuna)
        tx.run("MATCH (n:Dose_Number),(s:n4sch__Property) WHERE n.Dose_Number=1 AND s.n4sch__name='Dose_Number' MERGE (n)-[:is]->(s)")
        tx.run("MATCH (n:Dose_Number),(s:n4sch__Property) WHERE n.Dose_Number=2 AND s.n4sch__name='Dose_Number' MERGE (n)-[:is]->(s)")###########

        tx.run("MATCH (n:Vaccination_date), (s:n4sch__Property) WHERE n.Vaccination_date='"+FechaDP+"' AND s.n4sch__name='Vaccination_date'  MERGE (n)-[:is]->(s)",FechaDP=FechaDP)
        tx.run("MATCH (n:Vaccination_date), (s:n4sch__Property) WHERE n.Vaccination_date='"+FechaDS+"' AND s.n4sch__name='Vaccination_date'  MERGE (n)-[:is]->(s)",FechaDS=FechaDS)
        tx.run("MATCH (r:Lot),(u:n4sch__Property) WHERE r.Lot='"+LoteS+"' AND u.n4sch__name='Lot2' MERGE (r)-[:is]->(u)",LoteS=LoteS)
        tx.run("MATCH (r:Lot),(u:n4sch__Property) WHERE r.Lot='"+LoteP+"' AND u.n4sch__name='Lot1' MERGE (r)-[:is]->(u)",LoteP=LoteP)
        tx.run("MATCH (n:Employment_group),(s:n4sch__Class) WHERE n.Employment_group='"+Empleo+"' AND  s.n4sch__name='Employment_group' MERGE (n)-[:is]->(s)",Empleo=Empleo)
        
        tx.run("MATCH (n:Lot),(d:Dose_Number),(v:Vaccination_date) WHERE n.Lot='"+LoteP+"' AND v.Vaccination_date='"+FechaDP+"' AND d.Dose_Number=1 MERGE (n)-[:has]->(d) MERGE (n)-[:has]->(v) MERGE (v)-[:has]->(d)",Dosis=Dosis,LoteP=LoteP,FechaDP=FechaDP)
        tx.run("MATCH (n:Lot),(d:Dose_Number),(v:Vaccination_date) WHERE n.Lot='"+LoteS+"' AND v.Vaccination_date='"+FechaDS+"' AND d.Dose_Number=2 MERGE (n)-[:has]->(d) MERGE (n)-[:has]->(v) MERGE (v)-[:has]->(d)",Dosis=Dosis,LoteS=LoteS,FechaDS=FechaDS)
        tx.run("MATCH (n:Name_insurance_company),(m:Membership_regimen) WHERE  n.Name_insurance_company='"+EPS+"' AND m.Membership_regimen='"+Regimen+"' MERGE (m)-[:is]->(n)",EPS=EPS,Regimen=Regimen)

    def vacunado(self,tx,aleatVac,TIden,Name,Apell,Age,Genero,Efec,EPS,Vacuna,Dosis,LoteP,LoteS,FechaDP,FechaDS,TipVacunador,IPS,Regimen,Empleo,Municipio,Barrio,Etnia,Discap,Desplaz):
        tx.run("MERGE (:Vaccinated{Vaccinated:$aleatVac})",aleatVac=aleatVac)
        #tx.run("MATCH (n:Vaccinated),(s:n4sch__Class) WHERE n.Vaccinated='"+aleatVac+"' AND  s.n4sch__name='Vaccinator' MERGE (n)-[:is]->(s)",aleatVac=aleatVac)
        tx.run("MATCH (n:Type_of_identification ), (s:Vaccinated) where n.Type_of_identification='"+TIden+"' and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:has]->(n)" ,TIden=TIden,aleatVac=aleatVac)
        tx.run("MATCH (n:Name), (s:Vaccinated) where n.Name='"+Name+"' and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:has]->(n)" ,Name=Name,aleatVac=aleatVac)
        tx.run("MATCH (n:Surname), (s:Vaccinated) where n.Surname='"+Apell+"'and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:has]->(n)" ,Apell=Apell,aleatVac=aleatVac)
        tx.run("MATCH (n:Age), (s:Vaccinated) where n.Age='"+Age+"' and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:has]->(n)" ,Age=Age,aleatVac=aleatVac)
        tx.run("MATCH (n:Gender), (s:Vaccinated) where n.Gender='"+Genero+"' and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:has]->(n)" ,Genero=Genero,aleatVac=aleatVac)
        
        tx.run("MATCH (n:Confidence), (s:Vaccinated) where n.Confidence='"+Efec+"' and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:has]->(n)" ,Efec=Efec,aleatVac=aleatVac)
        tx.run("MATCH (n:Name_insurance_company), (s:Vaccinated) where n.Name_insurance_company='"+EPS+"' and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:affiliate_to]->(n)" ,EPS=EPS,aleatVac=aleatVac)
        tx.run("MATCH (n:Name_Vaccine), (s:Vaccinated) where n.Name_Vaccine='"+Vacuna+"' and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:vaccine]->(n)" ,Vacuna=Vacuna,aleatVac=aleatVac)
        tx.run("MATCH (n:Dose_Number), (s:Vaccinated) where n.Dose_Number="+Dosis+" and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:has]->(n)" ,aleatVac=aleatVac,Dosis=Dosis)
        tx.run("MATCH (n:Lot), (s:Vaccinated) where n.Lot='"+LoteP+"' and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:applied]->(n)" ,aleatVac=aleatVac,LoteP=LoteP)
        tx.run("MATCH (n:Lot), (s:Vaccinated) where n.Lot='"+LoteS+"' and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:applied]->(n)" ,aleatVac=aleatVac,LoteS=LoteS)
        tx.run("MATCH (n:Vaccination_date), (s:Vaccinated) where n.Vaccination_date='"+FechaDP+"'and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:has_vaccination_date_1]->(n)" ,aleatVac=aleatVac,FechaDP=FechaDP)
        tx.run("MATCH (n:Vaccination_date), (s:Vaccinated) where n.Vaccination_date='"+FechaDS+"'and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:has_vaccination_date_2]->(n)" ,aleatVac=aleatVac,FechaDS=FechaDS)
        tx.run("MATCH (n:Profession), (s:Vaccinated) where n.Profession='"+TipVacunador+"'and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:attended_by]->(n)" ,TipVacunador=TipVacunador,aleatVac=aleatVac)
        tx.run("MATCH (n:Name_company_org), (s:Vaccinated) where n.Name_company_org='"+IPS+"'and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:attended_in]->(n)" ,IPS=IPS,aleatVac=aleatVac)
        tx.run("MATCH (n:Membership_regimen), (s:Vaccinated) where n.Membership_regimen='"+Regimen+"'and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:is]->(n)" ,Regimen=Regimen,aleatVac=aleatVac)
        
        tx.run("MATCH (n:Employment_group), (s:Vaccinated) where n.Employment_group='"+Empleo+"'and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:has]->(n)" ,Empleo=Empleo,aleatVac=aleatVac)
        tx.run("MATCH (n:Municipality), (s:Vaccinated) where n.Municipality='"+Municipio+"'and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:is]->(n)" ,Municipio=Municipio,aleatVac=aleatVac)
        tx.run("MATCH (n:Neighborhood), (s:Vaccinated) where n.Neighborhood='"+Barrio+"'and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:is]->(n)" ,Barrio=Barrio,aleatVac=aleatVac)
        tx.run("MATCH (n:Ethnic_group), (s:Vaccinated) where n.Ethnic_group='"+Etnia+"'and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:has]->(n)" ,Etnia=Etnia,aleatVac=aleatVac)
        tx.run("MATCH (n:Condition_of_disability), (s:Vaccinated) where n.Condition_of_disability='"+Discap+"'and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:is]->(n)" ,Discap=Discap,aleatVac=aleatVac)
        tx.run("MATCH (n:Condition_of_displacement), (s:Vaccinated) where n.Condition_of_displacement='"+Desplaz+"'and s.Vaccinated='"+aleatVac+"' MERGE (s)-[:condition_of_displacement]->(n)" ,Desplaz=Desplaz,aleatVac=aleatVac)
        

        
    def ASMA(self,tx,x,aleatVac):
        tx.run('merge (:Comorbidity{Comorbidity:$x})',x=x)
        tx.run("MERGE (:Vaccinated{Vaccinated:$aleatVac})",aleatVac=aleatVac)
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+x+"' AND s.Vaccinated='"+aleatVac+"' AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)",aleatVac=aleatVac,x=x)

    def dolorIn (self,tx,doIn,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$doIn})',doIn=doIn)    
        tx.run("MERGE (:Vaccinated{Vaccinated:$aleatVac})",aleatVac=aleatVac)
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+doIn+"' AND s.Vaccinated='"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, doIn=doIn)

    def eritema (self,tx,Eri,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Eri})',Eri=Eri)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Eri+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Eri=Eri)

    def fatiga (self,tx,Fat,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Fat})',Fat=Fat)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Fat+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Fat=Fat)

    def mialga (self,tx,Mial,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Mial})',Mial=Mial)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Mial+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Mial=Mial)

    def nauseas (self,tx,Naus,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Naus})',Naus=Naus)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Naus+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Naus=Naus)
    
    def adenopatias (self,tx,Aden,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Aden})',Aden=Aden)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Aden+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Aden=Aden)

    def diarrea (self,tx,Diarr,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Diarr})',Diarr=Diarr)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Diarr+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Diarr=Diarr)

    def artralgia (self,tx,Art,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Art})',Art=Art)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Art+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Art=Art)

    def escalofrio (self,tx,Esca,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Esca})',Esca=Esca)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Esca+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Esca=Esca)
    
    def resfriado (self,tx,Resf,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Resf})',Resf=Resf)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Resf+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Resf=Resf)

    def fiebre (self,tx,Fieb,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Fieb})',Fieb=Fieb)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Fieb+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Fieb=Fieb)

    def alergia (self,tx,Aler,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Aler})',Aler=Aler)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Aler+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Aler=Aler)

    def cabeza (self,tx,Cabe,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Cabe})',Cabe=Cabe)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Cabe+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Cabe=Cabe)

    def hinchazon (self,tx,Hinch,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Hinch})',Hinch=Hinch)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Hinch+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Hinch=Hinch)

    def enrojecimiento (self,tx,Enroj,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Enroj})',Enroj=Enroj)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Enroj+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Enroj=Enroj)

    def desmayo (self,tx,Desm,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Desm})',Desm=Desm)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Desm+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Desm=Desm)
    
    def problemas (self,tx,Problem,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Problem})',Problem=Problem)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Problem+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Problem=Problem)

    def ninguno (self,tx,Ning,aleatVac):  
        tx.run('merge (:Name_side_effec{Name_side_effec:$Ning})',Ning=Ning)    
        tx.run("match (n:Name_side_effec),(s:Vaccinated),(c:n4sch__Class) where n.Name_side_effec='"+Ning+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Side_Effect' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Ning=Ning)

    def cancer (self,tx,Canc,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Canc})',Canc=Canc)
        tx.run("MERGE (:Vaccinated{Vaccinated:$aleatVac})",aleatVac=aleatVac)
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Canc+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Canc=Canc)
    
    def renal (self,tx,Ren,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Ren})',Ren=Ren)
        tx.run("MERGE (:Vaccinated{Vaccinated:$aleatVac})",aleatVac=aleatVac)
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Ren+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Ren=Ren)
    
    def epoc (self,tx,Epoc,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Epoc})',Epoc=Epoc)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Epoc+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Epoc=Epoc)
    
    def pulmonar (self,tx,Pulmo,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Pulmo})',Pulmo=Pulmo)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Pulmo+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Pulmo=Pulmo)
    
    def fibrosis (self,tx,Fibr,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Fibr})',Fibr=Fibr)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Fibr+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Fibr=Fibr)
    
    def hipertencion (self,tx,Hipert,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Hipert})',Hipert=Hipert)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Hipert+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Hipert=Hipert)
    
    def demencia (self,tx,Demen,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Demen})',Demen=Demen)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Demen+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Demen=Demen)
    
    def diabetes (self,tx,Diab,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Diab})',Diab=Diab)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Diab+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Diab=Diab)
    
    def down (self,tx,Down,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Down})',Down=Down)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Down+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Down=Down)
    
    def insuficiencia (self,tx,Insufi,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Insufi})',Insufi=Insufi)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Insufi+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Insufi=Insufi)
    
    def arteria (self,tx,Arter,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Arter})',Arter=Arter)    
        tx.run("match (n:Comorbidityc),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Arter+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Arter=Arter)
    
    def miocardio (self,tx,Miocardio,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Miocardio})',Miocardio=Miocardio)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Miocardio+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Miocardio=Miocardio)
    
    def vih (self,tx,Bih,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Bih})',Bih=Bih)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Bih+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Bih=Bih)
    
    def inmunodepresion (self,tx,Inmuno,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Inmuno})',Inmuno=Inmuno)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Inmuno+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Inmuno=Inmuno)
    
    def hepatica (self,tx,Hepat,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Hepat})',Hepat=Hepat)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Hepat+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Hepat=Hepat)
    
    def sobrepeso (self,tx,Sobrep,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Sobrep})',Sobrep=Sobrep)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Sobrep+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Sobrep=Sobrep)
   
    def embarazo (self,tx,Embar,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Embar})',Embar=Embar)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Embar+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Embar=Embar)
 
    def celulas (self,tx,Celul,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Celul})',Celul=Celul)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Celul+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Celul=Celul)
  
    def tabaco (self,tx,Taba,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Taba})',Taba=Taba)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Taba+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Taba=Taba)
  
    def transplante (self,tx,Transpl,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Transpl})',Transpl=Transpl)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Transpl+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Transpl=Transpl)
  
    def cerebrovascular (self,tx,Cerebrova,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Cerebrova})',Cerebrova=Cerebrova)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Cerebrova+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Cerebrova=Cerebrova)
  
    def transtorno (self,tx,Transto,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Transto})',Transto=Transto)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Transto+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Transto=Transto)
  
    def ninguno2 (self,tx,Ninguno2,aleatVac):  
        tx.run('merge (:Comorbidity{Comorbidity:$Ninguno2})',Ninguno2=Ninguno2)    
        tx.run("match (n:Comorbidity),(s:Vaccinated),(c:n4sch__Property) where n.Comorbidity='"+Ninguno2+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Comorbidity' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Ninguno2=Ninguno2)

        

    def covid (self,tx,covid,aleatVac):  
        tx.run('merge (:Belief{Belief:$covid})',covid=covid)    
        tx.run("match (n:Belief),(s:Vaccinated),(c:n4sch__Property) where n.Belief='"+covid+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Belief' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, covid=covid)

    def inmune (self,tx,inmune,aleatVac):  
        tx.run('merge (:Belief{Belief:$inmune})',inmune=inmune)    
        tx.run("match (n:Belief),(s:Vaccinated),(c:n4sch__Property) where n.Belief='"+inmune+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Belief' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, inmune=inmune)

    def virus(self,tx,virus,aleatVac):  
        tx.run('merge (:Belief{Belief:$virus})',virus=virus)    
        tx.run("match (n:Belief),(s:Vaccinated),(c:n4sch__Property) where n.Belief='"+virus+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Belief' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, virus=virus)

    def adn (self,tx,adn,aleatVac):  
        tx.run('merge (:Belief{Belief:$adn})',adn=adn)    
        tx.run("match (n:Belief),(s:Vaccinated),(c:n4sch__Property) where n.Belief='"+adn+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Belief' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, adn=adn)

    def dosDosis (self,tx,dosDosis,aleatVac):  
        tx.run('merge (:Belief{Belief:$dosDosis})',dosDosis=dosDosis)    
        tx.run("match (n:Belief),(s:Vaccinated),(c:n4sch__Property) where n.Belief='"+dosDosis+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Belief' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, dosDosis=dosDosis)

    def creencia (self,tx,creencia,aleatVac):  
        tx.run('merge (:Belief{Belief:$creencia})',creencia=creencia)    
        tx.run("match (n:Belief),(s:Vaccinated),(c:n4sch__Property) where n.Belief='"+creencia+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Belief' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, creencia=creencia)

    def ningunaCreencia (self,tx,Ninguna,aleatVac):  
        tx.run('merge (:Belief{Belief:$Ninguna})',Ninguna=Ninguna)    
        tx.run("match (n:Belief),(s:Vaccinated),(c:n4sch__Property) where n.Belief='"+Ninguna+"' AND s.Vaccinated= '"+aleatVac+"'   AND c.n4sch__name='Belief' merge (s)-[:has]->(n) merge (n)-[:is]->(c)" ,aleatVac=aleatVac, Ninguna=Ninguna)


    def similiaridadBelief(self, tx, aleatVac):
        query = ("MATCH (n:Vaccinated{Vaccinated:$aleatVac}) -[:has]->(s:Belief)WITH n, collect(id(s)) AS n1Creencias MATCH (v2:Vaccinated)-[:has] -> (Belief) WHERE n <> v2 WITH n, n1Creencias, v2, collect(id(Belief)) AS n2Creencias RETURN AVG(gds.alpha.similarity.jaccard(n1Creencias, n2Creencias)) AS similarity")
        result = tx.run(query, aleatVac=aleatVac)
        return [record["similarity"] for record in result]

    def similaridad (self,tx,resultado,aleatVac):
        tx.run("MERGE (:Similarity_B{Similarity_B:$resultado})",resultado=resultado)
        tx.run("MATCH (n:Similarity_B),(c:n4sch__Property),(s:Vaccinated) where s.Vaccinated='"+aleatVac+"'AND c.n4sch__name= 'Belief' AND n.Similarity_B='"+resultado+"'  MERGE (s)-[:has]->(n) MERGE (c)-[:is]->(s)",resultado=resultado,aleatVac=aleatVac)

    def consulta_idSimi(self,tx,lista):
        consulta=tx.run("match (n:Vaccinated)-[:has]->(s:Similarity_B) with s,n,id(s) as id where n.Vaccinated='"+lista+"' return id",lista=lista)
        return [record["id"]for record in consulta]
    
    def consulta_idSimi2(self,tx,lista):
        consulta=tx.run("match (n:Vaccinated)-[:has]->(s:Similarity_c) with s,n,id(s) as id where n.Vaccinated='"+lista+"' return id",lista=lista)
        return [record["id"]for record in consulta]

    def borrarSimiC(self,tx,id):
        tx.run("match (n) where id(n)=$id detach delete n",id=id)   
       
    def actualizacionSimiC(self,tx,aleatVac,resultado):
        tx.run("match (n:Vaccinated),(s:Similarity_B)with n,s match (n)-[:has]->(s) where n.Vaccinated='"+aleatVac+"' set s.Similarity_B='"+resultado+"'", resultado=resultado, aleatVac=aleatVac)   
        
    def actualizacionSimiC2(self,tx,aleatVac,resultado):
        tx.run("match (n:Vaccinated),(s:Similarity_c)with n,s match (n)-[:has]->(s) where n.Vaccinated='"+aleatVac+"' set s.Similarity_c='"+resultado+"'", resultado=resultado, aleatVac=aleatVac)   
        

    def similaridadSintoma(self, tx, aleatVac):
        query = ("match (n:Vaccinated{Vaccinated:'"+aleatVac+"'}) -[:has]->(s:Name_side_effec) WITH n, collect(id(s)) AS n1Efectos MATCH (v2:Vaccinated)-[:has] -> (Name_side_effec) WHERE n <> v2 WITH n, n1Efectos, v2, collect(id(Name_side_effec)) AS n2Efectos RETURN AVG(gds.alpha.similarity.jaccard(n1Efectos, n2Efectos)) AS similarity")
        result2 = tx.run(query, aleatVac=aleatVac)
        return [record["similarity"] for record in result2]

    def similaridad2 (self, tx, resultados, aleatVac):
        tx.run("MERGE (:Similarity_c{Similarity_c:$resultados})", resultados=resultados)
        tx.run("MATCH (n:Similarity_c),(c:n4sch__Class),(s:Vaccinated) where s.Vaccinated='"+aleatVac+"'AND c.n4sch__name='Side_Effect' AND n.Similarity_c='"+resultados+"' MERGE (s)-[:has]->(n) MERGE (c)-[:is]->(s)",resultado=resultados,aleatVac=aleatVac)
        

    def consultaV  (sel,tx):
        resultado=tx.run("MATCH (n:Vaccinated) RETURN n.Vaccinated as nombre")
        return [record["nombre"] for record in resultado]
    
    # def actualizacion (self,tx,lista):
    #     j
        

    

    def close(self):
        self._driver.close()