from django.contrib import admin
from .models import Section, Text, TextSection, SidePostSection, SidePost, PostSection, Post, PostImage, CarouselImage, \
    Carousel, GallerySection, Gallery, GalleryImage, NavigationBar, BackgroundImage, Instruction, ImageSection, Image

# Register your models here.
admin.site.register(Section)
admin.site.register(Text)
admin.site.register(TextSection)


@admin.register(NavigationBar)
class NavigationBarAdmin(admin.ModelAdmin):
    class Meta:
        model = NavigationBar

    def has_add_permission(self, request, obj=None):
        if NavigationBar.objects.all():
            return False
        else:
            return True


@admin.register(BackgroundImage)
class BackgroundImageAdmin(admin.ModelAdmin):
    class Meta:
        model = BackgroundImage

    def has_add_permission(self, request, obj=None):
        if BackgroundImage.objects.all():
            return False
        else:
            return True


@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    class Meta:
        model = Instruction

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        if Instruction.objects.all():
            return False
        else:
            return True


class CarouselImageAdmin(admin.StackedInline):
    model = CarouselImage
    extra = 1


@admin.register(Carousel)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "order")
    inlines = [CarouselImageAdmin]

    class Meta:
        model = Carousel


@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(GallerySection)
admin.site.register(GalleryImage)


class GalleryImageAdmin(admin.StackedInline):
    model = GalleryImage
    extra = 1


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("title", "gallery_section", "created")
    inlines = [GalleryImageAdmin]

    class Meta:
        ordering = "gallery_section"
        model = Gallery


class ImageSectionAdmin(admin.StackedInline):
    model = Image
    extra = 1


@admin.register(ImageSection)
class PostAdmin(admin.ModelAdmin):
    inlines = [ImageSectionAdmin]

    class Meta:
        model = ImageSection


@admin.register(Image)
class ImageSectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(PostSection)
admin.site.register(PostImage)


class PostSectionAdmin(admin.StackedInline):
    model = PostImage
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostSectionAdmin]

    class Meta:
        model = Post


# admin.site.register(SidePostSection)
admin.site.register(SidePost)


class SidePostSectionAdmin(admin.StackedInline):
    model = SidePost
    extra = 1


@admin.register(SidePostSection)
class PostAdmin(admin.ModelAdmin):
    inlines = [SidePostSectionAdmin]

    class Meta:
        model = SidePost
