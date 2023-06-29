# def calculate_word_frequency(text):
#     # 將文字轉換為小寫，以統一單詞的大小寫
#     text = text.lower()

#     # 將標點符號從文字中刪除
#     for char in '.,?!"\'':
#         text = text.replace(char, '')

#     # 使用空格分割文字，得到單詞列表
#     words = text.split()

#     # 建立一個空字典來保存單詞頻率
#     word_frequency = {}

#     # 計算每個單詞的頻率
#     for word in words:
#         if word in word_frequency:
#             word_frequency[word] += 1
#         else:
#             word_frequency[word] = 1

#     return word_frequency

# # 測試程式碼
# article = """
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed varius mi id velit efficitur, non vestibulum mi ultricies. Curabitur facilisis, lorem sed eleifend aliquet, leo lectus suscipit ante, eget iaculis mauris erat a tortor. Integer pharetra lectus vitae aliquam ultrices. Etiam vel lacinia justo. Phasellus dignissim felis ut nisl convallis, in fringilla metus bibendum. Sed faucibus augue ac lacinia ullamcorper. Fusce laoreet est ac urna tincidunt, a convallis enim tincidunt. Duis tristique mi vitae facilisis finibus. Donec malesuada augue in tortor facilisis, in egestas elit congue. Aliquam vulputate metus eget ex dictum, eget laoreet orci fermentum. Nullam pellentesque mi ac varius cursus. Mauris eget nisi ac quam lacinia tristique. Integer id quam rutrum, rhoncus mi eu, dapibus lectus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Curabitur nec ante a justo tincidunt iaculis. Aliquam rhoncus ultricies diam, id tempor erat accumsan ac.
# """

# word_frequency = calculate_word_frequency(article)
# print(word_frequency)

from collections import Counter

def calculate_word_frequency(text):
    # 將文字轉換為小寫，以統一單詞的大小寫
    text = text.lower()

    # 將標點符號從文字中刪除
    for char in '.,?!"\'':
        text = text.replace(char, '')

    # 使用空格分割文字，得到單詞列表
    words = text.split()

    # 使用Counter計算單詞頻率
    word_frequency = Counter(words)

    return word_frequency

# 測試程式碼
article = """
Kyiv and Moscow exchanged accusations over the collapse of a sprawling dam in Ukraine's Russian-occupied Kherson region, triggering a wave of evacuations as floods of water spilled from the Nova Kakhovka hydro-electric plant.

Here are the latest developments:

"Terrorist attack and war crime": The Ukrainian defense ministry claimed Russian forces blew up the dam "in panic" amid heightening speculation that a major push by Kyiv to recapture land held by Russia’s occupying forces could be getting underway.
Moscow accuses Ukraine of "deliberate sabotage": Kremlin spokesperson Dmitry Peskov said he "strongly rejects" allegations Russia is responsible for damaging the dam, instead accusing Ukraine of "deliberate sabotage." He claimed Kyiv wanted to “deprive Crimea of water” and distract from the battlefield.
Mass evacuations: Ukrainian authorities have evacuated at least 885 people from the liberated west bank of the Dnipro River near the dam. Meanwhile, Russian-appointed authorities in Nova Kakhovka on the occupied east bank also said they were preparing evacuations due to rising water levels.
"The city is flooded": The Russian-appointed mayor of Nova Kakhovka said the southern Ukrainian city was submerged in water after the dam burst overnight.
Zaporizhzhia power plant: Further east, the UN's nuclear watchdog said it is "closely monitoring the situation" at the Zaporizhzhia power plant, following the destruction of the nearby Nova Kakhovka dam. The International Atomic Energy Agency said Tuesday there is "no immediate nuclear safety risk."
"""

word_frequency = calculate_word_frequency(article)
print(word_frequency)
