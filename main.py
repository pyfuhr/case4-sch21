from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.widget import MDWidget
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.icon_definitions import md_icons
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDIconButton
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.size = (470, 800)

from kivymd.uix.bottomnavigation import MDBottomNavigationItem

from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models.gigachat import GigaChat

# Авторизация в сервисе GigaChat
chat = GigaChat(credentials='ZjhmNDZlZDYtYzllYS00ZDJiLWJkOGMtMzRjMDY3MTAwOWQ5Ojc5Y2UzNzY5LWIyNDItNDI0NS1hZTQ4LTNhNzQ2ZTYzNmEyNw==', verify_ssl_certs=False)

messages = [
    SystemMessage(
        content="Я — СберКот, ваш личный виртуальный ассистент в мобильном приложении Сбербанка.\
            Могу ответить на вопросы о банковских продуктах, рассказать о последних новостях из мира финансов,\
            помочь оформить документы или выполнить операции, настроить автоматические переводы между счетами.\
            Если запрос выглядит как \"Государство\" то проедложи оплатить госпошлины.\
            Если запрос \"Дом\" или \"Мобильная связь\" то предложи оплатить платежи из этой категорию. Если это связано\
            с вкладом предоли стандартные банковские операции с ним\
            на вопрос \"что ты умеешь?\" отвечай: \"Я могу создавать перодические перевод, могу предлагать\
            персональные предложения, интересные вам, помогу ответить на ваши вопросы, могу помочь оформить простые справки\
            и собрать документы для их получения\""
    )
]

import time
t = 0

import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"

from kivy.properties import StringProperty
# md_bg_color: "green"

