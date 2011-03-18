
from useragents import search_strings

def detect_mobile(request):
  if request.headers.has_key("User-Agent"):
    # This takes the most processing. Surprisingly enough, when I
    # Experimented on my own machine, this was the most efficient
    # algorithm. Certainly more so than regexes.
    # Also, Caching didn't help much, with real-world caches.
    s = request.headers["User-Agent"].lower()
    for ua in search_strings:
      if ua in s:
        return True
  
  #Otherwise it's not a mobile
  return False

