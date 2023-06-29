from collections import Counter
from collections import namedtuple
major_tuple = namedtuple("major_element", ["major_element", "count"])
m_1 = major_tuple(major_element = 9, count = 100)
m_2 = major_tuple(major_element = 15, count = 78)

print(m_1, m_2)
print(m_1[0], m_2[0]) #取major_element
print(m_1.major_element) #取major_element
print(m_1.count) #取count