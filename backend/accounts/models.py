from django.db import models
from .preprocess_audio import get_mel

class Files(models.Model):
    email = models.EmailField(unique=True, max_length=255)
    audio1 = models.FileField()
    audio2 = models.FileField()
    audio3 = models.FileField()
    audio4 = models.FileField()
    audio5 = models.FileField()
    embeddings1 = models.TextField()
    embeddings2 = models.TextField()
    embeddings3 = models.TextField()
    embeddings4 = models.TextField()
    embeddings5 = models.TextField()
    
    
    def save(self, *args, **kwargs):
        try:
            self.audio1.save(name=self.audio1.name, content=self.audio1, save=False)
            self.audio2.save(name=self.audio2.name, content=self.audio2, save=False)
            self.audio3.save(name=self.audio3.name, content=self.audio3, save=False)
            self.audio4.save(name=self.audio4.name, content=self.audio4, save=False)
            self.audio5.save(name=self.audio5.name, content=self.audio5, save=False)
        except TypeError:
            pass
        finally:
            file_path1 = "media/" + str(self.audio1)
            file_path2 = "media/" + str(self.audio1)
            file_path3 = "media/" + str(self.audio1)
            file_path4 = "media/" + str(self.audio1)
            file_path5 = "media/" + str(self.audio1)
            self.embeddings1 = str(get_mel(str(file_path1)).tolist())
            self.embeddings2 = str(get_mel(str(file_path2)).tolist())
            self.embeddings3 = str(get_mel(str(file_path3)).tolist())
            self.embeddings4 = str(get_mel(str(file_path4)).tolist())
            self.embeddings5 = str(get_mel(str(file_path5)).tolist())
            super(Files, self).save(*args, **kwargs)
