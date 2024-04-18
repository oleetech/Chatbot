from django.db import models

class Message(models.Model):
    text = models.CharField(max_length=1024)  # Increase max_length if necessary
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question: {self.text[:50]}..."  # Shows the beginning of the text
    
    
class QA_Pair(models.Model):
    question = models.CharField(max_length=1024)
    answer = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question: {self.question[:50]}... - Answer: {self.answer[:50]}"