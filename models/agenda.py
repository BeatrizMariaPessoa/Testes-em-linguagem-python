import json
from datetime import datetime
from datetime import timedelta


class Agenda:

  def __init__(self, id, data, confirmado, idcliente, idservico):
    self.__id = id
    self.__data = data
    self.__confirmado = confirmado
    self.__idcliente = idcliente
    self.__idservico = idservico

  def setid(self, id):
    self.__id = id

  def setdata(self, data):
    if data != '': self.__data = data
    else: raise ValueError()

  def setidcliente(self, idcliente):
    if idcliente >= 0: self.__idcliente = idcliente
    else: raise ValueError()

  def setidservico(self, idservico):
    if idservico >= 0: self.__idservico = idservico
    else: raise ValueError()

  def setconfirmado(self, confirmado):
    self.__confirmado = confirmado

  def get_id(self):
    return self.__id

  def get_data(self):
    return self.__data

  def get_confirmado(self):
    return self.__confirmado

  def get_idcliente(self):
    return self.__idcliente

  def get_idservico(self):
    return self.__idservico

  def __str__(self):
    return f'{self.__id} - {self.__data} - {self.__confirmado} - {self.__idcliente} - {self.__idservico}'

  def dicionario(self):
    return {
        "id": self.__id,
        "data": self.__data.strftime("%d/%m/%Y %H:%M"),
        "confirmado": self.__confirmado,
        "idcliente": self.__idcliente,
        "idservico": self.__idservico
    }


class NAgenda:
  __agendas = []

  @classmethod
  def inserir(cls, obj):
    NAgenda.abrir()
    id = 0
    for agenda in cls.__agendas:
      if agenda.get_id() > id: id = agenda.get_id()
    obj.setid(id + 1)
    cls.__agendas.append(obj)
    NAgenda.salvar()

  @classmethod
  def listar(cls):
    NAgenda.abrir()
    return cls.__agendas

  @classmethod
  def listar_id(cls, id):
    NAgenda.abrir()
    for agenda in cls.__agendas:
      if agenda.get_id() == id: return agenda
    return None

  @classmethod
  def atualizar(cls, obj):
    NAgenda.abrir()
    agenda = cls.listar_id(obj.get_id())
    agenda.setdata(obj.get_data())
    agenda.setconfirmado(obj.get_confirmado())
    agenda.setidcliente(obj.get_idcliente())
    agenda.setidservico(obj.get_idservico())
    NAgenda.salvar()

  @classmethod
  def excluir(cls, obj):
    NAgenda.abrir()
    agenda = cls.listar_id(obj.get_id())
    cls.__agendas.remove(agenda)
    NAgenda.salvar()

  @classmethod
  def abrir(cls):
    try:
      cls.__agendas = []
      with open("agendas.json", mode="r") as f:
        s = json.load(f)
        for agenda in s:
          a = Agenda(agenda["id"],
                     datetime.strptime(agenda["data"],
                                       "%d/%m/%Y %H:%M"), agenda["confirmado"],
                     agenda["idcliente"], agenda["idservico"])
          cls.__agendas.append(a)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("agendas.json", mode="w") as f:
      json.dump(cls.__agendas, f, default=Agenda.dicionario)
