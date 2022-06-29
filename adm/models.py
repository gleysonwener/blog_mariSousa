from django.db import models


class ImagenPrincipal(models.Model):
    foto = models.ImageField(upload_to='post_imagens_principal', blank=True, null=True, verbose_name='Imagem Principal')
    texto_principal = models.TextField(verbose_name='Texto Principal')


    def foto_url(self):
        if self.foto and hasattr(self.foto, 'url'):
            print("a url da foto é:", self.foto.url)
            return self.foto.url
        else:
            return "media/gw.jpg"

    def __int__(self):
        self.texto_principal




