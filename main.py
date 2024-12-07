import os

from dotenv import load_dotenv

from api.cardtrader_api import CardtraderAPI
from cards.cardtrader_data_handler import CardtraderDataHandler


def main():
    nb_cheapest_cards = 5
    load_dotenv()
    api_key = os.getenv("API_KEY")

    expansion = 'Shimmering Skies'
    collection_numbers = ['004', '044', '048']
    condition = 'Near Mint'
    language = 'en'

    all_expansions = CardtraderAPI.get_all_expansions(api_key)
    expansion_id = CardtraderDataHandler.get_expansion_id(all_expansions, expansion)

    products = CardtraderAPI.get_products_by_expansion(api_key, expansion_id)
    products_flattened = CardtraderDataHandler.flatten_products(products)

    for collection_number in collection_numbers:
        cards = CardtraderDataHandler.parse_cards(products_flattened)
        cards = CardtraderDataHandler.filter_by_language(cards, language)
        cards = CardtraderDataHandler.filter_by_collection_number(cards, collection_number)
        cards = CardtraderDataHandler.filter_by_condition(cards, condition)
        if cards:
            price_cents = CardtraderDataHandler.get_average_cheapest_cards(cards, nb_cheapest_cards)
            print(f'Expansion: {expansion} | Card Name: {cards[0].name} | Collection Number: {collection_number} | Average price in cents for {nb_cheapest_cards} cheapest cards: {price_cents}')
        else:
            print('No cards are found')


if __name__ == '__main__':
    main()
