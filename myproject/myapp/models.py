from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text

class ChoiceCategory(models.Model):
    name = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice_categories')

    def __str__(self):
        return self.name

class Choice(models.Model):
    category = models.ForeignKey(ChoiceCategory, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text

class QuestionParagraph(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='paragraphs')
    paragraph_text = models.TextField()

    def __str__(self):
        return f"Paragraph for {self.question.question_text}"

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    answer_text = models.TextField(blank=True, null=True)

class AnswerChoice(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='chosen_choices')
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return f"Answer for {self.answer.question.question_text}"
