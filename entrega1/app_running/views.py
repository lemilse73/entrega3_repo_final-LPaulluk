from django.http import HttpResponse
from django.shortcuts import render
from app_running.models import Corredor , Avatar
from app_running.models import Carreras , Avatar
from app_running.models import Teams , Avatar
from app_running.models import Post
from django.template import loader
from app_running.forms import Corredor_formulario , UserEditForm
from app_running.forms import Carreras_formulario , UserEditForm
from app_running.forms import Teams_formulario , UserEditForm
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
from app_running.forms import ContactoForm , UserEditForm
from app_running.forms import Post_formulario , UserEditForm

# Create your views here.
def inicio (request):
    return render (request,"padre.html")
    

def home (request):
    return render (request,"padre.html")

def nosotros (request):
    return render (request,"nosotros.html")
    
def contacto (request):
    data = {
        "form": ContactoForm()
    }

    if request.method == "POST":
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
         formulario.save()   
         data["mensaje"] = "Mensaje Recibido"
        else:
            data["form"] = formulario
    return render (request,"contacto.html", data)


def noticias (request):
    return render (request,"noticias.html")

def post (request):
    return render (request,"post.html")

def corredor (request):
    corredor = Corredor.objects.all()
    dicc = {"corredor" : corredor}
    plantilla = loader.get_template ("corredor.html")
    documento = plantilla.render (dicc)
    return HttpResponse(documento)

@login_required
def corredoradm (request):
    corredor = Corredor.objects.all()
    dicc = {"corredor" : corredor}
    plantilla = loader.get_template ("corredoradm.html")
    documento = plantilla.render (dicc)
    return HttpResponse(documento)

def carreras (request):
    carreras = Carreras.objects.all()
    dicc = {"carreras" : carreras}
    plantilla = loader.get_template ("carreras.html")
    documento = plantilla.render (dicc)
    return HttpResponse(documento)

@login_required
def carrerasadm (request):
    carreras = Carreras.objects.all()
    dicc = {"carreras" : carreras}
    plantilla = loader.get_template ("carrerasadm.html")
    documento = plantilla.render (dicc)
    return HttpResponse(documento)

def teams (request):
    teams = Teams.objects.all()
    dicc = {"teams" : teams}
    plantilla = loader.get_template ("teams.html")
    documento = plantilla.render (dicc)
    return HttpResponse(documento)

@login_required
def teamsadm (request):
    teams = Teams.objects.all()
    dicc = {"teams" : teams}
    plantilla = loader.get_template ("teamsadm.html")
    documento = plantilla.render (dicc)
    return HttpResponse(documento)

def corredor_formulario(request):

    if request.method == "POST":

        mi_formulario = Corredor_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data


        corredor = Corredor( nombre = datos['nombre'] , apellido = datos['apellido'] , modalidad = datos['modalidad'] , email = datos['email'], team = datos['team'])
        corredor.save()
        return render(request , "formulario_corredor.html")

    return render (request, "formulario_corredor.html")

def carreras_formulario(request):

    if request.method == "POST":

        mi_formulario = Carreras_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data


        carreras = Carreras( nombre = datos['nombre'] , modalidad = datos['modalidad'] , distancia = datos['distancia'], fecha = datos['fecha'])
        carreras.save()
        return render(request , "formulario_carreras.html")

    return render (request, "formulario_carreras.html")

def teams_formulario(request):

    if request.method == "POST":

        mi_formulario = Teams_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data


        teams = Teams( nombre = datos['nombre'] , modalidad = datos['modalidad'] , email = datos['email'])
        teams.save()
        return render(request , "formulario_teams.html")

    return render (request, "formulario_teams.html")

def buscar_corredor(request):
    return render( request , "buscar_corredor.html")

def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        corredor = Corredor.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html", {"corredor": corredor})

    else:
        return HttpResponse(" Campo vacio")

def buscar_corredor_apellido(request):
    return render( request , "buscar_corredor_apellido.html")

def buscar_apellido(request):

    if request.GET['apellido']:
        apellido = request.GET['apellido']
        corredor = Corredor.objects.filter(apellido__icontains = apellido)
        return render( request , "resultado_busqueda_apellido.html", {"corredor": corredor})

    else:
        return HttpResponse(" Campo vacio")

def buscar_carreras_nombre(request):
    return render( request , "buscar_carreras_nombre.html")

