from django.shortcuts import render


def products(request):
    links_menu = [
        {'href': 'products_tacheometrs', 'name': 'тахеометры'},
        {'href': 'products_gnss_equipmant', 'name': 'гнсс оборудование'},
        {'href': 'products_3D_scanner', 'name': '3D сканеры'},
        {'href': 'products_radio_station', 'name': 'Радиостанции'},
        {'href': 'products_laser_rangefinder', 'name': 'Лазерные дальномерыы'},
    ]
    context = {
        'links_menu': links_menu,
    }
    return render(request=request, template_name='mainapp/products.html', context=context)
