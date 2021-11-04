class InfoMessage:
    """Информационное сообщение о тренировке."""

    def __init__(self,
                 training_type: str,
                 duration: float,
                 distance: float,
                 speed: float,
                 calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        """Вернуть строку сообщения о тренировке."""
        info_str_rezult = (f'Тип тренировки: {self.training_type}; '
                           f'Длительность: {self.duration:.3f} ч.; '
                           f'Дистанция: {self.distance:.3f} км; '
                           f'Ср. скорость: {self.speed:.3f} км/ч; '
                           f'Потрачено ккал: {self.calories:.3f}.')
        return info_str_rezult


class Training:
    """Базовый класс тренировки."""
    LEN_STEP: float = 0.65
    M_IN_KM: float = 1000

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance_rezult = (self.action * self.LEN_STEP) / self.M_IN_KM
        return distance_rezult

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        get_mean_speed_rezult = self.get_distance() / self.duration
        return get_mean_speed_rezult

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        training_type = self.__class__.__name__
        duration = self.duration
        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spent_calories()
        training_info = InfoMessage(training_type,
                                    duration,
                                    distance,
                                    speed,
                                    calories)
        return training_info


class Running(Training):
    """Тренировка: бег."""
    coeff_calorie_1 = 18
    coeff_calorie_2 = 20
    coeff_minut: int = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float
                 ) -> None:
        super().__init__(action, duration, weight)

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        get_spent_calories_rezult = ((self.coeff_calorie_1
                                      * self.get_mean_speed()
                                      - self.coeff_calorie_2)
                                     * self.weight
                                     / self.M_IN_KM
                                     * self.duration
                                     * self.coeff_minut)
        return get_spent_calories_rezult

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        training_type = 'Running'
        duration = self.duration
        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spent_calories()
        training_info = InfoMessage(training_type,
                                    duration,
                                    distance,
                                    speed,
                                    calories)
        return training_info


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    coeff_calorie_1 = 0.035
    coeff_calorie_2 = 2
    coeff_calorie_3 = 0.029
    coeff_minut = 60

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float
                 ) -> None:
        super().__init__(action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        get_spent_calories_result = ((self.coeff_calorie_1
                                      * self.weight
                                      + (self.get_mean_speed()
                                         ** self.coeff_calorie_2
                                         // self.height)
                                      * self.coeff_calorie_3
                                      * self.weight)
                                     * self.duration
                                     * self.coeff_minut
                                     )
        return get_spent_calories_result

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        training_type = 'SportsWalking'
        duration = self.duration
        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spent_calories()
        training_info = InfoMessage(training_type,
                                    duration,
                                    distance,
                                    speed,
                                    calories)
        return training_info


class Swimming(Training):
    """Тренировка: плавание."""
    coeff_calorie_1 = 1.1
    coeff_calorie_2 = 2
    LEN_STEP = 1.38

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: int
                 ) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        get_mean_speed_rezult = (self.length_pool * self.count_pool
                                 / self.M_IN_KM / self.duration)
        return get_mean_speed_rezult

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        get_spent_calories_rezult = ((self.get_mean_speed()
                                      + self.coeff_calorie_1)
                                     * self.coeff_calorie_2 * self.weight)
        return get_spent_calories_rezult

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        training_type = 'Swimming'
        duration = self.duration
        distance = self.get_distance()
        speed = self.get_mean_speed()
        calories = self.get_spent_calories()
        training_info = InfoMessage(training_type,
                                    duration,
                                    distance,
                                    speed,
                                    calories)
        return training_info


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    type_training = {'RUN': Running, 'SWM': Swimming, 'WLK': SportsWalking}
    read_package_rez = type_training[workout_type](*data)
    return read_package_rez


def main(training: Training) -> None:
    """Главная функция."""
    info: InfoMessage = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
