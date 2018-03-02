""" Return images from context folder
"""
try:
    images = context.getFolderContents(
        contentFilter={'portal_type': ['Image']},
        full_objects=True
    )
except Exception:
    return []

return images
