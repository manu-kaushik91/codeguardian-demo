from .security_agent import review_security
from .quality_agent import review_quality
from .test_agent import generate_tests
from .defect_agent import defect_match
def run_review(diff):
 s=review_security(diff); q=review_quality(diff); d=defect_match(diff); t=generate_tests(diff)
 return {"risk":len(s)+len(q)+len(d),"security":s,"quality":q,"defects":d,"tests":t}