KV = """
<MD3Card>
    size_hint: None, None
    size: "150dp", "100dp"
    on_press: None
    
    MDRelativeLayout:
        Image:
            source: root.image
            height: 20
            pos: "12dp", "4dp"
        MDLabel:
            id: label
            text: root.text
            adaptive_size: True
            color: "grey"
            pos: "12dp", "12dp"
            bold: True

<MD5Card>
    size_hint: None, None
    size: "225dp", "100dp"
    on_press: None
    
    MDRelativeLayout:
        Image:
            source: root.image
            height: 20
            pos: "12dp", "4dp"
        MDLabel:
            id: label
            text: root.text
            adaptive_size: True
            color: "grey"
            pos: "12dp", "12dp"
            bold: True

<MD4Card>
    size_hint: None, None
    size: "450dp", "150dp"
    on_press: None
    
    MDBoxLayout:
        orientation: 'vertical'
        Image:
            source: 'res/13.png'

<ClickableTextFieldRound>:
    size_hint_y: None
    height: text_field.height

    MDTextField:
        id: text_field
        hint_text: root.htext
        text: root.text

    MDIconButton:
        icon: "arrow-right"
        pos_hint: {"center_y": .5}
        pos: text_field.width - self.width + dp(8), 0
        theme_text_color: "Hint"

<AssistScreen>:
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            padding: 5
            spacing: 5
            orientation: 'vertical'
            ScrollView:
                MDTextField:
                    id: ansfield
                    multiline: True
                    readonly: True
                    line_color_normal: self.fill_color_focus
                    line_color_focus: self.fill_color_focus
            Query:
                htext: "Напишите свой вопрос"

<Search>:
    size_hint_y: None
    height: search_query.height

    MDTextField:
        id: search_query
        hint_text: root.htext
        text: root.text

    MDIconButton:
        on_press: root.on_press()
        icon: "arrow-right"
        pos_hint: {"center_y": .5}
        pos: search_query.width - self.width + dp(8), 0
        theme_text_color: "Hint"

<Query>:
    size_hint_y: None
    height: text_query.height

    MDTextField:
        id: text_query
        hint_text: root.htext
        text: root.text

    MDIconButton:
        on_press: root.on_press()
        icon: "arrow-right"
        pos_hint: {"center_y": .5}
        pos: text_query.width - self.width + dp(8), 0
        theme_text_color: "Hint"            

<MainScreen>:
    MDBoxLayout:
        padding: 5
        orientation: 'vertical'
        Search:
            htext: "Задайте вопрос ассистенту"
        MDBottomNavigation:
            id: mbn
            #panel_color: "#eeeaea"
            selected_color_background: "green"
            text_color_active: "lightgrey"
            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Главный'
                icon: 'home'
                MDScrollView:
                    size: self.size
                    MDGridLayout:
                        spacing: 5
                        cols: 1
                        size_hint_y: None
                        height: '1090px'
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: 5
                            MD3Card:
                                text: ''
                                image: '0.png'
                            MD3Card:
                                text: ''
                                image: '0.png'
                            MD3Card:
                                text: ''
                                image: '0.png'
                        OneLineListItem:
                            text: "Перевести"
                        ClickableTextFieldRound:
                            htext: "На Сбер или в другой банк"
                        OneLineAvatarListItem:
                            text: "Между своими"
                            ImageLeftWidget:
                                source: "res/0.png"
                        OneLineAvatarListItem:
                            text: "В другую страну"
                            secondary_text: "Secondary text here"
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: 5
                            MD3Card:
                                text: '734 рублей'
                                image: 'res/5.png'
                            MD3Card:
                                text: 'Транспорт'
                                image: 'res/6.png'
                            MD3Card:
                                image: 'res/7.png'
                            ImageLeftWidget:
                                source: "res/1.png"
                        OneLineListItem:
                            text: "Кредиты"
                        BoxLayout:
                            orientation: 'horizontal'
                            spacing: 5
                            MD5Card:
                                text: 'Подобрать кредит'
                                image: 'res/8.png'
                            MD5Card:
                                text: 'Узнать одобренную сумму'
                                image: 'res/9.png'
                        OneLineListItem:
                            text: "Оплатить"
                        OneLineAvatarListItem:
                            text: "Оплатить по QR коду"

                            ImageLeftWidget:
                                source: "res/2.png"
                        OneLineAvatarListItem:
                            on_press: root.rtime(0)
                            on_release: root.rtime(1, self.text, 'f2')
                            text: "Мобильная связь"

                            ImageLeftWidget:
                                source: "res/3.png"
                        OneLineAvatarListItem:
                            text: "Дом"

                            ImageLeftWidget:
                                source: "res/4.png"
                        OneLineAvatarListItem:
                            text: "..."

                            ImageLeftWidget:
                                source: "kivymd/images/logo/kivymd-icon-256.png"
                        OneLineAvatarListItem:
                            text: "..."

                            ImageLeftWidget:
                                source: "kivymd/images/logo/kivymd-icon-256.png"
                        OneLineAvatarListItem:
                            text: "..."

                            ImageLeftWidget:
                                source: "kivymd/images/logo/kivymd-icon-256.png"
                        OneLineAvatarListItem:
                            text: "..."

                            ImageLeftWidget:
                                source: "kivymd/images/logo/kivymd-icon-256.png"

            MDBottomNavigationItem:
                name: 'screen 2'
                text: 'Накопления'
                icon: 'wallet'
                MDScrollView:
                    size: self.size
                    MDGridLayout:
                        spacing: 5
                        cols: 1
                        size_hint_y: None
                        height: '825px'
                        MD4Card:
                            text: '12'
                        OneLineListItem:
                            text: "Вклады и счета"
                        TwoLineAvatarListItem:
                            text: "Вклад в рублях"
                            secondary_text: "123.43 руб."
                            on_press: root.rtime(0)
                            on_release: root.rtime(1, self.text, 'f2')
                            ImageLeftWidget:
                                source: "res/11.png"
                        TwoLineAvatarListItem:
                            text: "Вклад в рублях"
                            on_press: root.rtime(0)
                            on_release: root.rtime(1, self.text, 'f2')
                            secondary_text: "12345.43 руб."
                            ImageLeftWidget:
                                source: "res/11.png"
                        TwoLineAvatarListItem:
                            text: "Вклад в долларах"
                            secondary_text: "5.43 $"
                            ImageLeftWidget:
                                source: "res/11.png"
                        TwoLineAvatarListItem:
                            text: "Вклад в металлах (золото)"
                            secondary_text: "12 унций (12345.43 руб.)"
                            ImageLeftWidget:
                                source: "res/12.png"
            AssistScreen:
                id: assist_screen
                name: 'screen 0'
                text: 'Ассистент'
                icon: 'res/20.png'
            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'Переводы'
                icon: 'bank-transfer'
                MDScrollView:
                    size: self.size
                    MDGridLayout:
                        spacing: 5
                        cols: 1
                        size_hint_y: None
                        height: '825px'
                        OneLineAvatarListItem:
                            text: "Мобильная связь"
                            on_press: root.rtime(0)
                            on_release: root.rtime(1, self.text, 'f2')
                            ImageLeftWidget:
                                source: "res/31.png"
                        OneLineAvatarListItem:
                            text: "Дом"
                            on_press: root.rtime(0)
                            on_release: root.rtime(1, self.text, 'f2')
                            ImageLeftWidget:
                                source: "res/32.png"
                        OneLineAvatarListItem:
                            text: "Государство"
                            on_press: root.rtime(0)
                            on_release: root.rtime(1, self.text, 'f2')
                            ImageLeftWidget:
                                source: "res/33.png"
                        OneLineAvatarListItem:
                            text: "Образование"
                            on_press: root.rtime(0)
                            on_release: root.rtime(1, self.text, 'f2')
                            ImageLeftWidget:
                                source: "res/34.png"
                        OneLineAvatarListItem:
                            text: "Транспорт"
                            on_press: root.rtime(0)
                            on_release: root.rtime(1, self.text, 'f2')
                            ImageLeftWidget:
                                source: "res/35.png"
                                
            MDBottomNavigationItem:
                icon: 'clock'
                name: 'screen 4'
                text: 'История'
                MDScrollView:
                    size: self.size
                    MDGridLayout:
                        spacing: 5
                        cols: 1
                        size_hint_y: None
                        height: '825px'
                        TwoLineAvatarListItem:
                            text: "Перевод Феодору К."
                            secondary_text: "30000 рублей"
                            ImageLeftWidget:
                                source: "res/52.png"
                        TwoLineAvatarListItem:
                            text: "Перевод от Феодора К."
                            secondary_text: "2 рублей"
                            ImageLeftWidget:
                                source: "res/53.png"
                        TwoLineAvatarListItem:
                            text: "Перевод от Феодора К."
                            secondary_text: "2 рублей"
                            ImageLeftWidget:
                                source: "res/53.png"
                        TwoLineAvatarListItem:
                            text: "Перевод между своими"
                            secondary_text: "200 рублей"
                            ImageLeftWidget:
                                source: "res/51.png"
                        TwoLineAvatarListItem:
                            text: "Перевод от Феодора К."
                            secondary_text: "2 рублей"
                            ImageLeftWidget:
                                source: "res/53.png"
                        TwoLineAvatarListItem:
                            text: "Перевод от Феодора К."
                            secondary_text: "2 рублей"
                            ImageLeftWidget:
                                source: "res/53.png"
                        TwoLineAvatarListItem:
                            text: "Перевод от Феодора К."
                            secondary_text: "2 рублей"
                            ImageLeftWidget:
                                source: "res/53.png"
            
"""

