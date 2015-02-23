from django.shortcuts import render
import mingoparser_01 as mgp


def index(request):
    vrste_goriva = mgp.vrste_goriva()
    return render(request, 'index.html', {"vrste_goriva": vrste_goriva})

def gorivo(request, gorivo_id):
    vrste_goriva = mgp.vrste_goriva()
    cijene_sa_vlasnicima = mgp.main(gorivo_id)
    return render(request, 'gorivo.html', {"vrste_goriva": vrste_goriva, "cijene_sa_vlasnicima": cijene_sa_vlasnicima, "gorivo_id": int(gorivo_id)})


                            
