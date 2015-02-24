from django.shortcuts import render
import mingoparser_02 as mgp

def gen_popularna_goriva(vrste_goriva):
    lista_popularnih = [2, 8]
    popularna_goriva = []
    
    for gorivo in vrste_goriva:
        if gorivo[0] in lista_popularnih:
            popularna_goriva.append(gorivo)

    return popularna_goriva
    

def index(request):
    vrste_goriva = mgp.vrste_goriva()
    popularna_goriva = gen_popularna_goriva(vrste_goriva)
    return render(request, 'index.html', {"vrste_goriva": vrste_goriva, "popularna_goriva": popularna_goriva})

def gorivo(request, gorivo_id):
    vrste_goriva = mgp.vrste_goriva()
    popularna_goriva = gen_popularna_goriva(vrste_goriva)

    cijene_sa_vlasnicima = mgp.gen_cijene_sa_vlasnicima(gorivo_id, limit = 4)

    return render(request, 'gorivo.html', {"vrste_goriva": vrste_goriva, "popularna_goriva": popularna_goriva, "cijene_sa_vlasnicima": cijene_sa_vlasnicima, "gorivo_id": int(gorivo_id)})
                            
def indeksi(request, gorivo_id):
    vrste_goriva = mgp.vrste_goriva()
    popularna_goriva = gen_popularna_goriva(vrste_goriva)

    cijene_sa_vlasnicima = mgp.gen_cijene_sa_vlasnicima(gorivo_id, limit = 4)
    vlasnici_sa_cijenama = mgp.gen_vlasnici_sa_cijenama(cijene_sa_vlasnicima)
    vlasnici_sa_cijenama.sort(key=lambda x: x.index())

    return render(request, 'indeksi.html', {"vrste_goriva": vrste_goriva, "popularna_goriva": popularna_goriva, "vlasnici_sa_cijenama": vlasnici_sa_cijenama, "gorivo_id": int(gorivo_id)})


                            
