import os
from pathlib import Path

from app import app
from models import BlogPost

BASE_DIR = Path(__file__).resolve().parent
PUBLIC_DIR = BASE_DIR / "public"
STATIC_DIR = BASE_DIR / "static"

ROUTES = [
    "/",
    "/about",
    "/training-programs",
    "/corporate-training",
    "/computer-sales",
    "/computer-repairs",
    "/services",
    "/gallery",
    "/testimonials",
    "/blog",
    "/faq",
    "/privacy-policy",
    "/terms",
    "/contact",
    "/book-training",
]


def route_to_output_path(route: str) -> Path:
    if route == "/":
        return PUBLIC_DIR / "index.html"
    target = PUBLIC_DIR / route.lstrip("/")
    return target / "index.html"


def copy_static_files() -> None:
    if not STATIC_DIR.exists():
        raise FileNotFoundError(f"Static directory not found: {STATIC_DIR}")

    target_static = PUBLIC_DIR / "static"
    if target_static.exists():
        for item in target_static.iterdir():
            if item.is_file():
                item.unlink()
            else:
                import shutil

                shutil.rmtree(item)
    target_static.mkdir(parents=True, exist_ok=True)

    for root, dirs, files in os.walk(STATIC_DIR):
        root_path = Path(root)
        relative_root = root_path.relative_to(STATIC_DIR)
        target_root = target_static / relative_root
        target_root.mkdir(parents=True, exist_ok=True)
        for filename in files:
            source_file = root_path / filename
            target_file = target_root / filename
            target_file.write_bytes(source_file.read_bytes())


def save_route(client, route: str) -> None:
    response = client.get(route)
    if response.status_code != 200:
        raise RuntimeError(f"Failed to fetch {route}: {response.status_code}")

    output_path = route_to_output_path(route)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(response.data)
    print(f"Saved {route} -> {output_path}")


def save_sitemap_and_robots() -> None:
    for filename in ["sitemap.xml", "robots.txt"]:
        source = BASE_DIR / filename
        if source.exists():
            target = PUBLIC_DIR / filename
            target.write_bytes(source.read_bytes())
            print(f"Copied {filename} -> {target}")


def get_blog_routes() -> list[str]:
    with app.app_context():
        posts = BlogPost.query.filter_by(published=True).all()
    return [f"/blog/{post.slug}" for post in posts]


def main() -> None:
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    copy_static_files()
    save_sitemap_and_robots()

    with app.test_client() as client:
        all_routes = ROUTES + get_blog_routes()
        for route in sorted(set(all_routes)):
            save_route(client, route)
    print(f"Static export completed. Files are available in {PUBLIC_DIR}")


if __name__ == "__main__":
    main()