class ClickableTextFieldRound(MDRelativeLayout):
    text = StringProperty()
    htext = StringProperty()

class MD3Card(MDCard):
    text = StringProperty()
    image = StringProperty()

class MD5Card(MDCard):
    text = StringProperty()
    image = StringProperty()

class MD4Card(MDCard):
    text = StringProperty()

class Search(MDRelativeLayout):
    text = StringProperty()
    htext = StringProperty()
    def on_press(self):
        ma.msc.ids['assist_screen'].putText(self.ids['search_query'].text)
        self.ids['search_query'].text = ''
        ma.msc.ids["mbn"].switch_tab('screen 0')

class Query(MDRelativeLayout):
    text = StringProperty()
    htext = StringProperty()
    def on_press(self):
        ma.msc.ids['assist_screen'].putText(self.ids['text_query'].text)
        self.ids['text_query'].text = ''

class MainScreen(Screen):
    def rtime(self, m, f1=None, f2=None):
        global t
        if m:
            if (time.time()-t) > 0.3:
                if isinstance(f1, str):
                    ma.msc.ids['assist_screen'].putText(f1)
                    ma.msc.ids["mbn"].switch_tab('screen 0')
            else:
                try:
                    f2()
                except:
                    pass

        t = time.time()

class AssistScreen(MDBottomNavigationItem):
    def putText(self, req):
        if req:
            text = gigachat(req)
            self.ids['ansfield'].text += "Запрос: " + req + '\nОтвет: ' + text + '\n'


class MainApp(MDApp):
    def build(self):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        Builder.load_string(KV)
        self.sm = ScreenManager()
        self.msc = MainScreen(name='main')
        self.sm.add_widget(self.msc)
        self.asc = AssistScreen(name='assist')
        self.sm.add_widget(self.asc)
        return self.sm

def gigachat(text):
    messages.append(HumanMessage(content=text))
    res = chat(messages)
    messages.append(res)
    # Ответ модели
    return res.content

ma = MainApp()
ma.run()