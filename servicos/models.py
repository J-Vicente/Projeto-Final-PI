from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.


ESTADOS = [('0', '--Selecione--'), ('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), 
    ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), 
    ('MT', 'MT'), ('MS', 'MS'), ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), 
    ('PE', 'PE'), ('PI', 'PI'), ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), 
    ('RR', 'RR'), ('SC', 'SC'), ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO')]

SERVICOS = [('0', '--Selecione--'),('babá', 'Babá'), ('cozinheiro(a)', 'Cozinheiro(a)'), ('eletricista', 'Eletricista'), 
    ('encanador(a)', 'Encanador(a)'), ('faxina', 'Faxina'), ('informática', 'Informática'), ('jardinagem', 'Jardinagem'), 
    ('lava-jato', 'Lava-jato'), ('pintura', 'Pintura')]


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    senha = models.CharField(max_length=15, default='Ifrn12345')
    email = models.EmailField()
    foto_perfil = models.ImageField(upload_to='images')
    celular = models.CharField(max_length=11)
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=200)
    estado = models.CharField(max_length=2, choices=ESTADOS)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=150, default='')
    usuario = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
    is_profissional = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        novo_usuario = User.objects.create_user(self.nome, self.email, self.senha)
        novo_usuario.save()
        grupo_clientes, created = Group.objects.get_or_create(name='clientes')
        novo_usuario.groups.add(grupo_clientes)
        super(Cliente, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome +' '+ self.sobrenome

class ProfissionalManager(models.Manager):
    def buscar_por_nome(self, termo):
        return self.filter(nome__icontains=termo) | self.filter(sobrenome__icontains=termo) 

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    senha = models.CharField(max_length=15, default='Ifrn12345')
    email = models.EmailField()
    foto_perfil = models.ImageField(upload_to='images')
    celular = models.CharField(max_length=11)
    cpf = models.CharField(max_length=14)
    endereco = models.CharField(max_length=200)
    estado = models.CharField(max_length=2, choices=ESTADOS)
    cep = models.CharField(max_length=9)
    cidade = models.CharField(max_length=150, default='')
    servico = models.CharField(max_length=100, choices=SERVICOS)
    descricao = models.TextField(default='descrição')
    usuario = models.ForeignKey(User,on_delete=models.CASCADE, null=True,blank=True)
    is_profissional = models.BooleanField(default=True)
    objects = ProfissionalManager()

    def save(self, *args, **kwargs):
        novo_usuario = User.objects.create_user(self.nome, self.email, self.senha)
        novo_usuario.save()
        grupo_profissionais, created = Group.objects.get_or_create(name='profissionais')
        novo_usuario.groups.add(grupo_profissionais)
        super(Profissional, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome +' '+ self.sobrenome

class Contrato(models.Model):
    servico = models.CharField(max_length=100, default='')
    data = models.DateField()
    valor = models.FloatField()
    duracao_prevista = models.IntegerField()
    cliente = models.ForeignKey("Cliente",on_delete=models.CASCADE,)
    profissional = models.ForeignKey("Profissional",on_delete=models.CASCADE,)
    confirmado = models.BooleanField(default=False)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        date = self.data.strftime("%m/%d/%Y")
        return self.servico+'-'+date

class Fotos_servico(models.Model):
    imagem = models.ImageField(upload_to='images')
    profissional = models.ForeignKey("Profissional",on_delete=models.CASCADE,)


