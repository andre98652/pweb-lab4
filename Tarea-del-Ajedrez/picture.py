from colors import *
class Picture:
  def __init__(self, img):
        self.img = img
        
  def changeColor(self, from_color, to_color):
        new_img = []
        for row in self.img:
            new_row = ''.join(to_color if pixel == from_color else pixel for pixel in row)
            new_img.append(new_row)
        return Picture(new_img)
  
  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  
  
  def verticalMirror(self):
    """ Returns the vertical mirror image of the picture """
    vertical = []
    for value in reversed(self.img):
        vertical.append(value)
    return Picture(vertical)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    mirrored_img = []
    for row in self.img:
        mirrored_row = row[::-1]  # Invertir el orden de los caracteres en cada fila
        mirrored_img.append(mirrored_row)
    return Picture(mirrored_img)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    new_img = []
    for row in self.img:
        neg_row = ''.join(self._invColor(pixel) for pixel in row)
        new_img.append(neg_row)
    return Picture(new_img)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    new_img = []
    for i in range(len(self.img)):
        new_row = self.img[i] + p.img[i]
        new_img.append(new_row)
    return Picture(new_img)
  def up(self, p):
        """ Devuelve una nueva figura poniendo la figura p sobre la
            figura actual """
        new_img = []
        for row_self, row_p in zip(self.img, p.img):
            new_row = ''.join(pixel_p if pixel_self == ' ' else pixel_self for pixel_self, pixel_p in zip(row_self, row_p))
            new_img.append(new_row)
        return Picture(new_img)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    new_img = self.img.copy()  # Copiar la lista actual para evitar modificarla
    new_img.extend(p.img)  # Concatenar la lista de p a la nueva lista
    return Picture(new_img)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    new_img = []
    for row in self.img:
        new_row = row * n
        new_img.append(new_row)
    return Picture(new_img)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)
