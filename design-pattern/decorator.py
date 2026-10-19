def gula():
  def wrapper():
    print("gula ")
  return wrapper
  
def kopi(func):
  def wrapper():
    print("kopi ")
    func()
  return wrapper

kopiGula = kopi(gula(kopi))