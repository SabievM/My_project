from django.db.models import Q
from phone.models import Phone

q_objects = ()
def q_search(search):
    kword = [word for word in search.split()]
    q_objects = Q()
    for item in kword:
        q_objects |= Q(name__icontains=item)
        q_objects |= Q(ram__icontains=item)
        q_objects |= Q(rom__icontains=item)
    return Phone.objects.filter(q_objects)
