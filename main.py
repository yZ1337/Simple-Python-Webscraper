from proxy_scraper import scrape_proxies
from any_website_scraper import any_website_scraper
from loading import loading

def main():
    while True:
        print("Choose an option:")
        print("1. Scrape proxies")
        print("2. Scrape a website on input")
        print("3. Quit")

        choice = input("> ")

        if choice == "1":
            values = scrape_proxies()
            with open('outputs/proxies.txt', 'w') as f:
                for value in values:
                    f.write(value + '\n')
            print(f"Scraped table with {len(values)} values.")

        elif choice == "2":
            website = input("Website: ")
            loading("Scraping Proxies First..")
            values = scrape_proxies()
            loading("Done Scraping, putting it in a file..")
            with open('outputs/proxies.txt', 'w') as f:
                for value in values:
                    f.write(value + '\n')
            print(f"\n Scraped table with {len(values)} values.")
            print("\n Saved it to proxies.txt")
            loading("Scraping Website..")
            stripped_website_input = website.replace('/', '')
            values = any_website_scraper(website)
            loading("Done scraping, putting it in a file..")
            with open(f'outputs/{stripped_website_input}.txt', 'w') as file:
                file.write(f'Scraping output for ({website}):\n')
                file.write('-----------------\n')
                file.write(values)
            print(f"\n Scraped table with {len(values)} values.")
            print(f"\n Saved it to {stripped_website_input}.txt")

        elif choice == "3":
            print("Quitting program...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

