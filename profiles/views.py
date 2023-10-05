from django.shortcuts import render, get_object_or_404
from .models import Profile
from utils import logger


# Sed placerat quam in pulvinar commodo.
# Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget.
# Fusc faucibus, urna quis auctor pharetra,
# massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
    function to get all profiles list,
    return profiles/index template with all profiles objects in context
    """
    logger.debug("profiles_index view with profiles list")
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui.
# Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla,
# eros leo tristique lacus,
# it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    function to display details on a profile,
    selecting it by its user's username
    return profile/profile template with profile favorite_city
    and associated user's informations in context
    """
    logger.debug("profile view with favorite_city and user's informations")
    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
