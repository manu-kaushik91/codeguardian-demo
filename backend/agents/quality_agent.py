def review_quality(diff):
 return ["Missing null check"] if ".get" in diff else []
