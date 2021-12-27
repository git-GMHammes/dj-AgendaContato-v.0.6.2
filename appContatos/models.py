# ↓ Antes de trabalhar no model execute o comando
# → python manage.py migrate
from django.db import models
# ↓ Acrescentar esta importação:
from django.utils import timezone
# → Importei por causa do campo ↓
# → models.DateTimeField(default=timezone.now)


# → Antes de tudo executar o comando
# → python manage.py migrate

# Create your models here.


class DbTabCategoria(models.Model):
    strNome = models.CharField(max_length=255)
# ↑ ATENÇÃO: Esta classe deve vir primeiro
# ↑ MOTIVO: Para ser referenciada pela classe abaixo
    # ↓ Para mudar representação de classe

    def __str__(self):
        # ↑ Para exibir o nome da categoria no admin
        return self.strNome


class DbTabContatos(models.Model):
    # Mudar o rótulo do formulário com o verbose_name ↓ - ↓
    strNome = models.CharField(max_length=255, verbose_name='Nome')
    strSobreNome = models.CharField(
        max_length=255, verbose_name='Sobrenome', blank=True)
    strTelefone = models.CharField(
        max_length=255, verbose_name='Telefone', blank=True)
    strEmail = models.CharField(
        max_length=255, verbose_name='E-mail', blank=True)
    strDataCriacao = models.DateTimeField(
        verbose_name='Data de Criação', default=timezone.now)
    # ↑ Utilizei a importação: ↑ from django.utils import timezone
    texDescricao = models.TextField(verbose_name='Descrição', blank=True)
    # ↓ Campo para marcar o que será exibido ↓
    bolExibir = models.BooleanField(verbose_name='Exibir', default=True)
    # ↓ Campo para exibir foto do contato ↓
    imgFoto = models.ImageField(
        verbose_name='Foto', blank=True, upload_to='fotos/%Y/%m')
    strKeyTabCategoria = models.ForeignKey(
        DbTabCategoria, verbose_name='Categoria',  on_delete=models.DO_NOTHING)
    # ↑ Referencia class DbTabCategoria(models.Model):
    # ↓ Para mudar representação de classe

    def __str__(self):
        # ↑ Para exibir o nome do contato no admin
        return self.strNome

    # Depois de concluir ou alterar etse arquivo faça:
    # Execute os comandos:
    # python manage.py makemigrations
    # python manage.py migrate
#
# Após a criação do models, ir para a área administrativa:
# admin.py
