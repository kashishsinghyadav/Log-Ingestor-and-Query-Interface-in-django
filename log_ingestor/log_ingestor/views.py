from django.shortcuts import render
from django.db.models import Q
from log.models import Logl
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


@csrf_exempt
def ingest_log(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        log = Logl(
            level=data['level'],
            message=data['message'],
            resourceId=data['resourceId'],
            timestamp=data['timestamp'],
            traceId=data['traceId'],
            spanId=data['spanId'],
            commit=data['commit'],
            parentResourceId=data['metadata'].get('parentResourceId')
        )
        log.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})


def search_logs(request):
    query = request.GET.get('q', '')
    level = request.GET.get('level', '')
    resourceId = request.GET.get('resourceId', '')
    timestamp = request.GET.get('timestamp', '')

    # Basic example, adapt to your needs
    logs = Logl.objects.filter(
        Q(message__icontains=query) |
        Q(level__icontains=level) |
        Q(resourceId__icontains=resourceId) |
        Q(timestamp__icontains=timestamp)
    )

    return render(request, 'index.html', {'logs': logs})