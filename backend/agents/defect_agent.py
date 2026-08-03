H=["null validation","logging"]
def defect_match(diff):
 return ["Historical defect: null validation"] if "getAddress" in diff else []
