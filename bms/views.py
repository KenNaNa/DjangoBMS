from django.shortcuts import render, redirect
from bms.models import *


# 显示作者
def indexAutor(request):
    author_list = Author.objects.all()
    return render(request, 'indexAuthor.html', {'author_list': author_list})


# 添加作者与作者信息
def addAuthor(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        addr = request.POST.get('addr')
        email = request.POST.get('email')
        detail_obj = AuhtorDetail.objects.create(addr=addr, email=email)
        Author.objects.create(name=name, age=age, detail_id=detail_obj.id)
        return redirect('/bms/indexAuthor/')
    return render(request, 'addAuthor.html')


# 显示出版社
def indexPublish(request):
    publish_list = Publish.objects.all()
    return render(request, 'indexPublish.html', {'publish_list': publish_list})


# 添加出版社
def addPublish(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Publish.objects.create(name=name, email=email)
        return redirect('/bms/indexPublish/')
    return render(request, 'addPublish.html')


# 显示书籍
def indexBook(request):
    book_list = Book.objects.all()
    return render(request, 'indexBook.html', {'book_list': book_list})


# 添加书籍
def addBook(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        date = request.POST.get('date')
        price = request.POST.get('price')
        publish_id = request.POST.get('publish')
        authors = request.POST.getlist('authors')
        book_obj = Book.objects.create(
            title=title,
            publishDate=date,
            price=price,
            publish_id=publish_id
        )
        print(authors)
        book_obj.authors.set(authors)
        return redirect('/bms/indexBook/')
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    return render(request, 'addBook.html', {'publish_list': publish_list, 'author_list': author_list})


# 删除书籍
def delBook(request):
    id=request.GET.get('id')
    Book.objects.filter(id=id).delete()
    return redirect('/bms/indexBook/')

# 删除出版社
def delPublish(request):
    id=request.GET.get('id')
    Publish.objects.filter(id=id).delete()
    book_obj=Book.objects.filter(publish_id=id)
    for book in book_obj:
        book.authors.all().delete()  # book-authors关系表中的该出版社的关系也删除
    Book.objects.filter(publish_id=id).delete()  # 该出版社出版的书也删除
    return redirect('/bms/indexPublish')

# 删除作者
def delAuthor(request):
    id = request.GET.get('id')
    Author.objects.filter(id=id).delete()
    return redirect('/bms/indexAuthor/')



# 编辑出版社
def editPublish(request):
    if request.method=='POST':
        id=request.POST.get('id')
        name=request.POST.get('name')
        email=request.POST.get('email')
        Publish.objects.filter(id=id).update(name=name,email=email)
        return redirect('/bms/indexPublish/')
    id=request.GET.get('id')
    publish=Publish.objects.filter(id=id).first()
    return render(request,'editPublish.html',{'publish':publish})

# 编辑书籍
def editBook(request):
    if request.method=='POST':
        id=request.POST.get('id')
        title=request.POST.get('title')
        date=request.POST.get('date')
        price=request.POST.get('price')
        authors=request.POST.getlist('authors')
        publish_id=request.POST.get('publish')
        book_obj=Book.objects.filter(id=id).update(
            title=title,
            publishDate=date,
            price=price,
            publish_id=publish_id
        )
        Book.objects.get(id=id).authors.set(authors)
        return redirect('/bms/indexBook/')

    id=request.GET.get('id')
    book=Book.objects.filter(id=id).first()
    author_list=Author.objects.all()
    publish_list=Publish.objects.all()
    return render(request,'editBook.html',{'book':book,'author_list':author_list,'publish_list':publish_list})

# 编辑作者
def editAuthor(request):
    if request.method=='POST':
        aid=request.POST.get('aid')
        did=request.POST.get('did')
        name=request.POST.get('name')
        age=request.POST.get('age')
        addr=request.POST.get('addr')
        email=request.POST.get('email')
        Author.objects.filter(id=aid).update(name=name,age=age,detail_id=did)
        AuhtorDetail.objects.filter(id=did).update(addr=addr,email=email)
        return redirect('/bms/indexAuthor/')
    id=request.GET.get('id')
    author=Author.objects.filter(id=id).first()
    detail=AuhtorDetail.objects.filter(id=author.detail_id).first()
    return render(request,'editAuthor.html',{'author':author,'detail':detail})