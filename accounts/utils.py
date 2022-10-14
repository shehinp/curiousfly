import pytz
from django.utils.translation import gettext_lazy as _

JOB_TITLE = (
    ("Principal Architect", "Principal Architect"),
    ("Principal Designer", "Principal Designer"),
    ("Executive Director", "Executive Director"),
    ("Co-Founder", "Co-Founder"),
    ("Architect", "Architect"),
    ("Admin", "Admin"),
    ("HR", "HR"),
    ("Junior Architect", "Junior Architect"),
    ("Senior Architect", "Senior Architect"),
    ("Senior Consultant", "Senior Consultant"),
    ("Project Coordinator", "Project Coordinator"),
    ("Principal Consultant", "Principal Consultant"),
    ("Proprietor", "Proprietor"),
    ("Director", "Director"),
    ("Manager", "Manager"),
    ("Person In charge", "Person In charge"),
    ("CEO", "CEO"),
    ("Founder and Chairman", "Founder and Chairman"),
    ("Chief Architect", "Chief Architect"),
    ("Managing Director", "Managing Director"),
    ("Project Head", "Project Head"),
    ("Project Director", "Project Director"),
    ("Project Manager", "Project Manager"),
    ("Associate", "Associate"),
    ("Project Associate", "Project Associate"),
    ("Interior Designer", "Interior Designer"),
    ("Partner", "Partner"),
    ("Chief Designer", "Chief Designer"),
)


INDUSTRIES = (
    ("Builder", "Builder"),
    ("Small Scale Builder", "Small Scale Builder"),
    ("Associate 3rd Party Vendor", "Associate 3rd Party Vendor"),
    ("Architect's Firm", "Architect's Firm"),
    ("Network Electrician", "Network Electrician"),
    ("Interior Designer's Firm", "Interior Designer's Firm"),
    ("Electrical consultant", "Electrical consultant"),
    ("Partner", "Partner"),
    ("Associates", "Associates"),
    ("Competitor", "Competitor"),
    ("Electrical Contractor", "Electrical Contractor"),
    ("Individual Customer", "Individual Customer"),
    ("Electrician", "Electrician"),
    ("Integrator", "Integrator"),
    ("Agent", "Agent"),
    ("Domain experts in other fields", "Domain experts in other fields"),
    ("PMC", "PMC"),
    ("Civil Contractor", "Civil Contractor"),
)

INDUSTRIES = (
    ("Builder", "Builder"),
    ("Small Scale Builder", "Small Scale Builder"),
    ("Associate 3rd Party Vendor", "Associate 3rd Party Vendor"),
    ("Architect's Firm", "Architect's Firm"),
    ("Network Electrician", "Network Electrician"),
    ("Interior Designer's Firm", "Interior Designer's Firm"),
    ("Electrical consultant", "Electrical consultant"),
    ("Partner", "Partner"),
    ("Associates", "Associates"),
    ("Competitor", "Competitor"),
    ("Electrical Contractor", "Electrical Contractor"),
    ("Individual Customer", "Individual Customer"),
    ("Electrician", "Electrician"),
    ("Integrator", "Integrator"),
    ("Agent", "Agent"),
    ("Domain experts in other fields", "Domain experts in other fields"),
    ("PMC", "PMC"),
    ("Civil Contractor", "Civil Contractor"),
)

LEAD_SOURCE = (
    ("Facebook Advertisement", "Facebook Advertisement"),
    ("Google adwords", "Google adwords"),
    ("Magazine advertisement", "Magazine advertisement"),
    ("Web research", "Web research"),
    ("Referral", "Referral"),
    ("Agent", "Agent"),
    ("PR", "PR"),
    ("Not Known", "Not Known"),
    ("Scouting", "Scouting"),
)

RATINGS = (
    ("Acquired", "Acquired"),
    ("Active", "Active"),
    ("Market Failed", "Market Failed"),
    ("Project Cancelled", "Project Cancelled"),
    ("ShutDown", "ShutDown"),
)

CURRENCIES = (
    ("INR", "INR"),
)

MEMBER_STATUS = (
    ("Not Added", "Not Added"),
    ("Added Member", "Added Member"),
)

ACCOUNT_TIER = (
    ("Tier A+", "Tier A+"),
    ("Tier A", "Tier A"),
    ("Tier B+", "Tier B+"),
    ("Tier B", "Tier B"),
    ("Tier C", "Tier C"),
)

PRIORITY = (
    ("LOW", "LOW"),
    ("MEDIUM", "MEDIUM"),
    ("HIGH", "HIGH"),
    ("NORMAL", "NORMAL"),
)

CF_ACCOUNT_STATUS = (
    ("Not yet Visited", "Not yet Visited"),
    ("Neutral", "Neutral"),
    ("Considering CF", "Considering CF"),
    ("Will Refer", "Will Refer"),
    ("Associated with CF", "Associated with CF"),
    ("Will Consider", "Will Consider"),
    ("Not Interested", "Not Interested"),
    ("Associated with Competitor", "Associated with Competitor"),
    ("Need To Boost", "Need To Boost"),
    ("Lost Account", "Lost Account"),
    ("Permanant Lost Account", "Permanant Lost Account"),
    ("Junk", "Junk"),
)

FOLLOW_UP_STATUS = (
    ("not contacted", "Not Contacted"),
    ("not contacted high priority", "Not Contacted High Priority"),
    ("Attempted to Contact", "Attempted to Contact"),
    ("Need to Visit 1", "Need to Visit 1"),
    ("Tried For Appointment 1", "Tried For Appointment 1"),
    ("Appointment Scheduled 1", "Appointment Scheduled 1"),
    ("visited 1", "Visited 1"),
    ("call 1", "call 1"),
    ("Need to Visit 2", "Need to Visit 2"),
    ("tried for appointment 2", "Tried for Appointment 2"),
    ("appointment scheduled 2", "Appointment Scheduled 2"),
    ("visited 2", "Visited 2"),
    ("call 2", "call 2"),
    ("need to visit 3", "Need to Visit 3"),
    ("tried for appointment 3", "Tried for Appointment 3"),
    ("appointment scheduled 3", "Appointment Scheduled 3"),
    ("visited 3", "Visited 3"),
    ("call 3", "call 3"),
    ("need to visit 4", "Need to Visit 4"),
    ("tried for appointment 4", "Tried for Appointment 4"),
    ("appointment scheduled 4", "Appointment Scheduled 4"),
    ("visited 4", "Visited 4"),
    ("call 4", "call 4"),
    ("need to visit 5", "Need to Visit 5"),
    ("tried for appointment 5", "Tried for Appointment 5"),
    ("appointment scheduled 5", "Appointment Scheduled 5"),
    ("visited 5", "Visited 5"),
    ("call 5", "call 5"),
    ("need to visit 5", "Need to Visit 5"),
    ("tried for appointment 5", "Tried for Appointment 5"),
    ("appointment scheduled 5", "Appointment Scheduled 5"),
    ("visited 5", "Visited 5"),
    ("call 5", "call 5"),

)
