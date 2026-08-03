def review_security(diff):
 f=[]
 if "password" in diff.lower(): f.append("Hardcoded secret")
 return f
