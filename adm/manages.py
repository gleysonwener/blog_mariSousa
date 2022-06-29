from django.db import models
from django.db.models import Q

class PostManager(models.Manager):

    def busca(self, termo=None):
        qs = self.get_queryset()
        if termo is not None:
            or_lookup = (Q(titulo_post__icontains=termo) | Q(autor_post__icontains=termo) |
                         Q(conteudo_post__icontains=termo) | Q(exerto_post__icontains=termo))
        qs = qs.filter(or_lookup).distinct()
        return qs


class ComentarioManager(models.Manager):

    def busca(self, termo=None):
        qs = self.get_queryset()
        if termo is not None:
            or_lookup = (Q(nome_comentario__icontains=termo) | Q(email_comentario__icontains=termo) |
                         Q(comentario__icontains=termo))
        qs = qs.filter(or_lookup).distinct()
        return qs
