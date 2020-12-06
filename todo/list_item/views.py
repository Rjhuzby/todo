from django.shortcuts import render

data = {
    'lists': [
        {'name': 'Забрать заказ', 'is_done': False},
        {'name': 'Сделать уборку', 'is_done': False},
        {'name': 'Написать вьюшку', 'is_done': True}
    ],
    'user_name': 'Admin',
}

def item_view(request):
    context = data
    return render(request, 'item.html', context)


