class OrderPageLocator:

    # локатор нижней кнопки «Заказать»
    LOWER_BUTTON_ORDER = './/button[(@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать")]'

    # локатор заголовка нового окна «Для кого самокат»
    HEADER_SCOOTER = './/div[text()="Для кого самокат"]'

    # локатор заголовка нового окна «Про аренду»
    HEADER_RENTAL = './/div[text()="Про аренду"]'

    # локатор кнопки «Далее»
    BUTTON_NEXT = './/button[(@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Далее")]'

    # локатор поля «Имя»
    FIRST_NAME = './/input[@placeholder="* Имя"]'

    # локатор поля «Фамилия»
    LAST_NAME = './/input[@placeholder="* Фамилия"]'

    # локатор поля «Адрес: куда привезти заказ»
    ADDRESS = './/input[@placeholder="* Адрес: куда привезти заказ"]'

    # локатор поля «Станция метро»
    METRO = './/input[@placeholder="* Станция метро"]'

    # локатор станции метро «Парк культуры»
    STATION_METRO = '(.//div[@class="select-search__select"]/ul/li)[1]/button'

    # локатор поля «Телефон: на него позвонит курьер»
    PHONE = './/input[@placeholder="* Телефон: на него позвонит курьер"]'

    # локатор поля «Когда привезти самокат»
    WHEN_BRING_SCOOTER = './/input[@placeholder="* Когда привезти самокат"]'

    # локатор выпадающего календаря
    CALENDAR = './/div[@class="react-datepicker__month-container"]'

    # локатор поля «Срок аренды»
    RENTAL_PERIOD = './/div[(@class="Dropdown-placeholder" and text()="* Срок аренды")]/parent::div'

    # локатор поля «трое суток»
    NUMBER_DAYS = './/div[(@class="Dropdown-option" and text()="трое суток")]'

    # локатор чек-бокса «чёрный жемчуг»
    COLOUR_SCOOTER = './/input[@id="black"]'

    # локатор поля «Комментарий для курьера»
    COMMENT_COURIER = './/input[@placeholder="Комментарий для курьера"]'

    # локатор заголовка всплывающего окна «Хотите оформить заказ?»
    HEADER_WANT_ORDER = './/div[text()="Хотите оформить заказ?"]'

    # локатор кнопки «Да» окна «Хотите оформить заказ?»
    BUTTON_YES = './/button[text()="Да"]'

    # локатор заголовка всплывающего окна «Заказ оформлен»
    HEADER_ORDER_REGISTER = './/div[text()="Заказ оформлен"]'

    # локатор кнопки «Да» окна «Хотите оформить заказ?»
    BUTTON_WATCH_STATUS = './/button[text()="Посмотреть статус"]'

    # локатор кнопки «Да» окна «Хотите оформить заказ?»
    BUTTON_ORDER_CANCEL = './/div[contains(@class, "Track_OrderInfo")]/button'






