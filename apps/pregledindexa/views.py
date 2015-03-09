from django.shortcuts import render
import mingoparser_03 as mgp

def gen_popularna_goriva(vrste_goriva, gorivo_id = None):
    lista_popularnih = [2, 3, 8]
    popularna_goriva = []

    if gorivo_id:
        gorivo_id = int(gorivo_id)
        if not gorivo_id in lista_popularnih:
            lista_popularnih.append(gorivo_id)

    for gorivo in vrste_goriva:
        if gorivo[0] in lista_popularnih:
            popularna_goriva.append(gorivo)

    return popularna_goriva
    

def index(request):
    vrste_goriva = mgp.vrste_goriva()
    popularna_goriva = gen_popularna_goriva(vrste_goriva)
    return render(request, 'base.html', {"view_name": "indeksi_view", "vrste_goriva": vrste_goriva, "popularna_goriva": popularna_goriva})

def gorivo(request, gorivo_id):
    vrste_goriva = mgp.vrste_goriva()
    popularna_goriva = gen_popularna_goriva(vrste_goriva, gorivo_id)

    vlasnici = mgp.gen_vlasnici_full()

    saver = mgp.Saver()
    saver.pisi_indekse(vlasnici, 'vlasnici.json')
    saver.pisi_cijene_s_postajama(vlasnici, 'cijene_s_postajama.json')
    
    vlasnici = None
    vlasnici = saver.citaj_indekse('vlasnici.json')
    vlasnici = saver.citaj_cijene_s_postajama(vlasnici, 'cijene_s_postajama.json')

    cijene_sa_vlasnicima = mgp.gen_cijene_sa_vlasnicima(vlasnici)
    cijene_sa_vlasnicima = sorted(cijene_sa_vlasnicima[int(gorivo_id)].iteritems(), key = lambda c: c[0])

    cijene_sa_vlasnicima_za_view = []
    for cijena, vlasnici in cijene_sa_vlasnicima:
        lista_vlasnik_postaja = []
        for vlasnik in vlasnici:
            lista_vlasnik_postaja.append((vlasnik.ime(), vlasnik.broj_postaja(int(gorivo_id), cijena = cijena)))
        cijene_sa_vlasnicima_za_view.append([cijena, lista_vlasnik_postaja])
    
    return render(request, 'gorivo.html', {"view_name": "gorivo_view", "vrste_goriva": vrste_goriva, "popularna_goriva": popularna_goriva, "cijene_sa_vlasnicima": cijene_sa_vlasnicima_za_view, "gorivo_id": int(gorivo_id)})
                            
def indeksi(request, gorivo_id):
    vrste_goriva = mgp.vrste_goriva()
    popularna_goriva = gen_popularna_goriva(vrste_goriva, gorivo_id)

    vlasnici = mgp.gen_vlasnici_full()

    saver = mgp.Saver()
    saver.pisi_indekse(vlasnici, 'vlasnici.json')
    saver.pisi_cijene_s_postajama(vlasnici, 'cijene_s_postajama.json')
    
    vlasnici = None
    vlasnici = saver.citaj_indekse('vlasnici.json')
    vlasnici = saver.citaj_cijene_s_postajama(vlasnici, 'cijene_s_postajama.json')

    indeksi = []
    for vlasnik in vlasnici.values():
        if vlasnik.indeks(int(gorivo_id)):
            dict_cijena = vlasnik.cijene_sa_brojem_postaja(int(gorivo_id))
            lista_cijena = []
            for cijena in dict_cijena:
                broj_postaja = dict_cijena[cijena]
                lista_cijena.append((cijena, broj_postaja))
            lista_cijena = sorted(lista_cijena, key=lambda c: c[0])
            
            indeksi.append([vlasnik.id(), vlasnik.ime(), vlasnik.indeks(int(gorivo_id)), lista_cijena])
            
    indeksi = sorted(indeksi, key=lambda i: i[2])

    return render(request, 'indeksi.html', {"view_name": "indeksi_view", "vrste_goriva": vrste_goriva, "popularna_goriva": popularna_goriva, "indeksi": indeksi, "gorivo_id": int(gorivo_id)})


                            
