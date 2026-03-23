import requests
import os
from colorama import init, Fore, Style

os.system('')
init(autoreset=True)

class CraftriseChecker:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': '*/*',
            'Accept-Language': 'tr-TR,tr;q=0.6',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.craftrise.com.tr',
            'Referer': 'https://www.craftrise.com.tr/urun/2369RC',
            'X-Requested-With': 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        })
        self.api_url = 'https://www.craftrise.com.tr/posts/post-search.php'

    def check_if_banned(self, username):
        try:
            response = self.session.post(
                self.api_url, 
                data={'username': username}, 
                timeout=5
            )

            if response.status_code == 200:
                try:
                    result = response.json()
                    
                    if result.get('resultType') == 'error' and result.get('resultMessage') == 'bu hesap kapalı ban yemis lifetime':
                        print(f"{Fore.RED}{username} adlı oyuncu banli.{Style.RESET_ALL}")
                        return True
                    else:
                        print(f"{Fore.GREEN}{username} adlı oyuncu temiz.{Style.RESET_ALL}")
                        return False
                        
                except ValueError:
                    print(f"{Fore.YELLOW}Beklenmeyen yanıt IP ban yemiş veya Cloudflare'a takılmış olabilirsin.{Style.RESET_ALL}")
                    return None
            else:
                print(f"{Fore.YELLOW}Sunucu Hatası: Durum Kodu {response.status_code}{Style.RESET_ALL}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}Bağlantı hatası: {e}{Style.RESET_ALL}")
            return None

if __name__ == '__main__':
    print(f"{Fore.CYAN}Craftrise Oyuncu Checker{Style.RESET_ALL}")
    checker = CraftriseChecker()
    
    while True:
        username = input(f"\n{Fore.WHITE}Kullanıcı adı gir ('exit' ile çık): {Style.RESET_ALL}").strip()

        if username.lower() == 'exit':
            print(f"{Fore.CYAN}Kapatılıyor...{Style.RESET_ALL}")
            break

        if not username:
            print(f"{Fore.YELLOW}Lütfen boş bırakmayın!{Style.RESET_ALL}")
            continue

        checker.check_if_banned(username)
