from django import template

register = template.Library()


##############
# Custom Tags
##############
@register.inclusion_tag("profile_card.html")
def profile_card(profile):
    return {"profile": profile}
