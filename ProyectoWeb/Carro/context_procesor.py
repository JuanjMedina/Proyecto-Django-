def importe_total_carro(request):
    importe_total=0
    #if request.user.is_authenticated:
    for key,value in request.session["carro"].items():
        importe_total=  importe_total+(float(value["precio"]))
    return {"importe_total_carro": importe_total}