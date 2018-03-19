from django import template

register = template.Library()


@register.inclusion_tag("comment_card.html")
def comment_card(comment):
    return {"comment": comment}
