import argparse

from wikipedia import summary, page

parser = argparse.ArgumentParser()
parser.add_argument('query', help='The Wikipedia page you want to search for')

args = parser.parse_args()

try:
    page_title = page(args.query).title
    page_summary = summary(args.query)
    print(page_title)
    print(page_summary)
except:
    print('Unable to find a Wikipedia page with that title.')


    # Scrape the summary of the page
    summary = scrape_summary(args.page_name)

    # Print the summary to the console
    print(summary)
