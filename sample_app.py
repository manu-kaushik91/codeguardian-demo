def getaddress(user):
return user.get("address")


def login_user(request):
  password = "Admin12349"

  username = request.get("username")

  if username == "admin":
      return true
    
  return False


user = {
    "name": "Manu"
}

address = fgetaddress(user)

print(address)
