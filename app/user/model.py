from tortoise import fields, models
from passlib.hash import bcrypt

#class Modules(models.Model):
#  id = fields.IntField(pk=True)
#  name = fields.CharField(max_length=50, unique=True)
#  
#  user: fields.ManyToManyRelation["Users"] = fields.ManyToManyField(
#    "models.Users", related_name="modules", through="user_module"
#  )
#  
#  rol: fields.ManyToManyRelation["Roles"] = fields.ManyToManyField(
#    "models.Roles", related_name="modules", through="rol_module"
#  )
#  
#  class Meta:
#    table = "modules"
#  
#  def __str__(self):
#    return self.name
#  
## Modelo para representar los usuarios registrados en el sistema
#class Users(models.Model):
#  """
#  The User model
#  """
#
#  id = fields.IntField(pk=True)
#  username = fields.CharField(max_length=20, unique=True)
#  name = fields.CharField(max_length=50, null=True)
#  surname = fields.CharField(max_length=50, null=True)
#  password_hash = fields.CharField(max_length=128, null=False)
#
#  rol: fields.ReverseRelation["Roles"]
#
#  module: fields.ManyToManyRelation[Modules]
#
#  def full_name(self) -> str:
#    """
#    Returns the best name
#    """
#    if self.name or self.surname:
#        return f"{self.name or ''} {self.surname or ''}".strip()
#    return self.username
#  
#  def verify_password(self, password):
#      return bcrypt.verify(password, self.password_hash)
#  
#  class Meta:
#    table = "users"
#    
#  def __str__(self):
#    return self.name
#
## Modelo para representar los roles para los usuarios
#class Roles(models.Model):
#  id = fields.IntField(pk=True)
#  name = fields.CharField(max_length=50, unique=True)
#
#  user: fields.ForeignKeyRelation[Users] = fields.ForeignKeyField(
#    "models.Users", related_name="roles"
#  )
#
#  module: fields.ManyToManyRelation[Modules]
#  
#  class Meta:
#    table = "roles"
#  
#  def __str__(self):
#    return self.name
#  
class Admin(models.Model):
  id = fields.IntField(pk=True)
  name = fields.CharField(max_length=50, unique=True)
  
  class Meta:
    table = "admin"
    
  def __str__(self):
    return self.name



