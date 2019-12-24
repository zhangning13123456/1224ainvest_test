from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from books.models import Books
from rest_framework.response import Response
from books.serializers import Booksserializers
class BookList(APIView):
    def get(self,request,*args,**kwargs):
        result = {
            'code': 1
        }
        queryset = Books.objects.all()
        ser = Booksserializers(instance=queryset,many=False)
        print(ser.data)
        result['data'] = ser.data
        return Response(result)

# 更新数据
class PutBook(APIView):
    def put(self, request, *args, **kwargs):
        # 自定义更新数据的方法
        result = {
            'code': 1
        }
        data = request.data
        # 先获取需要更新的数据
        pk = kwargs.get('pk')
        obj = Books.objects.filter(id=pk).first()
        if obj:
            ser = Booksserializers(instance=obj, data=data)
            if ser.is_valid():
                ser.save()
                result['msg'] = '数据更新成功'
            else:
                result['code'] = 0
                print(ser.errors)
                result['msg'] = '数据更新失败'
        else:
            result['code'] = 0
            result['msg'] = '数据更新失败,数据不存在'

        return Response(result)

class AddList(APIView):
    def post(self, request, *args, **kwargs):
        result = {
            'code': 1
        }
        data = request.data
        name = data.get('name')
        click_num = data.get('click_num')
        image = data.get('image')
        autor=data.get('autor')
        book_desc=data.get('book_desc')
        obj = Books.objects.filter(name=name).first()
        if not obj:
            Books.objects.create(
                name=name,
                click_num=click_num,
                image=image,
                autor=autor,
                book_desc=book_desc,
            )
            ser=Booksserializers(data=request.data)
            if ser.is_valid():
                ser.save()
            else:
                print(ser.errors)
            result['msg'] = '添加成功'
        else:
            result['code'] = 0
            result['msg'] = '书已存在'
            print('ＡＡＳ')
        return HttpResponse('添加成功')

class BookDelete(APIView):
    def delete(self, request, *args, **kwargs):
        # 获取书籍的id
        result = {
            'code': 1
        }
        try:
            pk = kwargs.get('pk')
            instance = Books.objects.filter(id=pk).first()

            if instance:
                # 从表中删除数据
                instance.delete()
                result['msg'] = '删除成功'
            else:
                result['code'] = 0
                result['msg'] = '删除失败'
        except Exception as err:
            print(err)
            result['code'] = 0
            result['msg'] = '请求异常'

        return Response(result)