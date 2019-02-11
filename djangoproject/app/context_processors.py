def user_processor(request):
 context = {
  'user': request.user,
 }
 return context
