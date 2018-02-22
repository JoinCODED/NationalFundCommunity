from django import template

register = template.Library()


##############
# Custom Tags
##############
@register.inclusion_tag("article_card.html")
def article_card(article):
    return {"article": article}