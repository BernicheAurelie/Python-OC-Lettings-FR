from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile


# Create your views here.

# Sed placerat quam in pulvinar commodo. 
# Nullam laoreet consectetur ex, 
# sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, 
# quis dictum lacus d
def index(request):
    """
    function to get all profiles list, 
    return profiles/index template with all profiles objects in context
    """
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
    profile = get_object_or_404(Profile, user__username=username)
    # profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)

# def profile(request, username):
#     """
#     function to display details on a profile, 
#     selecting it by its user's username
#     return profile/profile template with profile favorite_city 
#     and associated user's informations in context
#     """
#     try:
#         profile = Profile.objects.get(user__username=username)
#         context = {"profile": profile}
#         return render(request, "profiles/profile.html", context)
#     except ObjectDoesNotExist:
#         return render(request, "404.html")
    