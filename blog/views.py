from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "trail-run",
        "image": "mountains.jpg",
        "author": "david",
        "date": date(2021, 12, 21),
        "title": "Trail Running",
        "excerpt": "There's nothing like trail running in Western NC! I was not prepared for what I saw!",
        "content": """
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias vero veniam corporis aliquid ipsum quia! Voluptatum, cupiditate aperiam? Vitae, tempora expedita sint ab mollitia ipsam? Quas corrupti temporibus quae quo.
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias vero veniam corporis aliquid ipsum quia! Voluptatum, cupiditate aperiam? Vitae, tempora expedita sint ab mollitia ipsam? Quas corrupti temporibus quae quo.
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Alias vero veniam corporis aliquid ipsum quia! Voluptatum, cupiditate aperiam? Vitae, tempora expedita sint ab mollitia ipsam? Quas corrupti temporibus quae quo.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html")


def post_detail(request, slug):
    return render(request, "blog/post-detail.html")
