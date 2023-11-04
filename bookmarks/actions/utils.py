import datetime
from django.contrib.contenttypes.models import ContentType
from . models import Action
from django.utils import timezone



def create_action(user, verb, target=None):
    """
    create func to check if the user created the same
    object in last minute or not
    """
    now = timezone.now()
    last_minute = now - datetime.timedelta(seconds=60)
    simialr_actions = Action.objects.filter(user_id=user.id,
                                            verb= verb,
                                            created__gte=last_minute)
    

    if target:
        target_ct = ContentType.objects.get_for_model(target)
        simialr_actions = Action.objects.filter(target_ct=target_ct,
                                                target_id=target.id)
        
    if not simialr_actions:
        action = Action(user=user, verb=verb, target=target)
        action.save()
        return True
    return False