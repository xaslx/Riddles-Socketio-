from pydantic import BaseModel


class Riddle(BaseModel):
    text: str
    answer: str

class Player(BaseModel):
    current_index: int
    name: str
    score: int
    count: int
    riddle: Riddle | None = None
    riddles: list 


riddles: list[Riddle] = [
    Riddle(text='Зимой и летом одним цветом', answer='елочка'),
    Riddle(text='Висит груша, нельзя скушать', answer='лампочка'),
    Riddle(text='Кто в дом зайдёт, меня за ручку возьмёт', answer='дверь'),
    Riddle(text='Зубов полон рот, а поесть не берёт', answer='расчестка'),
    Riddle(text='Держусь я только на ходу, а если встану — упаду', answer='велосипед'),
    Riddle(text='33 подружки в ровный ряд стоят, А перемешаешь — вмиг заговорят.', answer='алфавит'),
    Riddle(text='Все на свете отражает, Себя увидеть помогает, Перед ним красуются, Собой всегда любуются.', answer='зеркало'),
    Riddle(text='Если дождик с неба льет, Тебе поможет всегда...', answer='зонт'),
    Riddle(text='Желтый, кислый, кладут в чай. Его медом заливай. При простуде нужен он, А зовут его...', answer='лимон'),
    Riddle(text='Речка спятила с ума — По домам пошла сама.', answer='водопровод'),
    Riddle(text='Музыкант, певец, рассказчик — А всего труба да ящик.', answer='граммафон'),
    Riddle(text='На раскрашенных страницах Много праздников хранится.', answer='календарь'),
    Riddle(text='Ах, не трогайте меня: Обожгу и без огня!', answer='крапива'),
    Riddle(text='Маленькие домики по улице бегут, Мальчиков и девочек домики везут.', answer='машины'),
    Riddle(text='Пустые отдыхаем, А полные шагаем.', answer='сапоги')
]
