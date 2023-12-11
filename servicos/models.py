from django.db import models
from django.contrib.auth.models import User, Group
# Create your models here.


ESTADOS = [('0', '--Selecione--'), ('ac', 'AC'), ('al', 'AL'), ('ap', 'AP'), ('am', 'AM'), 
    ('ba', 'BA'), ('ce', 'CE'), ('df', 'DF'), ('es', 'ES'), ('go', 'GO'), ('ma', 'MA'), 
    ('mt', 'MT'), ('ms', 'MS'), ('mg', 'MG'), ('pa', 'PA'), ('pb', 'PB'), ('pr', 'PR'), 
    ('pe', 'PE'), ('pi', 'PI'), ('rj', 'RJ'), ('rn', 'RN'), ('rs', 'RS'), ('ro', 'RO'), 
    ('rr', 'RR'), ('sc', 'SC'), ('sp', 'SP'), ('se', 'SE'), ('to', 'TO')]

SERVICOS = [('0', '--Selecione--'),('babá', 'Babá'), ('cozinheiro(a)', 'Cozinheiro(a)'), ('eletricista', 'Eletricista'), 
    ('encanador(a)', 'Encanador(a)'), ('faxina', 'Faxina'), ('informática', 'Informática'), ('jardinagem', 'Jardinagem'), 
    ('lava-jato', 'Lava-jato'), ('pintura', 'Pintura')]


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
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
        novo_usuario = User.objects.create_user(self.nome, self.email, 'Ifrn12345')
        novo_usuario.save()
        grupo_clientes, created = Group.objects.get_or_create(name='clientes')
        novo_usuario.groups.add(grupo_clientes)
        super(Cliente, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome + self.sobrenome

class Profissional(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
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

    def save(self, *args, **kwargs):
        # Se o usuário não estiver definido, associe-o ao usuário atual
        novo_usuario = User.objects.create_user(self.nome, self.email, 'Ifrn12345')
        novo_usuario.save()
        grupo_profissionais, created = Group.objects.get_or_create(name='profissionais')
        novo_usuario.groups.add(grupo_profissionais)
        super(Profissional, self).save(*args, **kwargs)


    def __str__(self):
        return self.nome + self.sobrenome

class Contrato(models.Model):
    servico = models.CharField(max_length=100, default='')
    data = models.DateField()
    valor = models.FloatField()
    duracao_prevista = models.IntegerField()
    cliente = models.ForeignKey("Cliente",on_delete=models.CASCADE,)
    profissional = models.ForeignKey("Profissional",on_delete=models.CASCADE,)

    def __str__(self):
        return self.servico+'-'+data

