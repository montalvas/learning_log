from django.db import models


class Topic(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""
    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Retorna o nome do tópico"""
        return self.text


class Entry(models.Model):
    """Algo específico aprendido sobre um assunto."""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """Retorna até 50 caracteres do conteúdo."""
        return self.text[:50] + "..."
