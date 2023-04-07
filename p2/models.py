from django.db import models
from .preprocess_audio import get_mel
from .predict import VAuthModel
from django.contrib.postgres.fields import ArrayField
from .settings import BASE_DIR
import os
from .predict import VAuthModel
from .settings import MEDIA_ROOT


model = VAuthModel()

class Files(models.Model):
    # phone_no = models.BigIntegerField(primary_key=True, max_length=10)
    email = models.EmailField(unique=True, max_length=255, primary_key=True)
    
    audio0 = models.FileField(upload_to='media/', default=None)
    audio1 = models.FileField(upload_to='media/', default=None)
    audio2 = models.FileField(upload_to='media/', default=None)
    audio3 = models.FileField(upload_to='media/', default=None)
    audio4 = models.FileField(upload_to='media/', default=None)
    audio5 = models.FileField(upload_to='media/', default=None)
    audio6 = models.FileField(upload_to='media/', default=None)
    audio7 = models.FileField(upload_to='media/', default=None)
    audio8 = models.FileField(upload_to='media/', default=None)
    audio9 = models.FileField(upload_to='media/', default=None)
    embeddings0 = models.TextField()
    embeddings1 = models.TextField()
    embeddings2 = models.TextField()
    embeddings3 = models.TextField()
    embeddings4 = models.TextField()
    embeddings5 = models.TextField()
    embeddings6 = models.TextField()
    embeddings7 = models.TextField()
    embeddings8 = models.TextField()
    embeddings9 = models.TextField()

    # embeddings0 = ArrayField(models.FloatField(default=[2.2]))
    # embeddings1 = ArrayField(models.FloatField(default=[2.2]))
    # embeddings2 = ArrayField(models.FloatField(default=[2.2]))
    # embeddings3 = ArrayField(models.FloatField(default=[2.2]))
    # embeddings4 = ArrayField(models.FloatField(default=[2.2]))
    # embeddings5 = ArrayField(models.FloatField(default=[2.2]))
    # embeddings6 = ArrayField(models.FloatField(default=[2.2]))
    # embeddings7 = ArrayField(models.FloatField(default=[2.2]))
    # embeddings8 = ArrayField(models.FloatField(default=[2.2]))
    # embeddings9 = ArrayField(models.FloatField(default=[2.2]))
    
    
    
    # def save(self, *args, **kwargs):
    #     try:
    #         self.audio0.save(name=self.audio0.name, content=self.audio0, save=False)
    #         self.audio1.save(name=self.audio1.name, content=self.audio1, save=False)
    #         self.audio2.save(name=self.audio2.name, content=self.audio2, save=False)
    #         self.audio3.save(name=self.audio3.name, content=self.audio3, save=False)
    #         self.audio4.save(name=self.audio4.name, content=self.audio4, save=False)
    #         self.audio5.save(name=self.audio5.name, content=self.audio5, save=False)
    #         self.audio6.save(name=self.audio6.name, content=self.audio6, save=False)
    #         self.audio7.save(name=self.audio7.name, content=self.audio7, save=False)
    #         self.audio8.save(name=self.audio8.name, content=self.audio8, save=False)
    #         self.audio9.save(name=self.audio9.name, content=self.audio9, save=False)
    #     except TypeError:
    #         pass
    #     finally:
    #         file_path0 = "media/" + str(self.audio0)
    #         file_path1 = "media/" + str(self.audio1)
    #         file_path2 = "media/" + str(self.audio2)
    #         file_path3 = "media/" + str(self.audio3)
    #         file_path4 = "media/" + str(self.audio4)
    #         file_path5 = "media/" + str(self.audio5)
    #         file_path6 = "media/" + str(self.audio6)
    #         file_path7 = "media/" + str(self.audio7)
    #         file_path8 = "media/" + str(self.audio8)
    #         file_path9 = "media/" + str(self.audio9)
    #         self.embeddings0 = str(model.get_embeddings(get_mel(str(file_path0)).tolist()))
    #         self.embeddings1 = str(model.get_embeddings(get_mel(str(file_path1)).tolist()))
    #         self.embeddings2 = str(model.get_embeddings(get_mel(str(file_path2)).tolist()))
    #         self.embeddings3 = str(model.get_embeddings(get_mel(str(file_path3)).tolist()))
    #         self.embeddings4 = str(model.get_embeddings(get_mel(str(file_path4)).tolist()))
    #         self.embeddings5 = str(model.get_embeddings(get_mel(str(file_path5)).tolist()))
    #         self.embeddings6 = str(model.get_embeddings(get_mel(str(file_path6)).tolist()))
    #         self.embeddings7 = str(model.get_embeddings(get_mel(str(file_path7)).tolist()))
    #         self.embeddings8 = str(model.get_embeddings(get_mel(str(file_path8)).tolist()))
    #         self.embeddings9 = str(model.get_embeddings(get_mel(str(file_path9)).tolist()))
    #         super(Files, self).save(*args, **kwargs)


class Name(models.Model):
    email = models.EmailField(unique=True, max_length=255, primary_key=True)
    embeddings0 = models.TextField(default=str(1))
    embeddings1 = models.TextField(default=str(1))
    embeddings2 = models.TextField(default=str(1))
    embeddings3 = models.TextField(default=str(1))
    embeddings4 = models.TextField(default=str(1))
    embeddings5 = models.TextField(default=str(1))
    embeddings6 = models.TextField(default=str(1))
    embeddings7 = models.TextField(default=str(1))
    embeddings8 = models.TextField(default=str(1))
    embeddings9 = models.TextField(default=str(1))
    