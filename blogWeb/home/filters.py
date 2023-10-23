from django import template

register = template.Library()

@register.filter
def group_comments_by_author(comments):
    grouped = {}
    for comment in comments:
        author_name = comment.author.name
        if author_name not in grouped:
            grouped[author_name] = []
        grouped[author_name].append(comment)
    return grouped.items()