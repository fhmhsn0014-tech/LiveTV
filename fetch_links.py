import requests
import json

SOURCES = ["https://iptv-org.github.io/iptv/index.m3u"] # يمكنك إضافة روابط m3u أخرى هنا
TARGETS = ["beIN", "SSC", "Alkass", "AD Sports", "RMC", "Canal+"]

def scrape():
    channels = []
    for src in SOURCES:
        try:
            r = requests.get(src, timeout=10).text
            lines = r.split('\n')
            for i in range(len(lines)):
                if "#EXTINF" in lines[i]:
                    for t in TARGETS:
                        if t.lower() in lines[i].lower():
                            url = lines[i+1].strip()
                            if url.startswith("http"):
                                channels.append({
                                    "name": lines[i].split(',')[-1].strip(),
                                    "url": url,
                                    "logo": "https://via.placeholder.com/50/FF0000/FFFFFF?text=TV"
                                })
        except: continue
    
    with open('channels.json', 'w', encoding='utf-8') as f:
        json.dump(channels[:100], f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    scrape()
