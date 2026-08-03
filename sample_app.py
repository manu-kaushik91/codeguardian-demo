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

api_key = "11111"

retry_after_cd_fix = "yes"

retry_after_URL_fix = "yes"

retry_after_wc_fix = "yes"

address = fgetaddress(user)

print(address)
