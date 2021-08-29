# -*- coding: utf-8 -*-
"""NZS_1170_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dqsUpCzIq-cRgnJhh3CtCpTRoeByDu1s

#NZS 1170.5:2004 .py method

This method references the following standard:
NZS 1170.5:2004 (incorporating Amendment Nos 1), for New Zealand structures.

Method developed 28 August 2021
(c) BVT Consulting Ltd

Developed - MMB

Reviewed -

###Initialise  Dependents and Libraries
"""

import pandas as pd
import numpy as np

"""#3 Site hazard spectra

##3.1.2 Spectral shape factor, $C_h(T)$

Given site subsoil class, period of vibration and spectral method (figure 3.1 or figure 3.2), this function returns the spectral shape factor. The function uses linear interpolation between table data points.
"""

#@title Table 3.1 - Spectral shape factor, $C_h(T)$ - General { vertical-output: true }

table3_1 = pd.DataFrame(
{"A Strong rock and B rock":[1.89,1.89,1.89,1.89,1.89,1.60,1.40,1.24,1.12,1.03,0.95,0.70,0.53,0.42,0.35,0.26,0.20,0.16],
 "C Shallow soil":[2.36,2.36,2.36,2.36,2.36,2.00,1.74,1.55,1.41,1.29,1.19,0.88,0.66,0.53,0.44,0.32,0.25,0.20],
 "D Deep or very soft soil":[3.00,3.00,3.00,3.00,3.00,3.00,2.84,2.53,2.29,2.09,1.93,1.43,1.07,0.86,0.71,0.52,0.40,0.32],
 "E Very soft soil":[3.00,3.00,3.00,3.00,3.00,3.00,3.00,3.00,3.00,3.00,3.00,2.21,1.66,1.33,1.11,0.81,0.62,0.49]

 },
 index = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5]
 )

table3_1.plot(table=True,figsize=(15, 10))

#@title Table 3.1(1) - Spectral shape factor, $C_h(T)$ - Modal analysis, numerical integration time history analysis, vertical loading and parts. { vertical-output: true }

table3_1_1 = pd.DataFrame(
{"A Strong rock and B rock":[1.00,2.35,2.35,2.35,1.89,1.60,1.40,1.24,1.12,1.03,0.95,0.70,0.53,0.42,0.35,0.26,0.20,0.16],
 "C Shallow soil":[1.33,2.93,2.93,2.93,2.36,2.00,1.74,1.55,1.41,1.29,1.19,0.88,0.66,0.53,0.44,0.32,0.25,0.20],
 "D Deep or very soft soil":[1.12,3.00,3.00,3.00,3.00,3.00,2.84,2.53,2.29,2.09,1.93,1.43,1.07,0.86,0.71,0.52,0.40,0.32],
 "E Very soft soil":[1.12,3.00,3.00,3.00,3.00,3.00,3.00,3.00,3.00,3.00,3.00,2.21,1.66,1.33,1.11,0.81,0.62,0.49]

 },
 index = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5]
 )

table3_1_1.plot(table=True,figsize=(15, 10))

#@title spectral_shape_factor(Subsoil_Type,Period_of_Vibration,spectral_method) { run: "auto", vertical-output: true }
Subsoil_Type = "C Shallow soil" #@param ["A Strong rock and B rock", "C Shallow soil", "D Deep or very soft soil", "E Very soft soil"]
Period_of_Vibration = 0 #@param {type:"number"}
spectral_method = "modal, numerical, parts (table 3.2)" #@param ["General (table 3.1)", "modal, numerical, parts (table 3.2)"]

def spectral_shape_factor(Subsoil_Type,Period_of_Vibration,spectral_method):

    if spectral_method == "General (table 3.1)":
      table = table3_1
    else:
      table = table3_1_1

    #linear interpolation
    a = table.index.values
    b = table[Subsoil_Type].to_numpy()
    
    ChT = np.interp(Period_of_Vibration, a, b)

    return ChT

spectral_shape_factor = spectral_shape_factor(Subsoil_Type,Period_of_Vibration,spectral_method)

print("Spectral shape factor =",spectral_shape_factor)

"""##3.1.4 Hazard factor, $Z$, and shortest major fault distance, $D$

Given location, this function returns the hazard factor and major fault distance for that location.
"""

#@title Table 3.3 - Z values and shortest major fault distances D for New Zealand locations { vertical-output: true }

