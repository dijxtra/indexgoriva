from django.shortcuts import render
import mingoparser_02 as mgp


def index(request):
    vrste_goriva = mgp.vrste_goriva()
    return render(request, 'index.html', {"vrste_goriva": vrste_goriva})

def gorivo(request, gorivo_id):
    vrste_goriva = mgp.vrste_goriva()

    cijene_sa_vlasnicima = mgp.gen_cijene_sa_vlasnicima(gorivo_id, limit = 4)

    return render(request, 'gorivo.html', {"vrste_goriva": vrste_goriva, "cijene_sa_vlasnicima": cijene_sa_vlasnicima, "gorivo_id": int(gorivo_id)})
                            
def indeksi(request, gorivo_id):
    vrste_goriva = mgp.vrste_goriva()

    cijene_sa_vlasnicima = mgp.gen_cijene_sa_vlasnicima(gorivo_id, limit = 4)
    vlasnici_sa_cijenama = mgp.gen_vlasnici_sa_cijenama(cijene_sa_vlasnicima)
    vlasnici_sa_cijenama.sort(key=lambda x: x.index())

    return render(request, 'indeksi.html', {"vrste_goriva": vrste_goriva, "cijene_sa_vlasnicima": cijene_sa_vlasnicima, "vlasnici_sa_cijenama": vlasnici_sa_cijenama, "gorivo_id": int(gorivo_id)})


                            
