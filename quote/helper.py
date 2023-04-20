from django.contrib.auth.models import User
"""
HELPER FUNCTIONS
"""
# helper function to check and see if the user is in the Testing group and is sampleadminuser. 
def is_in_testing_group(request):
    return request.user.groups.filter(name="Testing")

# def is_sampleadminuser(request):
#     return User.objects.filter(username="sampleadminuser")