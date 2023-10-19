from django.test import TestCase

text_series_descriptions = [
    'BMW 1 Series - серия малолитражных автомобилей представительского класса (C-сегмент), выпускаемых ' \
    'BMW с 2004 года. Является преемником BMW 3 серии Compact и в настоящее время находится в третьем' \
    ' поколении. Позиционируемая как модель начального уровня в линейке продуктов BMW, первое поколение' \
    ' выпускалось в кузовах хэтчбек, купе и кабриолет.',
    'BMW 2 — серия автомобилей немецкого автопроизводителя BMW, занявшая нишу между'
    ' BMW 1-й серии и BMW 3-й серии. Данная серия автомобилей в виде купе (внутреннее'
    ' обозначение F22) впервые была представлена 25 октября 2013 года, а продажи'
    ' начались 8 марта 2014 года.', 'Несколько поколений легковых автомобилей среднего класса выпускаемых'
                                    ' с 1975 года немецким автопроизводителем BMW. Отличаются большим выбором'
                                    ' кузовов, разнообразием двигателей и наличием спортивных версий. Самая'
                                    ' успешная серия автомобилей в истории компании',
    'BMW 4 (F32) — серия компактных престижных автомобилей BMW, выпуск которых начался'
    ' в июле 2013 года. Серия представляет собой отделившиеся от BMW 3 серии кузова купе'
    ' и кабриолет. Помимо обычных автомобилей, с 2014 года выпускается также спортивная'
    ' версия BMW M4. Предшественником нынешнего поколения (F32 (купе)/F33 (кабриолет)/F36'
    ' (четырёхдверное купе)) является BMW E92/E93, относившийся к BMW 3 серии.']


class TestBMWSeries(TestCase):
    def test_homepage(self):
        response = self.client.get('/home/')

        self.assertEquals(response.status_code, 200)
        self.assertIn('Это основная страница', response.content.decode())

    def test_series1(self):
        for i in range(1, 6):
            response = self.client.get(f'/home/{i}series')
            try:
                text = text_series_descriptions[i - 1]
            except IndexError:
                text = ''
            self.assertEquals(response.status_code, 200)
            self.assertIn(text, response.content.decode())

    def test_series1_redirect(self):
        for i in range(1, 6):
            response = self.client.get(f'/home/{i}')
            self.assertEquals(response.status_code, 302)
            print(response.status_code)