table3_3 = pd.DataFrame([
['Akaroa',0.3,20],
['Alexandra',0.21,20],
['Arrowtown',0.3,20],
['Arthurs Pass',0.6,12],
['Ashburton',0.2,20],
['Auckland',0.13,20],
['Balclutha',0.13,20],
['Blenheim',0.33,0],
['Bluff',0.15,20],
['Bulls',0.31,20],
['Cambridge',0.18,20],
['Cheviot',0.4,20],
['Christchurch',0.3,20],
['Cromwell ',0.24,20],
['Dannevirke',0.42,10],
['Darfield',0.3,20],
['Dargarville',0.1,20],
['Dunedin',0.13,20],
['Eastbourne - Point Howard',0.4,4],
['Fairlie',0.24,20],
['Fielding',0.37,20],
['Fox Glacier',0.44,2],
['Foxton/Foxton Beach',0.36,20],
['Franz Josef',0.44,2],
['Geraldine',0.19,20],
['Gisborne',0.36,20],
['Gore',0.18,20],
['Greymouth',0.37,20],
['Hamilton',0.13,20],
['Hanmer Springs',0.55,2],
['Harihari',0.46,4],
['Hastings',0.39,20],
['Hawera',0.18,20],
['Hokitika',0.45,20],
['Huntly',0.15,20],
['Hutt Valley - south of Taita Gorge',0.4,0],
['Ingelwood',0.17,20],
['Invercargill',0.18,20],
['Kaikohe',0.1,20],
['Kaikoura',0.42,12],
['Kaitaia',0.1,20],
['Kawerau',0.29,20],
['Levin',0.4,20],
['Manakau City',0.13,20],
['Mangakino',0.21,20],
['Marton',0.3,20],
['Masterton',0.42,6],
['Matamata',0.19,20],
['Mataura',0.17,20],
['Milford Sound',0.54,20],
['Morrinsville',0.18,20],
['Mosgiel',0.13,20],
['Motueka',0.26,20],
['Mount Manunganui',0.2,20],
['Mt Cook',0.38,20],
['Murchison',0.34,20],
['Murupara',0.3,20],
['Napier',0.38,20],
['Nelson',0.27,20],
['New Plymouth',0.18,20],
['Ngaruawahia',0.15,20],
['Oamaru',0.13,20],
['Oban',0.14,20],
['Ohakune',0.27,20],
['Opotiki',0.3,20],
['Opunake',0.18,20],
['Otaki',0.4,20],
['Otira',0.6,3],
['Otorohanga',0.17,20],
['Paeroa',0.18,20],
['Pahiatua',0.42,8],
['Paihia/Russell',0.1,20],
['Palmerston ',0.13,20],
['Palmerston North',0.38,8],
['Paraparaumu',0.4,14],
['Patea',0.19,20],
['Picton',0.3,16],
['Porirua',0.4,8],
['Pukekohe',0.13,20],
['Putaruru',0.21,20],
['Queenstown',0.32,20],
['Raetihi',0.26,20],
['Rangiora',0.33,20],
['Reefton',0.37,20],
['Riverton',0.2,20],
['Rotorua',0.24,20],
['Ruatoria',0.33,20],
['Seddon',0.4,6],
['Springs Junction',0.45,3],
['St Arnaud',0.36,2],
['Stratford',0.18,20],
['Taihape',0.33,20],
['Takaka ',0.23,20],
['Taumaranui',0.21,20],
['Taupo',0.28,20],
['Tauranga',0.2,20],
['Te Anua',0.36,20],
['Te Aroha',0.18,20],
['Te Awamutu',0.17,20],
['Te Kuiti',0.18,20],
['Te Puke',0.22,20],
['Temuka',0.17,20],
['Thames',0.16,20],
['Timaru',0.15,20],
['Tokoroa',0.21,20],
['Turangi',0.27,20],
['Twizel',0.27,20],
['Upper Hutt',0.42,2],
['Waihi',0.18,20],
['Waikanae',0.4,15],
['Waimate',0.14,20],
['Wainiuomata',0.4,5],
['Waiouru',0.29,20],
['Waipawa',0.41,20],
['Waipukurau',0.41,20],
['Wairoa',0.37,20],
['Waitara',0.18,20],
['Waiuku',0.13,20],
['Wanaka',0.3,20],
['Wanganui',0.25,20],
['Ward',0.4,4],
['Warkworth',0.13,20],
['Wellington ',0.4,0],
['Wellington CBD (north of Basin Reserve)',0.4,2],
['Westport',0.3,20],
['Whakatane',0.3,20],
['Whangerei',0.1,20],
['Winton',0.2,20],
['Woodville',0.41,2]],
columns = ["Location","Z","D"]                       
)

