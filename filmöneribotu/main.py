import requests

API_KEY = "eb25b0503f3764abff4506c6b958985f"
BASE_URL = "https://api.themoviedb.org/3"

def kategoriye_gore_film_oner(kategori):
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": kategori,
        "language": "tr-TR",
        "page": 1
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("API'den veri alınamadı.")
        return

    veriler = response.json()
    filmler = veriler.get("results", [])[:5]

    if not filmler:
        print("Film bulunamadı.")
        return

    for film in filmler:
        print(f"\n🎬 {film['title']}")
        print(f"📅 Yıl: {film.get('release_date', 'Bilinmiyor')}")
        print(f"📝 Açıklama: {film.get('overview', 'Yok')}")

if __name__ == "__main__":
    kategori = input("Hangi türde film istersiniz? (örnek: aksiyon, komedi, dram): ")
    kategoriye_gore_film_oner(kategori)
