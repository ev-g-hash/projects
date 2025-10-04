from django.db.models import Q
from goods.models import Products


def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    
    keywords = [word for word in query.split() if len(word) > 2]
    q_objects = Q()

    for token in keywords:
        token = token.capitalize()
        q_objects |= Q(description__icontains=token)
        q_objects |= Q(name__icontains=token)

    for token_1 in keywords:
        token_1 = token_1
        q_objects |= Q(description__icontains=token_1)
        q_objects |= Q(name__icontains=token_1)

    for token_2 in keywords:
        token_2 = token_2.lower()
        q_objects |= Q(description__icontains=token_2)
        q_objects |= Q(name__icontains=token_2)
    
    return Products.objects.filter(q_objects)