table3_3

#@title hazard_factor(location) { run: "auto", vertical-output: true }
location = "Dunedin" #@param ['Akaroa','Alexandra','Arrowtown','Arthurs Pass','Ashburton','Auckland','Balclutha','Blenheim','Bluff','Bulls','Cambridge','Cheviot','Christchurch','Cromwell ','Dannevirke','Darfield','Dargarville','Dunedin','Eastbourne - Point Howard','Fairlie','Fielding','Fox Glacier','Foxton/Foxton Beach','Franz Josef','Geraldine','Gisborne','Gore','Greymouth','Hamilton','Hanmer Springs','Harihari','Hastings','Hawera','Hokitika','Huntly','Hutt Valley - south of Taita Gorge','Ingelwood','Invercargill','Kaikohe','Kaikoura','Kaitaia','Kawerau','Levin','Manakau City','Mangakino','Marton','Masterton','Matamata','Mataura','Milford Sound','Morrinsville','Mosgiel','Motueka','Mount Manunganui','Mt Cook','Murchison','Murupara','Napier','Nelson','New Plymouth','Ngaruawahia','Oamaru','Oban','Ohakune','Opotiki','Opunake','Otaki','Otira','Otorohanga','Paeroa','Pahiatua','Paihia/Russell','Palmerston ','Palmerston North','Paraparaumu','Patea','Picton','Porirua','Pukekohe','Putaruru','Queenstown','Raetihi','Rangiora','Reefton','Riverton','Rotorua','Ruatoria','Seddon','Springs Junction','St Arnaud','Stratford','Taihape','Takaka ','Taumaranui','Taupo','Tauranga','Te Anua','Te Aroha','Te Awamutu','Te Kuiti','Te Puke','Temuka','Thames','Timaru','Tokoroa','Turangi','Twizel','Upper Hutt','Waihi','Waikanae','Waimate','Wainiuomata','Waiouru','Waipawa','Waipukurau','Wairoa','Waitara','Waiuku','Wanaka','Wanganui','Ward','Warkworth','Wellington ','Wellington CBD (north of Basin Reserve)','Westport','Whakatane','Whangerei','Winton','Woodville']

def hazard_factor(location):

    Z = table3_3.loc[table3_3["Location"]==location,"Z"]
    Z = Z.squeeze()
    D = table3_3.loc[table3_3["Location"]==location,"D"]
    D = D.squeeze()

    return Z,D

hazard_factor,major_fault_distance = hazard_factor(location)

print("Hazard factor =",hazard_factor)
print("Major fault distance =",major_fault_distance)

"""##3.1.5 Return period factor $R$

Given the annual probability of exceedance, this function returns the return period factor.
"""

#@title Table 3.5 { vertical-output: true }

table3_5 = pd.DataFrame(
    {"Required annual probability of exceedance":['1/2500','1/2000','1/1000','1/500','1/250','1/100','1/50','1/25','1/20'],
     "Rs or Ru":[1.8,1.7,1.3,1.0,0.75,0.5,0.35,0.25,0.20]}
)

table3_5

#@title return_period_factor(annual_probability_of_exceedance) { run: "auto", vertical-output: true }
annual_probability_of_exceedance = "1/500" #@param ['1/2500','1/2000','1/1000','1/500','1/250','1/100','1/50','1/25','1/20']

def return_period_factor(annual_probability_of_exceedance):

  return_period_factor = table3_5.loc[table3_5["Required annual probability of exceedance"]==annual_probability_of_exceedance,"Rs or Ru"].squeeze()

  return return_period_factor

return_period_factor = return_period_factor(annual_probability_of_exceedance)

print("Return period factor =", return_period_factor)

"""##3.1.6 Near fault factor, $N(T,D)$, modal, numerical integration and parts

Given the annual probability of exceedance, shortest major fault distance and the modal, numerical integration and parts period of vibration (table 3.1(1)), this function returns the near fault factor. This function interpolates values in table 3.7, and then uses the logic in clauses 3.1.6.1 and 3.1.6.2 to determine $N(T,D)$.
"""

