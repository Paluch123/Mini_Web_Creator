from django.db import models


# Create your models here.
class Section(models.Model):
    """Model for adding sections and enabling features"""
    title = models.CharField(max_length=25, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    enable_text = models.BooleanField(default=True)
    enable_side_posts = models.BooleanField(default=True)
    enable_galleries = models.BooleanField(default=True)
    enable_posts = models.BooleanField(default=True)
    enable_images = models.BooleanField(default=True)
    enable_carousel = models.BooleanField(default=True)
    enable_info_tab = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    on_site = models.BooleanField(default=True)

    # enable_contact_form = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class TextSection(models.Model):
    """choose which section u want your text to be in(section),
     also where your text will be placed comparing to other features(order)"""

    title = models.CharField(max_length=100, default='not created yet or title not changed')
    section = models.OneToOneField(Section, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.section.title + ' ' + self.title


class Text(models.Model):
    """choose your alignment, html text type, font"""

    order = models.IntegerField(default=0)
    AlignChoices = (
        ('center', 'center'),
        ('left', 'left'),
        ('right', 'right'),
        ('justify', 'justify'),

    )
    FontChoices = (
        ('', 'default'),
        ('\'Montserrat\', sans-serif;', 'Montserrat'),
        ('\'Oswald\', sans-serif;', 'Oswald'),
        ('\'Roboto\', sans-serif;', 'Roboto'),
        ('\'RocknRoll One\', sans-serif;', 'RocknRoll One'),
        ('\'Stick\', sans-serif;', 'Stick'),
    )
    TextChoices = (
        ('p', 'p'),
        ('h1', 'h1'),
        ('h2', 'h2'),
        ('h3', 'h3'),
        ('h4', 'h4'),
        ('h5', 'h5'),
        ('h6', 'h6'),
        ('pre', 'pre'),

    )
    section = models.ForeignKey(TextSection, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024, blank=True)
    align = models.CharField(max_length=100, default='left', choices=AlignChoices)
    text_choice = models.CharField(max_length=100, default='p', choices=TextChoices)
    font = models.CharField(max_length=100, default='default', choices=FontChoices, blank=True)
    your_summary = models.CharField(default='not defined', max_length=50)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.your_summary + self.section.title

    class Meta:
        ordering = ['-created']

        def __unicode__(self):
            return u'%s' % self.title


class SidePostSection(models.Model):
    """Choose section, hover effect for side posts"""

    StyleChoices = (
        ('hovereffect', 'hover effect #1'),
        ('hovereffect2', 'hover effect #2'),
        ('hovereffect3', 'hover effect #3'),
        ('', 'None'),

    )

    order = models.IntegerField(default=0)
    title = models.CharField(max_length=100, default='not named yet')
    section = models.OneToOneField(Section, on_delete=models.CASCADE)
    style = models.CharField(max_length=100, default='hover effect #1', choices=StyleChoices, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.section.title + ' ' + self.title


class SidePost(models.Model):
    """Side post content, orientation"""

    SideChoices = (
        ('LEFT', 'left'),
        ('RIGHT', 'right'),
    )
    post_section = models.ForeignKey(SidePostSection, on_delete=models.CASCADE)
    heading = models.CharField(max_length=25)
    heading2 = models.CharField(max_length=25, blank=True)
    description = models.TextField(max_length=1024)
    image_title = models.CharField(blank=True, max_length=25)
    image = models.FileField(upload_to='side_post_images/')
    enable_link = models.BooleanField(default=True)
    link = models.CharField(blank=True, max_length=100)
    side = models.CharField(max_length=100, default='LEFT', choices=SideChoices)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        ordering = ['-created']

        def __unicode__(self):
            return u'%s' % self.title


class PostSection(models.Model):
    """Choose section for post"""

    order = models.IntegerField(default=0)
    title = models.CharField(max_length=100, default='not created yet or title not changed')
    section = models.OneToOneField(Section, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.section.title


class Post(models.Model):
    """Post's content"""
    post_section = models.ForeignKey(PostSection, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    post_slug = models.SlugField(max_length=255, unique=True)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    enable_images = models.BooleanField(default=False)
    link = models.URLField(blank=True, max_length=255)

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-created']

        def __unicode__(self):
            return u'%s' % self.title


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post\'s_images', blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.post.title


class Carousel(models.Model):
    """choose section for your carousel, set first image, description, header, title"""
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=50)
    section = models.OneToOneField(Section, on_delete=models.CASCADE)
    head_image = models.ImageField(blank=True, upload_to='carousel_images')
    centered_header = models.CharField(max_length=255, blank=True)
    header = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=150, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.section.title + ' ' + self.title


class CarouselImage(models.Model):
    """add on another images for your carousel, set headers etc."""
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, upload_to='carousel_images')
    centered_header = models.CharField(max_length=255, blank=True)
    header = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=150, blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.header + ' in ' + str(self.carousel)


class GallerySection(models.Model):
    """create gallery sections, choose hover effect, title etc."""
    StyleChoices = (
        ('hovereffect', 'hover effect #1'),
        ('hovereffect2', 'hover effect #2'),
        ('hovereffect3', 'hover effect #3'),

    )
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=100, default='not named yet')
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    style = models.CharField(max_length=100, default='hovereffect', choices=StyleChoices)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.section.title + ' ' + self.title


class Gallery(models.Model):
    """choose gallery sections, set front image, description, image title"""
    gallery_section = models.ForeignKey(GallerySection, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.FileField(blank=True, upload_to='gallery_images/')
    image_title = models.CharField(max_length=50, default='some title')
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    """choose gellery and upload image to it"""
    section = models.ForeignKey(Gallery, default=None, on_delete=models.CASCADE)
    image = models.FileField(upload_to='gallery_images/')
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.section.title


class NavigationBar(models.Model):
    """Choose your logo image, navbar style and title(for example your company name)"""
    StyleChoices = (
        ('navbar navbar-expand-sm bg-light navbar-light', 'light'),
        ('navbar navbar-expand-sm bg-dark navbar-dark', 'dark'),
        ('navbar navbar-expand-sm bg-primary navbar-dark', 'blue'),
        ('navbar navbar-expand-sm bg-success navbar-dark', 'green'),
        ('navbar navbar-expand-sm bg-info navbar-dark', 'turquoise'),
        ('navbar navbar-expand-sm bg-warning navbar-dark', 'yellow'),
        ('navbar navbar-expand-sm bg-danger navbar-dark', 'red'),
        ('navbar navbar-expand-sm bg-secondary navbar-dark', 'grey'),

    )
    style = models.CharField(max_length=100, default='light', choices=StyleChoices)
    side_text = models.CharField(max_length=50, blank=True)
    logo_image = models.FileField(upload_to='logo_images/')
    title = models.CharField(max_length=50, blank=True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return 'your logo'


class BackgroundImage(models.Model):
    """you can add your image background and it's opacity here"""
    OpacityChoices = (
        (0.1, 0.1),
        (0.2, 0.2),
        (0.3, 0.3),
        (0.4, 0.4),
        (0.5, 0.5),
        (0.6, 0.6),
        (0.7, 0.7),
        (0.8, 0.8),
        (0.9, 0.9),
        (1.0, 1.0),
    )

    image = models.ImageField(upload_to='background_images/')
    opacity = models.FloatField(choices=OpacityChoices, default=1.0)

    def __str__(self):
        return "Background Image"


class Instruction(models.Model):
    """turn on and off instruction page, remember it won't turn off if no sectons are added"""
    On = models.BooleanField(default=True)

    def __str__(self):
        return "ON/OFF"


class ImageSection(models.Model):
    """choose where would u like to have your images"""
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=100, default='not created yet or title not changed')
    section = models.OneToOneField(Section, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.section.title


class Image(models.Model):
    """choose what and which section would u like to have your images"""
    image = models.ImageField(upload_to='images_images/', blank=True)
    image_section = models.ForeignKey(ImageSection, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, blank=True)


class InfoTab(models.Model):
    """set section and order also image, heading, content and link to every out of 3 tab"""
    title = models.CharField(max_length=25, default='info tab')
    section = models.OneToOneField(Section, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)
    img1 = models.ImageField(upload_to="info_tab_images/")
    heading1 = models.CharField(max_length=50)
    content1 = models.TextField(max_length=255)
    link1 = models.URLField()
    img2 = models.ImageField(upload_to="info_tab_images/")
    heading2 = models.CharField(max_length=50)
    content2 = models.TextField(max_length=255)
    link2 = models.URLField()
    img3 = models.ImageField(upload_to="info_tab_images/")
    heading3 = models.CharField(max_length=50)
    content3 = models.TextField(max_length=255)
    link3 = models.URLField()
