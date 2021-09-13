import unittest
from app.models import Articles

#Articles = articles.Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test to test the behaviour of the Articles class
    '''
    def setUp(self):
        '''
        Set up method that will run before every test
        '''
        self.new_article = Articles(
            'John Rogers',
            'Cryptocurrency latest news – Bitcoin legalized by Ukraine after El Salvador adopts it as legal tender... - The Sun',
            '- Why is the cryptocurrency market down today?- Shiba Inu price prediction 2021: Can the cryptocurrency hit $1?- Ethereum price prediction 2021: Can the...',
            'https://www.the-sun.com/money/3645940/cryptocurrency-latest-bitcoin-legalized-ukraine-el-salvador/',
            'https://www.the-sun.com/wp-content/uploads/sites/6/2021/09/lv-comp-crypto-currency-blog-1.jpg?strip=all&quality=100&w=1200&h=800&crop=1',
            '2021-09-12T14:31:00Z',
            'WHAT HAS BEEN THE RESPONSE TO BITCOIN BECOMING EL SALVADORS NATIONAL CURRENCY?\r\nProponents of El Salvadors decision have hailed the move as the progressive future of money.\r\nCritics, however, have … [+1279 chars]'
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

if __name__ == '__main__':
    unittest.main()
