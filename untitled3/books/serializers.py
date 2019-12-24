from rest_framework import serializers
from books.models import Books

class Booksserializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'