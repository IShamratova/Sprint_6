from data.main_page_data import MainPageData


class MainPageLocator:

    # локатор поля «Сколько это стоит? И как оплатить?»
    FIRST_QUESTION = '(.//div[(@class="accordion__button")])[1]'
    # локатор поля ответа на «Сколько это стоит? И как оплатить?»
    FIRST_ANSWER = f'.//p[text() = "{MainPageData.FIRST_ANSWER_TEXT}"]'

    # локатор поля «Хочу сразу несколько самокатов! Так можно?»
    SECOND_QUESTION = '(.//div[(@class="accordion__button")])[2]'
    # локатор поля ответа на «Хочу сразу несколько самокатов! Так можно?»
    SECOND_ANSWER = f'.//p[text() = "{MainPageData.SECOND_ANSWER_TEXT}"]'

    # локатор поля «Как рассчитывается время аренды?»
    THIRD_QUESTION = '(.//div[(@class="accordion__button")])[3]'
    # локатор поля ответа на «Как рассчитывается время аренды?»
    THIRD_ANSWER = f'.//p[text() = "{MainPageData.THIRD_ANSWER_TEXT}"]'

    # локатор поля «Можно ли заказать самокат прямо на сегодня?»
    FOURTH_QUESTION = '(.//div[(@class="accordion__button")])[4]'
    # локатор поля ответа на «Можно ли заказать самокат прямо на сегодня?»
    FOURTH_ANSWER = f'.//p[text() = "{MainPageData.FOURTH_ANSWER_TEXT}"]'

    # локатор поля «Можно ли продлить заказ или вернуть самокат раньше?»
    FIFTH_QUESTION = '(.//div[(@class="accordion__button")])[5]'
    # локатор поля ответа на «Можно ли продлить заказ или вернуть самокат раньше?»
    FIFTH_ANSWER = f'.//p[text() = "{MainPageData.FIFTH_ANSWER_TEXT}"]'

    # локатор поля «Вы привозите зарядку вместе с самокатом?»
    SIXTH_QUESTION = '(.//div[(@class="accordion__button")])[6]'
    # локатор поля ответа на «Вы привозите зарядку вместе с самокатом?»
    SIXTH_ANSWER = f'.//p[text() = "{MainPageData.SIXTH_ANSWER_TEXT}"]'

    # локатор поля «Можно ли отменить заказ?»
    SEVENTH_QUESTION = '(.//div[(@class="accordion__button")])[7]'
    # локатор поля ответа на «Можно ли отменить заказ?»
    SEVENTH_ANSWER = f'.//p[text() = "{MainPageData.SEVENTH_ANSWER_TEXT}"]'

    # локатор поля «Я жизу за МКАДом, привезёте?»
    EIGHTH_QUESTION = '(.//div[(@class="accordion__button")])[8]'
    # локатор поля ответа на «Я жизу за МКАДом, привезёте?»
    EIGHTH_ANSWER = f'.//p[text() = "{MainPageData.EIGHTH_ANSWER_TEXT}"]'

    # локатор логотипа «Самокат»
    LOGO_SCOOTER = './/a[contains(@class, "Header_LogoScooter")]'

    # локатор логотипа «Яндекс»
    LOGO_YANDEX = './/a[contains(@class, "Header_LogoYandex")]'

    # локатор верхней кнопки «Заказать»
    NAV_BUTTON_ORDER = './/div[contains(@class, "Header_Nav")]/button[text() = "Заказать"]'
