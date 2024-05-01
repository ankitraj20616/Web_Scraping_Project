from requests import get
from bs4 import BeautifulSoup


class Game:
    def game_code(self) -> None:
        base_url = "http://quotes.toscrape.com"
        page_url = "/page/1"
        print("Wanna play game:-Y/N")
        x = input()
        if x != "Y" and x != "N":
            raise ValueError("Please input correct option next time!")
        if x == "N":
            print("Okiee Fine Don't Play..")
            return
        while True:
            req = get(f"{base_url}{page_url}",
                      headers={
                          "Accept": "text/plain"
                      })

            web_html = req.text

            soup = BeautifulSoup(web_html, "html.parser")

            data = soup.select(".quote")

            all_quotes = []

            for row in data:
                all_quotes.append({
                    "text": row.find(class_="text").get_text(),
                    "author": row.find(class_="author").get_text(),
                    "author_bio": row.find("a")["href"]
                })



            for quote in all_quotes:
                print(quote["text"])
                name = input("Guess The author name:-")
                if name == quote["author"]:
                    print("You guessed the write author name!...\nYou Win!")
                    return
                else:
                    print("OOPs!...Try again...")
            try:
                page_url = soup.find(class_="next").find("a")["href"]
            except:
                print("OPPS! No more Quotes!")
                break








if __name__ == "__main__":
    play = Game()
    play.game_code()