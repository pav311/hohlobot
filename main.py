import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import time
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="") #тут токен
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        if event.user_id==1:# тут айди
            vk.messages.send(chat_id=event.chat_id,
                message=random.choice(("ХОХЛА НЕ СПРАШИВАЛИ",
                    "хохол проснулся",
                    "угомонись хохлинка))",
                    "!!!ТУТ НЕ ХРЮКАТЬ!!!","хрю-хрю))",
                    "свин))))",
                    "🇺🇦г🇺🇦е💩р🇺🇦б🇺🇦 хохлов)",
                    "не ваняй тут свин",
                    "свина забыли спросить)))")),
                reply_to=event.message_id,
                random_id=random.randint(1,999999)
            )
        elif  "не хохол" in event.text.lower() or "крым" in event.text.lower() or "украин" in event.text.lower() or "хрю" in event.text.lower() or "либер" in event.text.lower():
            vk.messages.send(chat_id=event.chat_id, 
                message=random.choice(("ХОХЛА НЕ СПРАШИВАЛИ",
                    "хохол проснулся",
                    "угомонись хохлинка))",
                    "!!!ТУТ НЕ ХРЮКАТЬ!!!","хрю-хрю))",
                    "свин))))",
                    "🇺🇦г🇺🇦е💩р🇺🇦б🇺🇦 хохлов)",
                    "не ваняй тут свин",
                    "свина забыли спросить)))")),
                reply_to=event.message_id,
                random_id=random.randint(1,999999)
            )
