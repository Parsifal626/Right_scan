from django.shortcuts import render, get_object_or_404, redirect
from .models import Bird

# Глобальная переменная для хранения идентификатора птицы, которую пользователь видел
seen_bird_id = None

def bird_list(request):
    birds = Bird.objects.all()
    return render(request, 'bird_app/bird_list.html', {'birds': birds})

def bird_detail(request, bird_id):
    bird = get_object_or_404(Bird, pk=bird_id)
    
    # Проверяем, была ли птица уже видена пользователем
    seen = False
    if bird_id == seen_bird_id:
        seen = True
    
    return render(request, 'bird_app/bird_detail.html', {'bird': bird, 'seen': seen})

def create_bird(request):
    if request.method == 'POST':
        name = request.POST['name']
        feather_color = request.POST['feather_color']
        photo = request.FILES['photo']
        bird = Bird(name=name, feather_color=feather_color, photo=photo)
        bird.save()
        return redirect('bird_list')
    return render(request, 'bird_app/create_bird.html')

def mark_bird_as_seen(request, bird_id):
    global seen_bird_id
    seen_bird_id = bird_id
    return redirect('bird_app/bird_detail', bird_id=bird_id)