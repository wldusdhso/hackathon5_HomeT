from django import template

register = template.Library()

@register.filter
def add_link(value):
    hashtagBox = value.hashtagBox
    tags = value.hashtags.all()

    for tag in tags:
        hashtagBox = hashtagBox.replace(f"{tag.content}", f"<a href='/videopage/hashtags/{tag.id}/'>{tag.content}</a>")
    
    return hashtagBox