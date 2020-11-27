from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from spots.models import Spot
from chat.services import serialize_messages


@login_required
def spot_chat_room(request, spot_id):
    spot = get_object_or_404(Spot, pk=spot_id)
    messages = {'messages': serialize_messages(spot.messages.all())}
    return render(request, 'chat.html', {'spot': spot, 'messages': messages})
