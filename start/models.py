from django.db import models

# x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
# def get_ip(request):
#     try:
#         x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
#         if x_forward:
#             ip = x_forward.split(",")[0]
#         else:
#             ip = request.META.get("REMOTE_ADDR")
#     except:
#         ip = ""
#     return ip
def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class Newsletter(models.Model):
    email = models.EmailField()
    heading=models.CharField(max_length=200)
    # friend = models.ForeignKey("self", related_name='referral', on_delete=models.CASCADE, null=True, blank=True)
    # ref_id = models.CharField(max_length=120, default='ABC', unique=True)
    # ip = models.CharField(max_length=100,default='hero')
    # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    # updated = models.DateTimeField(auto_now_add=False, auto_now=True)



    def __str__(self):
        return self.email

class News(models.Model):
    heading = models.CharField(max_length=200)

    def __str__(self):
        return self.heading

class Fileupload(models.Model):
    file= models.FileField(blank=False,null=False,max_length=200)

class htmlupload(models.Model):
    file = models.TextField(blank=False, null=False, max_length=1000000000)

class newshtmlupload(models.Model):
    file = models.FileField(blank=False, null=False, max_length=200)
    #
    # def __str__(self):
    #     return self.File

        # friend = models.ForeignKey("self", related_name='referral', on_delete=models.CASCADE, null=True, blank=True)
        # ref_id = models.CharField(max_length=120, default='ABC', unique=True)
        # ip = models.CharField(max_length=100,default='hero')
        # timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
        # updated = models.DateTimeField(auto_now_add=False, auto_now=True)



    # def get_ip(request):
    #     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    #     if x_forwarded_for:
    #         ip = x_forwarded_for.split(',')[0]
    #     else:
    #         ip = request.META.get('REMOTE_ADDR')
    #     return ip
    # #


    # def home(request):
    #
    #     form = JoinForm(request.POST or None)
    #     if form.is_valid():
    #         new_join = form.save(commit=False)
    #         email = form.cleaned_data['email']
    #         new_join_old, created = Newsletter.objects.get_or_create(email=email)
    #         new_join_old.ip_address = get_ip(request)
    #         new_join_old.save()
    #
    #         return HttpResponseRedirect("/%s" % ("thankyou"))
    #
    #     context = {"form": form}
    #     template = "home.html"
    #     return render(request, template, context)
