from django.shortcuts import render, get_object_or_404, redirect, Http404
from .models import Section, TextSection, Text, SidePostSection, SidePost, \
    PostSection, Post, PostImage, Carousel, CarouselImage, GallerySection, Gallery, GalleryImage, NavigationBar, \
    BackgroundImage, Instruction, ImageSection, Image, InfoTab

numbers = []
for _ in range(25):
    numbers.append(_)


# Create your views here.
def base(request):
    sections = Section.objects.all()
    navigation_bar = NavigationBar.objects.first()
    background_image = BackgroundImage.objects.first()
    if (Instruction.objects.first() is None or Instruction.objects.first().On is False) and Section.objects.all():
        home_url = Section.objects.first().slug
    else:
        home_url = False

    context = {
        'home_url': home_url,
        'sections': sections,
        'navigation_bar': navigation_bar,
        'background_image': background_image,
    }
    if home_url:
        return redirect(f'/section/{home_url}')
    else:
        return render(request, 'main/base.html', context)


def section(request, slug):
    # ----------------section
    sections = Section.objects.all()
    current_section = get_object_or_404(Section, slug=slug)

    # --------------text
    text_sections = TextSection.objects.all()
    text = Text.objects.all()

    # --------------side_post
    side_post_sections = SidePostSection.objects.all()
    side_posts = SidePost.objects.all()

    # --------------posts
    post_sections = PostSection.objects.all()
    posts = Post.objects.all()

    # --------------carousels
    carousels = Carousel.objects.all()
    carousel_images = CarouselImage.objects.all()
    carousel_text_style = "color: white; text-shadow: black 0.1em 0.1em 0.2em"

    # --------------gallery
    gallery_sections = GallerySection.objects.all()
    galleries = Gallery.objects.all()

    # --------------navigation bar
    navigation_bar = NavigationBar.objects.first()
    background_image = BackgroundImage.objects.first()

    # --------------images
    image_section = ImageSection.objects.all()
    images = Image.objects.all()

    # ------------info tab
    info_tab = InfoTab.objects.all()
    context = {
        'sections': sections,
        'text_sections': text_sections,
        'text': text,
        'numbers': numbers,
        'current_section': current_section,
        'side_post_sections': side_post_sections,
        'side_posts': side_posts,
        'post_sections': post_sections,
        'posts': posts,
        'carousels': carousels,
        'carousel_images': carousel_images,
        'carousel_text_style': carousel_text_style,
        'gallery_sections': gallery_sections,
        'galleries': galleries,
        'navigation_bar': navigation_bar,
        'background_image': background_image,
        'image_section': image_section,
        'images': images,
        'info_tabs': info_tab,

    }
    return render(request, 'main/section.html', context)


def post_details(request, slug, post_slug):
    current_post = get_object_or_404(Post, post_slug=post_slug)
    current_section = get_object_or_404(Section, slug=slug)
    navigation_bar = NavigationBar.objects.first()
    sections = Section.objects.all()
    background_image = BackgroundImage.objects.first()
    images = PostImage.objects.all()
    context = {
        'navigation_bar': navigation_bar,
        'current_section': current_section,
        'current_post': current_post,
        'sections': sections,
        'background_image': background_image,
        'images': images,

    }
    return render(request, 'posts/details.html', context)


def gallery_details(request, slug, pk):
    gallery_section = GallerySection.objects.all()
    sections = Section.objects.all()
    filter_section = get_object_or_404(Gallery, pk=pk)
    images = GalleryImage.objects.filter(section=filter_section)
    navigation_bar = NavigationBar.objects.first()
    background_image = BackgroundImage.objects.first()

    context = {
        'navigation_bar': navigation_bar,
        'gallery_section': gallery_section,
        'current_section': get_object_or_404(Section, slug=slug),
        'sections': sections,
        'gallery': section,
        'images': images,
        'background_image': background_image,

    }
    return render(request, 'gallery/gallery_details.html', context)


def gallery1(request):
    sections = Section.objects.all()
    navigation_bar = NavigationBar.objects.first()
    background_image = BackgroundImage.objects.first()

    context = {
        'sections': sections,
        'navigation_bar': navigation_bar,
        'background_image': background_image,
    }
    if (Instruction.objects.first() is None or Instruction.objects.first().On is False) and Section.objects.all():
        return Http404()
    else:
        return render(request, 'main/gallery_detail/gallery1.html', context)


def gallery2(request):
    sections = Section.objects.all()
    navigation_bar = NavigationBar.objects.first()
    background_image = BackgroundImage.objects.first()

    context = {
        'sections': sections,
        'navigation_bar': navigation_bar,
        'background_image': background_image,
    }

    if (Instruction.objects.first() is None or Instruction.objects.first().On is False) and Section.objects.all():
        return Http404()
    else:
        return render(request, 'main/gallery_detail/gallery2.html', context)


def gallery3(request):
    sections = Section.objects.all()
    navigation_bar = NavigationBar.objects.first()
    background_image = BackgroundImage.objects.first()

    context = {
        'sections': sections,
        'navigation_bar': navigation_bar,
        'background_image': background_image,
    }

    if (Instruction.objects.first() is None or Instruction.objects.first().On is False) and Section.objects.all():
        return Http404()
    else:
        return render(request, 'main/gallery_detail/gallery3.html', context)


def post1(request):
    sections = Section.objects.all()
    navigation_bar = NavigationBar.objects.first()
    background_image = BackgroundImage.objects.first()

    context = {
        'sections': sections,
        'navigation_bar': navigation_bar,
        'background_image': background_image,
    }

    if (Instruction.objects.first() is None or Instruction.objects.first().On is False) and Section.objects.all():
        return Http404()
    else:
        return render(request, 'main/post_detail/post1.html', context)


def post2(request):
    sections = Section.objects.all()
    navigation_bar = NavigationBar.objects.first()
    background_image = BackgroundImage.objects.first()

    context = {
        'sections': sections,
        'navigation_bar': navigation_bar,
        'background_image': background_image,
    }

    if (Instruction.objects.first() is None or Instruction.objects.first().On is False) and Section.objects.all():
        return Http404()
    else:
        return render(request, 'main/post_detail/post2.html', context)


def post3(request):
    sections = Section.objects.all()
    navigation_bar = NavigationBar.objects.first()
    background_image = BackgroundImage.objects.first()

    context = {
        'sections': sections,
        'navigation_bar': navigation_bar,
        'background_image': background_image,
    }

    if (Instruction.objects.first() is None or Instruction.objects.first().On is False) and Section.objects.all():
        return Http404()
    else:
        return render(request, 'main/post_detail/post3.html', context)


def testing_post(request):
    return render(request, 'test/test.html', {})