#@title Table 3.7 Maximum near-fault factors $N_{max}(T)$ { vertical-output: true }

table3_7 = pd.DataFrame(
    {'Period T (s)':[1.5,2,3,4,5],
     'Nmax(T)':[1.0,1.12,1.36,1.60,1.72]}
)

table3_7

def near_fault_factor(annual_probability_of_exceedance,major_fault_distance,Period_of_Vibration):

      a = annual_probability_of_exceedance

      T = Period_of_Vibration

    #Find Nmax(T) from table 3.7

      if T <= 1.5:
          N_max = table3_7.loc[table3_7["Period T (s)"]==1.5,"Nmax(T)"].squeeze()
      if T >= 5:
          N_max = table3_7.loc[table3_7["Period T (s)"]==5.0,"Nmax(T)"].squeeze()
      else:
          b = table3_7["Period T (s)"].to_numpy()
          c = table3_7["Nmax(T)"].to_numpy()
    
          N_max = np.interp(T, b, c)
    
    #Find N(T,D) from clauses 3.1.6.1 and 3.1.6.2
      
      if a in ['1/25','1/50','1/100','1/150','1/250'] :
          N = 1.0
      elif major_fault_distance >= 20 :
          N = 1.0
      elif major_fault_distance > 2 :
          N = 1 + (N_max - 1)*((20 - major_fault_distance )/18)
      elif major_fault_distance <= 2 :
          N = N_max
      else: N = 1.0

      return N

near_fault_factor = near_fault_factor(annual_probability_of_exceedance,major_fault_distance,Period_of_Vibration)

print("Near fault factor =",near_fault_factor)

"""##3.1.1 Elastic site spectra $C(T)$
Given the spectral shape factor, $C_h(T)$, the hazard factor, $Z$, the return period factor, $R$, and the near fault factor, $N(T,D)$, this function returns the elastic site hazard spectra, $C(T)$, also refered to as the site hazard coefficient.

$$C(T)=C_h(T)* Z* R* N(T,D)$$
"""

def elastic_site_spectra(spectral_shape_factor,hazard_factor,return_period_factor,near_fault_factor):

  #as per clause 3.1.1, check Z*Ru is not greater than 0.7. If Z*Ru is greater than 0.7, Z*Ru will be set to 0.7

  if hazard_factor*return_period_factor > 0.7:
    ZRu = 0.7
  else:
    ZRu = hazard_factor*return_period_factor
  
  elastic_site_spectra = spectral_shape_factor * ZRu * near_fault_factor

  return elastic_site_spectra

elastic_site_spectra = elastic_site_spectra(spectral_shape_factor,hazard_factor,return_period_factor,near_fault_factor)

print("Elastic site spectra =",elastic_site_spectra)

"""#8 Parts

This section is data, methods and functions for determining actions on parts of structures.

##8.1.2 Classification of parts and components

Given a part category and a return period factor, this function returns the Part risk factor, $R_p$, and the Structure limit state.

A value for $R_u$, the return period factor, is required for calculation of the P.6 part risk factor. It is ignored in the function for all other part categories.
"""

#@title Table 8.1 { vertical-output: true }

table8_1 = pd.DataFrame(
    {"Category":["P1","P2/P3","P4","P5","P6","P7"],
     "Part risk factor Rp":[1.0,1.0,1.0,1.0,2.0,1.0],
     "Structure limit state":['ULS','ULS','ULS','SLS2','SLS1','SLS1']}
)

table8_1

#@title part_risk_factor_limit_state(part_category,return_period_factor)) { run: "auto", vertical-output: true }
part_category = "P2/P3" #@param ["P1","P2/P3","P4","P5","P6","P7"]

def part_risk_factor_limit_state(part_category,return_period_factor):

  part_risk_factor = table8_1.loc[table8_1["Category"]==part_category,"Part risk factor Rp"].squeeze()
  structure_limit_state = table8_1.loc[table8_1["Category"]==part_category,"Structure limit state"].squeeze()

#check if part category is P6
  if part_category == "P6":
    part_risk_factor = part_risk_factor * return_period_factor

  return part_risk_factor, structure_limit_state

part_risk_factor, structure_limit_state = part_risk_factor_limit_state(part_category,return_period_factor)

print('Part risk factor =',part_risk_factor)
print('Structure limit state =',structure_limit_state)

