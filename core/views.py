from django.shortcuts import render
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = 'core/base-list.html'


def coinDeterminer(request):
    coins_list = [ 1, 5, 7, 9, 11]
    coin = int(request.GET.get('coin'))
    change_count, change_final = 0, True,

    if coin in coins_list or coin == 0:
        change_count = 0

    while change_final == True:
        for coin_result in reversed(coins_list):
            if coin >=  coin_result:
                coin = coin - coin_result
                change_count += 1
                if coin == 0:
                    change_final = False
                break

    return render(request, 'core/base-result.html', {'change_count': change_count})