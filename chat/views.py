from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from spots.models import Spot


@login_required
def spot_chat_room(request, spot_id):
    spot = get_object_or_404(Spot, pk=spot_id)
    return render(request, 'chat.html', {})