"""## 8.3 Floor height coefficient, $C_{Hi}$

Given the height of the part attachment in the building, $h_i$, and the total height of the building, $h_n$, this function returns the floor height coefficient, $C_{Hi}$.
"""

#@title floor_height_coefficient(part_height,building_height) { run: "auto" }
part_height =  25#@param {type:"number"}
building_height =  50#@param {type:"number"}

def floor_height__coefficient(part_height,building_height):
  
  if part_height < 12 :
      floor_height__coefficient = (1+part_height/6)
  if part_height < 0.2*building_height:
    if (1+part_height/6) > (1+10*(part_height/building_height)):
      floor_height__coefficient = (1+10*(part_height/building_height))
    else:
      floor_height__coefficient = (1+part_height/6)

  if part_height >= 0.2*building_height:
      floor_height__coefficient = 3.0

  return floor_height__coefficient

floor_height__coefficient = floor_height__coefficient(part_height,building_height)
  
print("Floor height coefficient =",floor_height__coefficient)

"""## 8.4 Part or component spectral shape coefficient, $C_i(T_p)$

Given the part period of vibration, $T_p$, this function returns the part or component spectral shape factor, $C_i(T_p)$.
"""

#@title { run: "auto" }
part_period_of_vibration = 0 #@param {type:"number"}

def part_spectral_shape_factor(part_period_of_vibration):

  if part_period_of_vibration <= 0.75:
    part_spectral_shape_factor = 2.0
  elif part_period_of_vibration >= 1.5:
    part_spectral_shape_factor = 0.5
  else:
    part_spectral_shape_factor = 2*(1.75-part_period_of_vibration)

  return part_spectral_shape_factor

part_spectral_shape_factor = part_spectral_shape_factor(part_period_of_vibration)

print("Part spectral shape factor =",part_spectral_shape_factor)

"""## 8.2 Design response coefficient for parts and components

Given the site hazard coefficient, $C(0)$, the floor height coefficient, $C_{Hi}$ and the part spectral shape coefficient, $C_i(T_p)$, this function returns $C_p(T_p)$, the part or component design response coefficient.

$$C_p(T_p) = C(0)C_{Hi}C_i(T_p)$$
"""

def part_design_response_coefficient(elastic_site_spectra,floor_height__coefficient,part_spectral_shape_factor):
  
  part_design_response_coefficient = elastic_site_spectra * floor_height__coefficient * part_spectral_shape_factor

  return part_design_response_coefficient 

part_design_response_coefficient = part_design_response_coefficient(elastic_site_spectra,floor_height__coefficient,part_spectral_shape_factor)

print ("Part design response coefficient =",part_design_response_coefficient)

"""##8.6 Part or component response factor, $C_{ph}$

Given a part ductility, $\mu_p$, this function returns the part response factor, $C_{ph}$. $C_{ph}$, the horizonal part response factor, is equal to $C_{pv}$, the vertical part response factor.
"""

#@title Table 8.2 { vertical-output: true }

table8_2 = pd.DataFrame(
    {"Ductility of the part, Mu_p":[1.0,1.25,2.0,3.0],
     "Cph and Cpv":[1.0,0.85,0.55,0.45]})
table8_2

part_ductility = 1 #@param [1.0,1.25,2.0,3.0] {type:"

def part_response_factor(part_ductility):
  part_response_factor = table8_2.loc[table8_2["Ductility of the part, Mu_p"]==part_ductility,"Cph and Cpv"].squeeze()
  return part_response_factor

part_response_factor = part_response_factor(part_ductility)
print("Part response factor =",part_response_factor)

"""##8.5.1 Horizontal design actions

Given the horizontal design coefficient, $C_p(T_p)$, the part horizontal response factor, $C_{ph}$, the part risk factor, $R_p$ and the part weight, $W_p$ (in N), this function returns the horizontal design action on a part, $F_{ph}$.

$$F_{ph}=C_p(T_p) * C_{ph} * R_p * W_p$$
"""

part_weight = 42.08 #@param {type:"number"}

def part_horizontal_design_action(part_design_response_coefficient,part_response_factor,part_risk_factor,part_weight):

  part_horizontal_design_action = part_design_response_coefficient * part_response_factor * part_risk_factor * part_weight

  return part_horizontal_design_action

part_horizontal_design_action = part_horizontal_design_action(part_design_response_coefficient,part_response_factor,part_risk_factor,part_weight)

print("Part horizontal design action =",part_horizontal_design_action)