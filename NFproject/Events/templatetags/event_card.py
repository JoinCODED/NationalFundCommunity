from django import template

register = template.Library()


##############
# Custom Tags
##############
@register.inclusion_tag("event_card.html")
def event_card(event):
    return {"event": event}
