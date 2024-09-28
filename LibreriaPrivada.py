import os, random, re, string, time
from colorama import Fore, Style
from typing import Optional


      
class DonValidator():
  # expresion para la llave
  EXP_LLAVE = r'^[a-z]{3,8}$'
  EXPS_REG = {
    'facil': r"^[a-zA-Z]{2}$",
    'facil2' : r"^[0-9]{2}+$",
    'empty': r'\s+', # elimina espacios en blanco y une todos los caracteres
    #expresiones originales
    'rut2':  r"^[1-9]{1}\d{6,7}-[0-9Kk]{1}$",
    'name': r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ]{2,20}$",
    'email2': r"^[a-z0-9._-]{2,50}@[a-z0-9]{2,30}\.[a-z]{2,3}$",
    'phone2': r"^[1-9]{1}\d{7}$",
    'address2': r"^[a-zA-Z0-9áéíóúÁÉÍÓÚñÑ\s.,_-]{2,60}$",
    }  
  
  lambda_exp_user = {
    'name': lambda valor : re.match(DonValidator.EXPS_REG['name'],valor),
    'rut': lambda valor : re.match(DonValidator.EXPS_REG['rut'],valor),
    'email': lambda valor : re.match(DonValidator.EXPS_REG['email'],valor),
    'phone': lambda valor : re.match(DonValidator.EXPS_REG['phone'],valor),
    'address': lambda valor : re.match(DonValidator.EXPS_REG['address'],valor), }
  
  lambda_fun_user = { 
    'name': lambda valor : DonValidator.validate_name(valor),  }

  valores_lambda = {
    'price': lambda valor : re.match(DonValidator.EXPS_REG['price'],valor),
    'amount': lambda valor : re.match(DonValidator.EXPS_REG['amount'],valor)  }
  
  def __init__(self):
    self.errores = 0
    pass

  def validate(self,llave:str,valor:str) -> Optional[str]:
    try:
      #flags = re.IGNORECASE  # Ignorar mayúsculas y minúsculas
      if llave := re.match(self.EXP_LLAVE,llave): 
        print('parametros buenos llave'),time.sleep(0.5)
        llave = llave.group()
        if llave in self.EXPS_REG.keys(): 
          print('llave correcta'),time.sleep(0.5)
          if respuesta := self.lambda_exp_user[llave](valor):
            valor = respuesta.group()
            valor = self.lambda_fun_user[llave](valor)
            print('valor correcto'),time.sleep(0.5)
            return valor
          else:
            print('errOr! en validate() : parametros del valor erroneos')
            return None
        else:
          print('errOr! en validate() : llave desconocida')
          return None
      else:
        print('errOr! en validate() : parametros de llave erroneo')
        return None
    except Exception as e:
      print(f'ERROR GRAVE en validate() tipo : {e}')
      return False
    else:
      pass
  
  @staticmethod
  def validate_name(valor:str) -> Optional[str]:
    print('validando...'),time.sleep(0.5)
    try:
      if valor.isalpha():
        if len(valor) >= 3 and len(valor) <= 20:
          return valor
        else:
          print('errOr! en validate_name() : largo de nombre no valido'),time.sleep(0.5)
          return None
      else:
        print('errOr! en validate:name() : nombre no contiene caracteres validos'),time.sleep(0.5)
        return None
    except Exception as e:
      print(f'ERROR GRAVE EN validate_name() tipo : {e}'),time.sleep(0.5)
      return False
    else:
      pass
      
  

  def validate_phone(self,valor:str) -> Optional[str]:
    try:
      if valor.isnumeric():
        if len(valor) == 8: 
          valor = f'569{valor}'
          return valor
        else:
          print('errOr! en validate_phone() : cantidad de numeros no valido')
          return None
      else:
        print('errOr! en validate_phone() : algunos caracteres no son validos')
        return None
    except Exception as e:
      print(f'ERROR GRAVE EN VALIDATE_PHONE() tipo : {e}')
      return False
    else:
      pass

os.system('cls')
juanita = DonValidator()
while True:
  
  llave = 'name'
  resultado = juanita.validate(llave,input('ingrese un nombre : ').strip().lower())
  print(f'el resultado es : {resultado}')
  