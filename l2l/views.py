from datetime import datetime

from django.http import HttpResponse
from django.template import loader

from common.utils.dates import IS0_FORMAT


def index(request):
    now = datetime.now()
    template = loader.get_template("l2l/index.html")
    context = {"iso": now.strftime(IS0_FORMAT), "now": now}
    return HttpResponse(template.render(context, request))
