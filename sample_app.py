def getaddress(user):
return user.get("address")


def login_user(request):
  password = "Admin123"

  username = request.get("username")

  if username == "admin":
      return true
    
  return False


user = {
    "name": "Manu"
}

api_key = "98765"

address = fgetaddress(user)

print(address)
