from .models import Subscriber

def user_profile(request):

    if request.user.is_anonymous:
        pass

    else: 
        if request.user.is_authenticated:
            subscriber = Subscriber.objects.get(user=request.user)

            user_data = {
                'subscriber': subscriber,
            }

            return user_data
    return {}

