from chartit import DataPool, Chart
from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from wttxApp.models import WTTX_SERVICE_LOGS
from django.shortcuts import render


def wttx(request):
    a = WTTX_SERVICE_LOGS.objects.all().values('DESCRIPTION').annotate(total=Count('DESCRIPTION')).order_by(
        'DESCRIPTION')
    wttx = DataPool(
        series=
        [{'options': {
            # 'source': SalesReport.objects.all()},
            # 'source': SalesReport.objects.filter(sales__lte=20.00)},
            'source': WTTX_SERVICE_LOGS.objects.all().values('DESCRIPTION').annotate(
                total=Count('DESCRIPTION')).order_by(
                'total')},
            'terms': [{'DESCRIPTION': 'DESCRIPTION', 'total': 'total'}]
        }

        ])

    # sales = DataPool(
    #     series=
    #     [{'options': {
    #         'source': SalesReport.objects.filter(sales_lte=20.00)},
    #         'terms': [{
    #                 'month': 'month',
    #                 'sales': 'sales'}]
    #
    #     ])

    cht = Chart(
        datasource=wttx,
        series_options=
        [{'options': {
            'type': 'column',
            'stacking': False},
            'terms': {
                'DESCRIPTION': [
                    'total']
            }}],
        chart_options=
        {'title': {
            'text': 'WTTX Amount Over Months'},
            'xAxis': {
                'title': {'text': 'WTTX Total'}},
            'yAxis': {
                'title': {'text': 'WTTX Number'}}})

    cht2 = Chart(
        datasource=wttx,
        series_options=
        [{'options': {
            'type': 'pie',
            'stacking': False},
            'terms': {
                'DESCRIPTION': [
                    'total']
            }}],
        chart_options=
        {'title': {
            'text': 'WTTX Amount Over Query - Pie Chart'},
            'xAxis': {
                'title': {'text': 'WTTX Total'}},
            'yAxis': {
                'title': {'text': 'WTTX Number'}}})

    return render(request, 'wttx.html', {'chart_list': [cht, cht2]})
