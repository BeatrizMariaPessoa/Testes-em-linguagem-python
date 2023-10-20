from models.cliente import Cliente, NCliente

class View:
  @classmethod
  def cliente_inserir(cls, nome, email, fone):
    cliente = Cliente(0, nome, email, fone)
    NCliente.inserir(cliente)
    
  @classmethod
  def cliente_atualizar(cls, id, nome, email, telefone):
    cliente = Cliente(id, nome, email, fone)
    NCliente.atualizar(cliente)