def buscar_carreras(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        carreras = Carreras.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda_carreras.html", {"carreras": carreras})

    else:
        return HttpResponse(" Campo vacio")

def elimina_corredor(request, id):
    
    corredor = Corredor.objects.get (id=id)
    corredor.delete()

    corredor = Corredor.objects.all()

    return render(request, "corredoradm.html", {"corredor": corredor})


def elimina_carreras(request, id):
    
    carreras = Carreras.objects.get (id=id)
    carreras.delete()

    carreras = Carreras.objects.all()

    return render(request, "carreras.html", {"carreras": carreras})


def elimina_teams(request, id):
    
    teams = Teams.objects.get (id=id)
    teams.delete()

    teams = Teams.objects.all()

    return render(request, "teams.html", {"teams": teams})  


def editar_corredor( request , id):
    corredor = Corredor.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Corredor_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            corredor.nombre = datos['nombre']
            corredor.apellido = datos['apellido']
            corredor.modalidad = datos['modalidad']
            corredor.email = datos['email']
            corredor.team = datos['team']
                  
            corredor.save()
            corredor = Corredor.objects.all()          
            return render(request , "corredor.html" , {"corredor": corredor})
    else:
        mi_formulario = Corredor_formulario(initial={'nombre':corredor.nombre , "apellido":corredor.apellido , 'modalidad':corredor.modalidad , 'email':corredor.email , 'team':corredor.team})
    
    return render( request , "editar_corredor.html" , {"mi_formulario":mi_formulario, "corredor": corredor})


def editar_carreras( request , id):

    carreras = Carreras.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Carreras_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            carreras.nombre = datos['nombre']
            carreras.modalidad = datos['modalidad']
            carreras.distancia = datos['distancia']
            carreras.fecha = datos['fecha']
                              
            carreras.save()
            carreras = Carreras.objects.all()          
            return render(request , "carreras.html" , {"carreras": carreras})
    else:
        mi_formulario = Carreras_formulario(initial={'nombre':carreras.nombre , "modalidad":carreras.modalidad , 'distancia':carreras.distancia , 'fecha':carreras.fecha})
    
    return render( request , "editar_carreras.html" , {"mi_formulario":mi_formulario, "carreras": carreras})


def editar_teams( request , id):

    teams = Teams.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = Teams_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            teams.nombre = datos['nombre']
            teams.modalidad = datos['modalidad']
            teams.email = datos['email']
                              
            teams.save()
            teams = Teams.objects.all()          
            return render(request , "teams.html" , {"teams": teams})
    else:
        mi_formulario = Teams_formulario(initial={'nombre':teams.nombre , 'modalidad':teams.modalidad , 'email':teams.email})
    
    return render( request , "editar_teams.html" , {"mi_formulario":mi_formulario, "teams": teams})


def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request , data= request.POST)
        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request,user)
                avatares = Avatar.objects.filter(user=request.user.id)
                 
                if avatares.exists():
                    return render( request , "inicio.html" , {"url":avatares[0].imagen.url })
   
                else:

                    return render (request,"inicio.html")

            else:
                return HttpResponse(f"Usuario Incorrecto")
        else:         
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()

    return render( request , "login.html" , {"form":form})


def register(request):

    if request.method == "POST":
        
        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            ##return HttpResponse("Usuario Creado")
            return render (request,"registrado.html")

    else:
        form = UserCreationForm()
    
    return render( request , "registro.html" , {"form":form})

@login_required
def editar_perfil(request):

    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()
            
            return render(request , "inicio.html")
     
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render( request , "editar_perfil.html" , {'miFormulario':miFormulario , "usuario":usuario})

def perfil(request):

     return render( request , "perfil.html")

def post (request):
    post = Post.objects.all()
    dicc = {"post" : post}
    plantilla = loader.get_template ("post.html")
    documento = plantilla.render (dicc)
    return HttpResponse(documento)

@login_required
def postadm (request):
    post = Post.objects.all()
    dicc = {"post" : post}
    plantilla = loader.get_template ("postadm.html")
    documento = plantilla.render (dicc)
    return HttpResponse(documento)

def post_formulario(request):

    if request.method == "POST":

        mi_formulario = Post_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data


        post = Post( nombre = datos['nombre'] , mensaje = datos['mensaje'])
        post.save()
        return render(request , "formulario_post.html")

    return render (request, "formulario_post.html")

def elimina_post(request, id):
    
    post = Post.objects.get (id=id)
    post.delete()

    post = Post.objects.all()

    return render(request, "postadm.html", {"post": post})

# Create your views here.
