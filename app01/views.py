from django.shortcuts import render

from app01 import models


# Create your views here.
def books(request):
    page_num = request.GET.get('page')
    print(page_num, type(page_num))

    # 总数据是多少
    total_count = models.Book.objects.all().count()

    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=5, url_prefix="/books/", max_page=5)

    ret = models.Book.objects.all()[page_obj.start:page_obj.end]

    page_html = page_obj.page_html()

    return render(request, 'books.html', {'books': ret, 'page_html': page_html})
