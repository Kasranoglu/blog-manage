CREATIVE_UNIQUE = 'creative-unique'
CATEGORY_RESPONSIVE_TEMPLATES = 'responsive-templates'
CATEGORY_CREATIVE_IDEAS = 'creative-ideas'
CATEGORY_AWESOME_LAYOUTS = 'awesome-layouts'
CATEGORY_NATURE_LIFESTYLE = 'nature-lifestyle'

CATEGORY_CHOICES = (
    (CREATIVE_UNIQUE, 'Nature Lifestyle'),
    (CATEGORY_RESPONSIVE_TEMPLATES, 'Awesome Layouts'),
    (CATEGORY_CREATIVE_IDEAS, 'Creative Ideas'),
    (CATEGORY_AWESOME_LAYOUTS, 'Responsive Templates'),
    (CATEGORY_NATURE_LIFESTYLE, 'Creative & Unique')
)

STATUS_DRAFT = 'draft'
STATUS_PUBLISHED = 'published'

STATUS_CHOICES = (
    (STATUS_DRAFT, 'Draft'),
    (STATUS_PUBLISHED, 'Published')
)

DEFAULT_BLOG_IMAGE = 'blog-thumb-03_kQncFpU.jpg'

IMAGE_DEFAULT = (
    (DEFAULT_BLOG_IMAGE, 'blog-thumb-03_kQncFpU.jpg')
)

CONFIRMATION_CONFIRMED = 'confirmed'
CONFIRMATION_WAIT = 'wait'

CONFIRMATION_CHOICES = (
    (CONFIRMATION_CONFIRMED, 'Confirmed'),
    (CONFIRMATION_WAIT, 'Wait')

)
