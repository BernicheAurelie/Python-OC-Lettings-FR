from django.shortcuts import render


# Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
# Quisque molestie quam lobortis leo consectetur ullamcorper non id est.
# Praesent dictum, nulla eget feugiat sagittis, sem mi convallis eros,
# vitae dapibus nisi lorem dapibus sem. Maecenas pharetra purus ipsum, 
# eget consequat ipsum lobortis quis. 
# Phasellus eleifend ex auctor venenatis tempus.
# Aliquam vitae erat ac orci placerat luctus. 
# Nullam elementum urna nisi, pellentesque iaculis enim cursus in. 
# Praesent volutpat porttitor magna, non finibus neque cursus id.
def index(request):
    """
    function to display home page, 
    returning index template for this project.
    """
    return render(request, "index.html")

def handler404(request, *args, **argv):
    """ function to custom 404 error page"""
    context = {}
    return render(request, "404.html", context)

def handler500(request, *args, **argv):
    """ function to custom 500 error page"""
    context = {}
    return render(request, "500.html", context)
