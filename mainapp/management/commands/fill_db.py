from django.core.management import BaseCommand
from authapp.models import User
from resumeapp.models import Resume
from vacancyapp.models import Vacancy
from mainapp.models import Responses, BlogPost, Favorites
from django.utils import timezone
import datetime
import random


class Command(BaseCommand):
    tables = [User, Resume, Vacancy, Responses, BlogPost, Favorites]

    def handle(self, *args, **options):
        self.clear_all_tables()

        resume_quantity = 200
        vacancy_quantity = 200
        blog_post_quantity = 30
        applicant_quantity = 100
        company_quantity = 30

        first_name = ['Дмитрий', 'Николай', 'Никита', 'Максим', 'Сергей', 'Василий', 'Владимир', 'Игорь', 'Вячеслав']
        user_patronymic = ['Дмитриевич', 'Николаевич', 'Максимович', 'Сергеевич', 'Владимирович', 'Игоревич',
                           'Вячеславович', 'Никитич']
        last_name = ['Дмитриев', 'Николаев', 'Сергеев', 'Лебедев', 'Нилов', 'Прохоров', 'Рыльков', 'Аполлонов', 'Лашин']
        user_about = ['Пятилетний опыт продаж элитных женских товаров: косметика, парфюмерия, одежда. Заключала '
                      'договора с салонами и клиниками, проводила презентации продукции, разрабатывала маркетинговые '
                      'стратегии и планы сбыта. В совершенстве владею техниками продаж и являюсь экспертом в своей '
                      'деятельности. Легко нахожу общий язык с клиентами, умею контролировать эмоции и распоряжаться '
                      'своим временем.',
                      'Имею опыт ведения бухгалтерского и налогового учета, работала с различными системами '
                      'налогообложения (УСНО, ТСНО, ЕНВД), взаимодействовала с контролирующими и проверяющими '
                      'органами. Успешно осуществляла полное ведение бухгалтерии организаций. Владею программами 1С, '
                      'BISQUIT, SIRE, АиТСофт, DIASOFT, RS-Bank. Отличаюсь внимательным и ответственным подходом к '
                      'делу.',
                      'Эксперт по работе с полевой командой и ведению сложных переговоров, имею опыт заключения '
                      'договоров с крупными торговыми сетями. Умею формировать команду и выстраивать эффективную '
                      'мотивацию персонала. Всегда ориентируюсь на результат, быстро обучаюсь, легко усваиваю новую '
                      'информацию и ответственно подхожу к выполнению задач.',
                      'За рулем более 10 лет. Грамотно и аккуратно управляю машиной, знаю дороги города и области, '
                      'имею устойчивые навыки безаварийного вождения и хорошо знаком с устройством автомобилей. '
                      'Работал на авто представительского класса и совершал поездки на дальние расстояния. Не имею '
                      'вредных привычек, пунктуален и способен оптимально рассчитать маршрут.',
                      'В университете занималась организацией конференций. Окончила курсы актерского и ораторского '
                      'искусства, Благодаря участию в команде КВН – спокойно чувствую себя перед большой аудиторией. '
                      'Эффектно провожу презентации и легко завожу новые знакомства.',
                      'Имею опыт ведения переговоров с руководителями предприятий, заключал контракты на внедрение '
                      'энергосберегающих систем, координировал и контролировал выполнение ремонтных работ. '
                      'Обеспечивал бесперебойную работу предприятия: водоснабжение, электроснабжение, '
                      'лифтовое хозяйство, вентиляции. Работу выполняю качественно и быстро, внимательно и '
                      'ответственно отношусь к поручениям.',
                      '15 лет управления локальными и международными компаниями (промышленными и инвестиционными '
                      'процессами). Разрабатывал стратегии развития предприятий, обеспечивал финансово-хозяйственную '
                      'деятельность, повышал операционную эффективность бизнеса. Проводил тренинги и переговоры на '
                      'управленческом уровне. Работаю в режиме многозадачности, умею принимать решения и расставлять '
                      'приоритеты.',
                      ]
        password = '123456'

        company_name = ['НПО Развитие Инновационных Технологий', 'ЭкоКлимат', 'ВНИИСВ', 'Фобос', 'Эра Людей',
                        'Спартак Мебель', 'МУП Тверьгорэлектро']
        company_about = ['Это федеральная розничная сеть и надежный партнер крупнейших операторов связи. Мы '
                         'специализируемся на продаже тарифов и услуг операторов, цифровых и мобильных устройств, '
                         'аксессуаров к ним, а также на продвижении финансовых услуг и сервисов',
                         'Группа компаний "Наследие" - компания замкнутого цикла, способная самостоятельно решать '
                         'любые вопросы в сфере реставрации объектов культурного наследия, гражданского '
                         'строительства, энергоснабжения и инженерных сетей. Мы расширяем виды бизнеса, развиваемся и '
                         'растим команду!!!',
                         'С момента основания компания растет и развивается, учитывая конъюнктуру рынка. Дружная '
                         'команда специалистов постоянно повышает свой профессиональный уровень, что позволяет нам '
                         'занимать устойчивые позиции на рынке услуг в нескольких регионах России',
                         'Мы помогаем бизнесу других компаний развиваться с помощью современных IT-решений.',
                         'In 2015, our founder, Max Faldin, was trying to streamline cross-border fulfilment for '
                         'Chinese merchants during the e-commerce boom in Asia. He did well in all parts of the '
                         'fulfilment process except one – payments.',
                         'В портфель Группы компаний «Автоимпорт» входят 18 официальных брендов и 26 Дилерских '
                         'предприятия в четырех городах РФ: Рязань, Липецк, Тула, Тамбов (Mercedes-Benz, Toyota, '
                         'Lexus, Volkswagen, Hyundai, Skoda, Kia, Peugeot, Citroen, Haval, LADA, УАЗ, ГАЗ, Chevrolet, '
                         'Mitsubishi, Iveco, CHERRY, Honda).',
                         'Мы крупнейшая компания по ремонту бытовой техники в России.',
                         ]
        company_main_business = ['Оптовая торговля', 'Розничаня торговля', 'Разработка ПО', 'Грузоперевозки', 'Общепит']
        resume_name = ['Разработчик', 'Продавец', 'Директор', 'Водитель', 'Уборщик', 'Программист',
                       'Системный администратор', 'Инженер', 'Техник']
        cellphone = [89109333335, 89109333333, 89109999999, 89109998799, 89109879999, 89108889999, 89109999333,
                     89109999222, 89109999111, 89109999963]
        salary = [150000, 20000, 200000, 300000, 250000, 77000, 89000, 90000, 65000, 325000, 44000, 280000]
        education = ['Высшее', 'Среднее', 'Дополнительное', 'Среднее специальное']
        job_list = ['mail', 'yandex', 'google', 'rambler', 'facebook', 'vk']
        key_words = ['компетенция в заключении сделок', 'переговоры', 'опыт проведения презентаций',
                     'ведение и увеличение клиентской базы', 'заполнение договоров', 'контроль доставки продукции',
                     'уверенное владение компьютером']
        languages = ['Китайский', 'Английский', 'Испанский', 'Арабский', 'Русский', 'Немецкий', 'Французский']

        description = ['В мебельную компанию требуется категорийный менеджер по направлению офисная мебель',
                       'Производственный холдинг ищет технолога на направление производства корпусной'
                       ' мебели для железнодорожного транспорта и мебели по индивидуальным заказам',
                       'Эффективное управление корпоративным блоком филиала в составе 4 сотрудников\n'
                       'Развитие корпоративного бизнеса в регионе, привлечение новых клиентов и партнеров\n'
                       'Решение всех оперативных вопросов, отчетность по подразделению',
                       'Отбор, адаптация, обучение, мотивация управленческой команды филиала, численный рост ОП, '
                       'выстраивание бизнес-процессов для достижения необходимых результатов, управление '
                       'эффективностью бизнес-процессов, выполнение ключевых фин показателей, управление текучестью '
                       'персонала (в т.ч. вовлеченностью и удовлетворенностью)',
                       'Анализ рынка, конкурентный анализ, план-фактный анализ продаж, планирование продаж, '
                       'еженедельный отчет о проделанной работе, ежеквартальный отчет отдела',
                       'Выявление отклонений по бизнес-процессам, принятие мер по предотвращению отклонений, '
                       'выявление неэффективных бизнес-процессов, внесение предложений и участие в совещаниях по '
                       'оптимизации бизнес-процессов, снижение себестоимости бизнес-процессов без потери '
                       'эффективности, инициация изменения или внедрения новых бизнес-процессов',
                       'Планирование команды, участие в отборе кандидатов на вакантные должности, адаптация, '
                       'обучение, развитие, мотивация сотрудников, создание кадрового резерва. Управление текучестью',
                       'Бюджетирование и контроль расходов по отделам, формирование ежемесячных отчетов план|факт и '
                       'их анализ',
                       'Разработка регламентирующих документов, внутренних положений и политик компании',
                       'Подготовка отчетов согласно запросам руководства',
                       'Формирование и ведение баз данных клиентов.',
                       ]
        text = ['Рынок труда — зеркало того, что происходит на рынке в целом. С марта угроза эпидемии меняет нашу '
                'реальность. Чтобы вы могли держать руку на пульсе, мы решили наблюдать динамику рынка труда на hh.ru '
                'не ежемесячно, а еженедельно. Начиная с апреля, каждый вторник мы будем делиться здесь отчетами за '
                'предыдущую неделю.',
                'Мы постоянно работаем над улучшением CRM-платформы для рекрутинга Talantix. И не собираемся '
                'останавливаться! В марте команда сервиса интегрировала по-настоящему инновационные решения. И теперь '
                'технологическое оснащение Talantix опережает все существующие платформы российского рынка '
                'автоматизации рекрутинга. Заглянем в будущее? В нашем дайджесте мы рассказываем, как вы сможете '
                'применить инновации в своей работе уже сегодня и стать хедлайнером подбора персонала вместе с '
                'Talantix!',
                'Talantix (входит в HR-экосистему hh.ru) стал первой* российской CRM для рекрутинга, использующей '
                'технологии искусственного интеллекта для рекомендации и ранжирования наиболее подходящих кандидатов.',
                '12 марта 2021 г. состоялось подписание соглашения о сотрудничестве между Департаментом '
                'государственной службы занятости населения Ярославской области и hh.ru, крупнейшей российской '
                'онлайн-платформы по поиску работы и сотрудников.',
                'В нашем дайджесте мы собрали самые важные обновления сервиса Talantix в феврале, интересные '
                'материалы и советы для рекрутеров. А еще — анонсы самых долгожданных интеграций.',
                '15 сентября состоялось торжественное награждение российских компаний за лучшие проекты в области '
                'управления персоналом. Обладателями статуэток «профессионального Оскара» в этом году стали 23 '
                'лауреата.',
                'Мы продолжаем наблюдать за тем, как происходит возврат с внезапной удалёнки, вызванной эпидемией '
                'коронавируса, к обычному формату работы. Служба исследований hh.ru провела опрос работодателей, '
                'чтобы выяснить, много ли компаний уже начали возвращать сотрудников с удалёнки на обычные рабочие '
                'места. Опрос проводился с 7 по 20 июля 2020, в нем принял участие 81 работодатель.',
                '15 сентября состоится торжественная церемония вручения Премии HR-бренд 2019, которую мы ждали '
                'несколько месяцев.',
                'Совместно с Академией больших данных MADE от Mail.ru Group hh.ru составил портреты российских '
                'специалистов по анализу данных (Data Science) и машинному обучению (Machine Learning). Аналитики '
                'выяснили, где они живут и что умеют — а также чего ждут от них работодатели и как меняется спрос на '
                'таких профессионалов. Академия MADE и hh.ru проводят исследование уже второй год подряд. На этот раз '
                'эксперты проанализировали 10 500 резюме и 8100 вакансий.',
                '«Говорят, под Новый год что ни пожелается, всё всегда произойдет, всё всегда сбывается». Мы '
                'подготовили для вас новогодний мини-опрос о ваших мечтах про идеальную работу. И не только про нее.',
                'Согласны с известной пословицей? Мы — да: иметь под рукой больше одного источника информации о '
                'зарплатах, компенсациях и льготах гораздо лучше, чем иметь один. И удобнее, особенно если '
                'компоновать и сопоставлять их при этом не приходится вручную, и все доступно на одной странице. '
                ]
        title = ['Одна голова хорошо, а две лучше!',
                 'Культ профессии: без кого культуры нет?',
                 'Выберите лучшего работодателя',
                 '«Рейтинг работодателей-2017»: открыт прием заявок',
                 'Еще больше цифр про людей',
                 'Сделано в России. Подборка лучших приложений по версии Google',
                 'Конкурентов нужно знать в лицо',
                 'На саммите HR Digital 2017 выступит Дэвид Грин',
                 'Работодатели уточнят зарплату в вакансиях',
                 'Спрос на рабочий персонал вырос на 64% за год',
                 'В «Индексе HeadHunter» появилось сравнение статистики по периодам',
                 'Мы улучшили рекомендации вакансий'
                 ]
        # Супер юзер
        User.objects.create_superuser(username='admin', email='admin@test.ru', password='123456',
                                      user_about='Суперюзер', first_name='Админ',
                                      last_name='Администратор', user_patronymic='Админович')

        applicant_username = []
        company_username = []
        qnt = 1
        for i in range(applicant_quantity):
            User.objects.create_user(username=f'test{qnt}@test.ru',
                                     email=f'test{qnt}@test.ru',
                                     password=password,
                                     first_name=random.choice(first_name),
                                     last_name=random.choice(last_name),
                                     user_patronymic=random.choice(user_patronymic),
                                     user_age=random.randint(18, 60),
                                     user_about=random.choice(user_about))
            applicant_username.append(f'test{qnt}@test.ru')
            qnt += 1
        for i in range(company_quantity):
            User.objects.create_user(username=f'test{qnt}@test.ru',
                                     email=f'test{qnt}@test.ru',
                                     password=password,
                                     company_name=random.choice(company_name),
                                     company_about=random.choice(company_about),
                                     company_main_business=random.choice(company_main_business),
                                     company_since=timezone.now() - datetime.timedelta(days=random.randint(100, 3000)),
                                     is_staff=True)
            company_username.append(f'test{qnt}@test.ru')
            qnt += 1
        qnt = 1
        data = User.objects.filter(is_staff=True)
        for i in data:
            i.is_partner = True
            i.save()
            if qnt == len(data) // 2:
                break
            qnt += 1

        resume = []
        for i in range(resume_quantity):
            resume.append({'user': User.objects.filter(username=random.choice(applicant_username)).first(),
                           'resume_name': random.choice(resume_name),
                           'cellphone': random.choice(cellphone),
                           'salary': random.choice(salary),
                           'education': random.choice(education),
                           'job_list': random.choice(job_list),
                           'key_words': random.choice(key_words),
                           'languages': random.choice(languages), })
        for item in resume:
            Resume.objects.create(**item)
        qnt = 0
        for i in Resume.objects.all():
            i.is_draft = True
            i.save()
            qnt += 1
            if qnt == resume_quantity // 3:
                break
        for i in Resume.objects.filter(is_draft=False):
            i.is_approved = True
            i.save()
        qnt = 0
        data = Resume.objects.filter(is_approved=True)
        for i in data:
            i.is_active = True
            i.save()
            qnt += 1
            if qnt == len(data) // 2:
                break

        vacancy = []
        for i in range(vacancy_quantity):
            vacancy.append({'company': User.objects.filter(username=random.choice(company_username)).first(),
                            'vacancy_name': random.choice(resume_name),
                            'description': random.choice(description),
                            'salary': random.choice(salary), })

        for item in vacancy:
            Vacancy.objects.create(**item)

        qnt = 0
        for i in Vacancy.objects.all():
            i.is_draft = True
            i.save()
            qnt += 1
            if qnt == resume_quantity // 3:
                break
        for i in Vacancy.objects.filter(is_draft=False):
            i.is_approved = True
            i.save()
        qnt = 0
        data = Vacancy.objects.filter(is_approved=True)
        for i in data:
            i.is_active = True
            i.save()
            qnt += 1
            if qnt == len(data) // 2:
                break

        resume = Resume.objects.filter(is_active=True)
        responses = []
        qnt = 0
        for i in range(len(resume)):
            responses.append({'user': User.objects.filter(username=random.choice(company_username)).first(),
                              'resume': Resume.objects.filter(id=random.choice(resume).id).first()})
            qnt += 1
            if qnt == len(resume) // 2:
                break

        vacancy = Vacancy.objects.filter(is_active=True)
        qnt = 0
        for i in range(len(vacancy)):
            responses.append({'user': User.objects.filter(username=random.choice(applicant_username)).first(),
                              'vacancy': Vacancy.objects.filter(id=random.choice(vacancy).id).first()})
            qnt += 1
            if qnt == len(vacancy) // 2:
                break

        for item in responses:
            Responses.objects.create(**item)

        resume = Resume.objects.filter(is_active=True)
        favorites = []
        qnt = 0
        for i in range(len(resume)):
            favorites.append({'user': User.objects.filter(username=random.choice(company_username)).first(),
                              'resume': Resume.objects.filter(id=random.choice(resume).id).first()})
            qnt += 1
            if qnt == len(resume) // 2:
                break
        vacancy = Vacancy.objects.filter(is_active=True)
        qnt = 0
        for i in range(len(vacancy)):
            favorites.append({'user': User.objects.filter(username=random.choice(applicant_username)).first(),
                              'vacancy': Vacancy.objects.filter(id=random.choice(vacancy).id).first()})
            qnt += 1
            if qnt == len(vacancy) // 2:
                break

        for item in responses:
            Favorites.objects.create(**item)

        blog_post = []
        for i in range(blog_post_quantity):
            blog_post.append({'title': random.choice(title),
                              'text': random.choice(text), })
        for item in blog_post:
            BlogPost.objects.create(**item)

        #    self.show_all_tables()
        self.count_tables_data()

    def clear_all_tables(self):
        for table in self.tables:
            table.objects.all().delete()

    def count_tables_data(self):
        for table in self.tables:
            print(f'Количество записей в таблице {table.__name__}: {len(table.objects.all())}')
            if table.__name__ == 'User':
                print(f'Из них:\nКоличество соискателей - {len(table.objects.filter(is_staff=False))}\n'
                      f'Количество работодателей - '
                      f'{len(table.objects.filter(is_staff=True)) - len(table.objects.filter(is_superuser=True))} '
                      f'из них партнеров - {len(table.objects.filter(is_partner=True))}\n'
                      f'Количество суперпользователей - {len(table.objects.filter(is_superuser=True))}')
            elif table.__name__ == 'Resume' or table.__name__ == 'Vacancy':
                print(f'Из них:\nКоличество черновиков - {len(table.objects.filter(is_draft=True))}\n'
                      f'Количество проверенных - {len(table.objects.filter(is_approved=True))}, из них опубликовано'
                      f' - {len(table.objects.filter(is_active=True))}')

    def show_all_tables(self):
        for table in self.tables:
            print(table.objects.all())
