import pprint #美化print出的東西
def _save_database(info_dictionary):
    print("Save to DB complete!")
    pprint.pprint(info_dictionary)

#會員系統生成的流程
def handle_membership_creation(name, id, phone, *hobbies, **other_information): #不定參數 #可將args, kwargs代換hobby, gender #**key-value pair 參數
    gender = other_information['gender'] if 'gender' in other_information else "unknown"
    age = other_information['age'] if 'age' in other_information else "unknown"
    member_information = {
        'member_name': name,
        'member_personal_id': id,
        'member_cellphone_number': phone,
        'member_hobby': hobbies,
        'member_gender': gender,
        'member_age': age,
    }
    _save_database(info_dictionary = member_information)

if __name__ == '__main__':
    hobby = ['reading', 'travel', 'online game']
    info = {
        'gender': 'male',
        'age': 30,
        'born_city': 'I-lan'
    }
    handle_membership_creation("Wei-Kung", 'F123456789', '0912345678', *hobby, **info)